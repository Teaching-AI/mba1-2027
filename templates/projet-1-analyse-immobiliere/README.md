# Projet 1 : Observatoire du Marche Immobilier Toulonnais

## Objectif

Construire une application web deployee qui analyse le marche immobilier toulonnais en temps reel, avec des algorithmes statistiques implementes from scratch.

## Evaluation automatique

A chaque `git push`, le CI evalue automatiquement votre travail.
Consultez l'onglet **Actions** > dernier workflow > **Job Summary** pour voir votre score.

**Tests publics : 15 points.** 10 points de tests caches (memes fonctions, autres cas) sont lances
par l'enseignant la veille de la soutenance. Le reste de la note est evalue par l'enseignant et en soutenance.

Faire passer les tests publics ne suffit pas : ecrivez du code juste, pas du code qui passe les tests.

## Structure du projet

```
.
├── analysis/
│   ├── stats.py          <- Fonctions statistiques from scratch (Grus ch.5)
│   ├── regression.py     <- Regression lineaire from scratch (Grus ch.14)
│   └── scoring.py        <- Score d'opportunite par bien
├── app/
│   └── streamlit_app.py  <- Dashboard principal (ou app.py a la racine)
├── data/
│   ├── dvf_toulon.csv    <- Donnees DVF (>= 500 transactions)
│   └── annonces.csv      <- Annonces reelles collectees
├── tests/
│   ├── test_stats.py     <- Vos tests (5 minimum au total, hors test_auto_eval.py)
│   ├── test_regression.py
│   └── test_auto_eval.py <- Tests d'evaluation (NE PAS MODIFIER)
├── requirements.txt
└── README.md             <- Ce fichier (ajoutez l'URL de deploiement !)
```

## Installation

```bash
git clone <votre-url>
cd <votre-repo>
pip install -r requirements.txt
```

## Lancement local

```bash
streamlit run app/streamlit_app.py
```

## Application deployee

**URL :** <!-- REMPLACEZ PAR VOTRE URL DE DEPLOIEMENT -->

## Repartition du travail

| Membre | Role | Contributions principales |
|--------|------|--------------------------|
| Prenom NOM | Data Engineer | ... |
| Prenom NOM | Data Scientist | ... |
| Prenom NOM | AI Engineer | ... |
| Prenom NOM | Frontend / DevOps | ... |

## Donnees

- **DVF** : telechargees depuis https://files.data.gouv.fr/geo-dvf/latest/csv/83/ le [DATE], filtre [PERIODE], [N] transactions apres dedoublonnage
- **Annonces** : collectees via [GumLoop / scraper Python] le [DATE]

## References

- Joel Grus, *Data Science From Scratch*, ch.5 (statistiques) et ch.14 (regression)
- Variance et covariance d'echantillon : division par n - 1
