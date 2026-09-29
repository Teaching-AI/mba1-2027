# NidBuyer — votre acheteur IA à Toulon

> Projet 2 — MBA1 IA & Transformation des organisations, 2027

## Équipe

| Membre | Périmètre principal |
|--------|------|
| Prénom NOM | Lead architecture + déploiement |
| Prénom NOM | RAG + ingestion + Supabase |
| Prénom NOM | Scoring DVF + médianes par quartier + prompts |
| Prénom NOM | R&D Vision + frontend |

Chaque membre doit pouvoir expliquer **toutes** les parties en soutenance, pas seulement la sienne.

## Démo

- Frontend : https://TODO
- API : https://TODO

(Garder le format « API : https://... » : le CI lit cette ligne et appelle `/health`.)

Nombre d'annonces indexées : **XXX** (au JJ/MM) ← *à mettre à jour*

## Architecture

```
GitHub Actions (7h00) ──POST /admin/sync──▶ ┌──────────────────────────┐
                                             │ API FastAPI (hébergée)   │──▶ Gemini (clé d'API)
Sources ──scraping──────────────────────────▶│  ingestion · RAG · score │
(BienIci, agences...)                        └───────────┬──────────────┘
                                                         │ source de vérité
                                              Supabase (PostgreSQL)
Frontend Streamlit (hébergé) ──HTTP──▶ API
```

- **Supabase** garde les annonces. **ChromaDB** est un index local, reconstruit au démarrage
  du conteneur (le disque d'un hébergement cloud est effacé à chaque redémarrage).
- **Tous les appels LLM passent par `backend/llm.py`** (fourni). Changer de fournisseur
  = changer `LLM_PROVIDER`, pas le code (Gemini, Vertex AI, ou un modèle local via Ollama).
- Les calculs (prix au m², écart à la médiane, rendement) sont faits **en Python**.
  Le LLM rédige à partir de ces chiffres ; il ne calcule jamais.

```
backend/
├── main.py        # API — contrats de réponse dans les docstrings
├── llm.py         # FOURNI — accès unique aux LLM (gemini | vertex | ollama | fake)
├── db.py          # FOURNI — lecture/écriture Supabase
├── rag.py         # ChromaDB — à implémenter
├── scoring.py     # Score d'opportunité — à implémenter
├── marche.py      # Médianes DVF par quartier
├── ingestion.py   # Sources → Supabase → ChromaDB → alertes
├── alert.py       # Alertes e-mail / Slack
└── sources/       # BienIci · LeBonCoin · Générique (LLM)
frontend/          # Streamlit — service séparé (son propre Dockerfile)
vision/            # R&D : CNN ou LLM multimodal
prompts/           # Prompts + EXPERIMENTS.md
tests/             # test_auto_eval.py (NE PAS MODIFIER) + vos tests
```

## Lancer en local

```bash
cp .env.example .env            # puis remplir
pip install -r requirements.txt

uvicorn backend.main:app --reload                 # API    → http://localhost:8000/docs
streamlit run frontend/app.py                     # Front  → http://localhost:8501
```

Sans accès GCP (train, avion) : `LLM_PROVIDER=fake` pour développer sans appel réel.

## Supabase

Créer un projet gratuit sur https://supabase.com, puis la table `annonces`
(SQL dans l'en-tête de [`backend/db.py`](backend/db.py)). Importer les annonces de P1 :

```python
import pandas as pd
from backend import db
df = pd.read_csv("annonces_p1.csv")          # vos CSV de P1, fusionnés et dédoublonnés
df["id"] = "p1-" + df.index.astype(str)
db.enregistrer_annonces(df.to_dict("records"))
```

## Déployer

Recommandé : **Hugging Face Spaces** (gratuit, 16 Go de RAM, assez pour le modèle d'embedding).
Render ou Railway fonctionnent aussi, mais leurs offres gratuites (512 Mo) sont trop justes pour l'API.

**API** : https://huggingface.co/new-space → SDK **Docker** → pousser le repo dans le Space
(ou le relier au repo GitHub). Dans *Settings > Variables and secrets* du Space :

| Nom | Type | Valeur |
|---|---|---|
| `PORT` | variable | `7860` |
| `LLM_PROVIDER` | variable | `gemini` |
| `LLM_MODEL` | variable | modèle donné par l'enseignant |
| `SUPABASE_URL` | variable | URL de votre projet Supabase |
| `GEMINI_API_KEY` | **secret** | votre clé AI Studio |
| `SUPABASE_KEY` | **secret** | clé service_role Supabase |
| `ADMIN_TOKEN` | **secret** | une chaîne aléatoire (`openssl rand -hex 16`) |

URL de l'API : `https://<compte>-<space>.hf.space` → à mettre dans la section Démo.

**Frontend** : un second Space, SDK Docker, avec le contenu de `frontend/` et la variable
`API_URL` = URL de l'API. (Ou Streamlit Community Cloud, fichier `frontend/app.py`.)

**Synchro quotidienne à 7h** : le workflow `.github/workflows/sync.yml` appelle `/admin/sync`.
Créer dans le repo GitHub les secrets `API_URL` et `ADMIN_TOKEN`, puis le lancer une fois à la main
(onglet *Actions* > *Synchro quotidienne* > *Run workflow*).

> Aucune clé dans le code, dans le Dockerfile ou dans un commit. Une clé qui fuit se fait
> utiliser par d'autres en quelques heures, à vos frais.

## Choix à justifier (le jury les demandera)

- Modèle d'embedding et texte encodé par annonce (`rag.texte_a_encoder`)
- Rattachement des ventes DVF à un quartier (voir `backend/marche.py`)
- Seuils opportunité / prix du marché / surévalué
- Démarrage à froid après mise en veille de l'hébergement : quelle expérience utilisateur, quelle parade ?

## Prompt engineering

[`prompts/EXPERIMENTS.md`](prompts/EXPERIMENTS.md) — 3 versions comparées sur le jeu de test du module 2, avec des chiffres.

## R&D Vision

[`vision/APPROACH.md`](vision/APPROACH.md) — approche retenue, précision mesurée, limites.
