"""
Tests caches - Projet 2 NidBuyer (10 points). ENSEIGNANT UNIQUEMENT.
Ne jamais copier ce fichier dans le template etudiant.

    ./templates/run_hidden_tests.sh projet-2 projets/projet_2/evaluation/test_caches_p2.py

Memes contrats que les tests publics (docstrings de backend/scoring.py, rag.py, main.py),
autres cas : valeurs manquantes, filtres, idempotence, securite, format de reponse.
"""
import os
import sys

import pytest

ROOT = os.getcwd()
sys.path.insert(0, ROOT)
os.environ["LLM_PROVIDER"] = "fake"
os.environ["ADMIN_TOKEN"] = "jeton-cache"
os.environ["SUPABASE_URL"] = "https://placeholder.supabase.co"

ANNONCES = [
    {"id": "h1", "type": "T3", "surface": 70, "quartier": "Mourillon", "prix": 230_000,
     "description": "T3 lumineux avec balcon, proche plages du Mourillon."},
    {"id": "h2", "type": "T2", "surface": 40, "quartier": "Centre", "prix": 120_000,
     "description": "T2 en centre-ville, idéal investissement locatif, proche gare."},
    {"id": "h3", "type": "T4", "surface": 90, "quartier": "Mourillon", "prix": 520_000,
     "description": "T4 familial vue mer, terrasse, parking."},
    {"id": "h4", "type": "maison", "surface": 110, "quartier": "Cap Brun", "prix": 440_000,
     "description": "Maison avec jardin, calme, quartier résidentiel, proche écoles."},
]


@pytest.fixture(scope="module")
def rag(tmp_path_factory):
    os.environ["CHROMA_PATH"] = str(tmp_path_factory.mktemp("chroma_cache"))
    import backend.rag as m
    m._client = None
    m.indexer_annonces(ANNONCES)
    return m


# --- Scoring (4 pts) ---------------------------------------------------------

def test_scoring_donnees_manquantes():
    """[1 pt] Surface absente ou mediane inconnue : label 'inconnu', pas d'exception."""
    from backend.scoring import score_opportunite
    assert score_opportunite({"prix": 200_000, "surface": None}, 3400, "rp")["label"] == "inconnu"
    assert score_opportunite({"prix": 200_000, "surface": 50}, None, "rp")["label"] == "inconnu"


def test_scoring_profil_inconnu():
    """[1 pt] Profil inconnu : ValueError."""
    from backend.scoring import score_opportunite
    with pytest.raises(ValueError):
        score_opportunite({"prix": 200_000, "surface": 50}, 3400, "retraite")


def test_rendement_locatif():
    """[1 pt] Rendement brut et net selon la convention du cours."""
    from backend.scoring import rendement_locatif
    r = rendement_locatif({"prix": 150_000}, 750)
    assert r["rendement_brut_pct"] == pytest.approx(6.0, abs=0.01)
    assert r["rendement_net_pct"] == pytest.approx(4.5, abs=0.01)


def test_fiche_prix_m2_du_bien():
    """[1 pt] La fiche contient aussi le prix au m2 du bien (215 000 / 68 = 3 162)."""
    from backend.scoring import fiche_decision
    fiche = fiche_decision({"prix": 215_000, "surface": 68}, {"mediane_prix_m2": 3400})
    assert "3162" in fiche.replace(" ", "").replace(" ", "").replace("\xa0", "")


# --- RAG (3 pts) -------------------------------------------------------------

def test_reindexation_sans_doublon(rag):
    """[1 pt] Reindexer les memes annonces ne cree pas de doublon."""
    rag.indexer_annonces(ANNONCES)
    assert rag.get_collection().count() == len(ANNONCES)


def test_filtre_quartier(rag):
    """[1 pt] filtre_meta restreint au quartier demande."""
    r = rag.search_similar("appartement", n_results=4, filtre_meta={"quartier": "Mourillon"})
    assert r and {b["quartier"] for b in r} == {"Mourillon"}


def test_n_results_superieur_a_l_index(rag):
    """[1 pt] Demander plus de resultats que d'annonces : pas d'erreur."""
    assert len(rag.search_similar("maison", n_results=50)) == len(ANNONCES)


# --- API (3 pts) -------------------------------------------------------------

@pytest.fixture(scope="module")
def client(rag):
    from fastapi.testclient import TestClient
    from backend.main import app
    with TestClient(app) as c:
        yield c


def test_sync_protegee(client):
    """[1 pt] /admin/sync refuse un appel sans jeton."""
    assert client.post("/admin/sync").status_code in (401, 403)
    assert client.post("/admin/sync", headers={"X-Admin-Token": "mauvais"}).status_code in (401, 403)


def test_rechercher_contrat(client):
    """[2 pts] /rechercher : 5 resultats max, budget respecte, champs du contrat, mention IA."""
    r = client.post("/rechercher", json={"intention": "rp", "budget_max": 300_000})
    assert r.status_code == 200, r.text[:300]
    data = r.json()
    assert data.get("mention_ia"), "Champ mention_ia absent (AI Act art. 50)"
    res = data["resultats"]
    assert 1 <= len(res) <= 5
    assert all(b["prix"] <= 300_000 for b in res), "Bien au-dessus du budget renvoye"
    assert all({"id", "score", "label", "analyse"} <= b.keys() for b in res)
