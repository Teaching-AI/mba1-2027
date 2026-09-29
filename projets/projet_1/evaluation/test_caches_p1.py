"""
Tests caches - Projet 1 (10 points). ENSEIGNANT UNIQUEMENT.
Ne jamais copier ce fichier dans le template etudiant.

Lance avant la soutenance par templates/run_hidden_tests.sh :
    ./templates/run_hidden_tests.sh projet-1 projets/projet_1/evaluation/test_caches_p1.py

Principe : memes fonctions que les tests publics, cas differents. Un groupe qui a
code pour faire passer les tests publics (valeurs en dur, cas particuliers oublies)
perd des points ici. Un groupe qui a compris ne perd rien.
"""

import os
import random
import sys

import pytest

PROJECT_ROOT = os.getcwd()
sys.path.insert(0, PROJECT_ROOT)


@pytest.fixture
def stats():
    import analysis.stats as m
    return m


@pytest.fixture
def reg():
    import analysis.regression as m
    return m


def _dvf():
    import pandas as pd
    for name in ["dvf_toulon.csv", "dvf.csv", "dvf_83137.csv"]:
        p = os.path.join(PROJECT_ROOT, "data", name)
        if os.path.exists(p):
            return pd.read_csv(p, low_memory=False)
    pytest.fail("DVF absent")


# --- Statistiques (4 pts) ---------------------------------------------------

def test_median_paire_non_triee(stats):
    """[1 pt] Mediane d'une liste paire non triee."""
    assert stats.median([10, 2, 8, 4]) == pytest.approx(6.0)


def test_mean_variance_aleatoire(stats):
    """[1 pt] Moyenne et variance sur des donnees aleatoires (detecte les valeurs en dur)."""
    rnd = random.Random(42)
    xs = [rnd.uniform(1000, 6000) for _ in range(200)]
    m = sum(xs) / len(xs)
    v = sum((x - m) ** 2 for x in xs) / (len(xs) - 1)
    assert stats.mean(xs) == pytest.approx(m, rel=1e-6)
    assert stats.variance(xs) == pytest.approx(v, rel=1e-6)


def test_correlation_negative(stats):
    """[1 pt] Correlation negative parfaite."""
    assert stats.correlation([1, 2, 3, 4], [8, 6, 4, 2]) == pytest.approx(-1.0, abs=1e-6)


def test_correlation_ecart_type_nul(stats):
    """[1 pt] Correlation avec une serie constante : 0, pas de division par zero."""
    assert stats.correlation([1, 2, 3], [5, 5, 5]) == 0


# --- Regression (3 pts) ------------------------------------------------------

def test_r_squared_imparfait(reg):
    """[1 pt] R2 sur des donnees bruitees, compare au calcul de reference."""
    x = [30, 45, 60, 75, 90]
    y = [110_000, 150_000, 205_000, 230_000, 300_000]
    alpha, beta = reg.least_squares_fit(x, y)
    assert beta == pytest.approx(3066.67, rel=1e-3)
    assert reg.r_squared(alpha, beta, x, y) == pytest.approx(0.9833, abs=1e-3)


def test_regression_sur_leurs_donnees(reg):
    """[2 pts] Regression prix ~ surface sur le DVF du groupe : pente positive, R2 dans [0, 1]."""
    df = _dvf()
    cols = {c.lower(): c for c in df.columns}
    surf = cols.get("surface_reelle_bati") or cols.get("surface")
    prix = cols.get("valeur_fonciere") or cols.get("prix")
    if not surf or not prix:
        pytest.fail(f"Colonnes surface/prix introuvables : {list(df.columns)}")
    d = df[[surf, prix]].dropna()
    d = d[(d[surf] > 10) & (d[surf] < 300) & (d[prix] > 20_000)]
    x, y = d[surf].astype(float).tolist(), d[prix].astype(float).tolist()
    alpha, beta = reg.least_squares_fit(x, y)
    r2 = reg.r_squared(alpha, beta, x, y)
    assert beta > 0, f"Pente negative ({beta:.0f} EUR/m2) : donnees ou calcul a verifier"
    assert 0 <= r2 <= 1, f"R2 hors de [0, 1] : {r2}"


# --- Donnees (3 pts) ---------------------------------------------------------

def test_dvf_filtre_logements():
    """[1 pt] DVF filtre sur Appartement / Maison."""
    df = _dvf()
    col = next((c for c in df.columns if c.lower() == "type_local"), None)
    assert col, "Colonne type_local absente"
    types = set(df[col].dropna().unique())
    assert types <= {"Appartement", "Maison"}, f"Types non filtres : {types}"


def test_dvf_recent():
    """[1 pt] DVF limite aux 3 dernieres annees."""
    import pandas as pd
    df = _dvf()
    col = next((c for c in df.columns if c.lower() == "date_mutation"), None)
    assert col, "Colonne date_mutation absente"
    oldest = pd.to_datetime(df[col], errors="coerce").min()
    assert oldest >= pd.Timestamp.now() - pd.DateOffset(years=3), f"Transaction la plus ancienne : {oldest.date()}"


def test_prix_m2_plausible():
    """[1 pt] Mediane du prix/m2 plausible pour Toulon (1 500 - 7 000 EUR)."""
    df = _dvf()
    cols = {c.lower(): c for c in df.columns}
    surf = cols.get("surface_reelle_bati") or cols.get("surface")
    prix = cols.get("valeur_fonciere") or cols.get("prix")
    d = df[[surf, prix]].dropna()
    d = d[d[surf] > 10]
    med = (d[prix] / d[surf]).median()
    assert 1500 <= med <= 7000, f"Mediane prix/m2 = {med:.0f} EUR : doublons de lots ou filtre manquant ?"
