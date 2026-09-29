# MBA1 IA & Transformation des organisations — 2027

Spécialisation Innovation IA, première année. Supports de cours, énoncés de projets et
templates d'évaluation automatisée. Groupes de 4.

**Fil rouge : NidDouillet**, agence immobilière toulonnaise qui accompagne des jeunes couples
primo-accédants (budget max 450 000 €). Les deux projets construisent le même produit :
un observatoire du marché, puis un acheteur IA déployé en ligne.

Calendrier détaillé : [CALENDRIER.md](CALENDRIER.md)

---

## Modules

| # | Date | Module | Ce qu'on en retient |
|---|---|---|---|
| M1 | 1er mars | [Fondamentaux de l'IA et du TAL](modules/1-Fondamentaux-IA-TAL/) | Du ML classique aux LLM multimodaux : ce qu'un modèle sait faire, et ce qu'il ne sait pas |
| M2 | 2 mars | [Prompt, contexte et évaluation](modules/2-Prompt-Engineering/) | Sorties structurées, RAG, agents, et surtout : mesurer la qualité d'un système LLM |
| M3 | 3 mars | [Gestion de projet IA](modules/3-Gestion-de-projet-IA/) | Agile appliqué à l'IA, AI Act, RGPD, coût réel d'une feature IA |

Le projet 0 (kickoff, formation des groupes, backlog P1) se déroule le 1er mars avec M1.

---

## Projets

Chaque projet dure 5 jours de travail, répartis sur 3 ou 4 journées en présentiel.
Les groupes de 4 restent les mêmes pour P1 et P2.

| Projet | Dates | Livrable |
|---|---|---|
| [P0 — Kickoff](projets/projet_0/) | 1er mars | Groupes, outils, backlog P1 (vidéo 3-5 min) |
| [P1 — Observatoire](projets/projet_1/) | 4 → 12 mars | Dashboard Streamlit déployé sur données réelles (DVF + annonces), stats et régression implémentées à la main |
| [P2 — NidBuyer](projets/projet_2/) | 26 → 30 avril | Acheteur IA déployé en ligne : RAG sur annonces réelles, scoring vs médiane DVF, fiche décision LLM, R&D vision sur photos |

---

## Évaluation

Même grille pour P1 et P2, sur 100 points. **La note est individuelle.**

| Volet | Pts | Comment |
|---|---|---|
| Code — automatique | 25 | Tests GitHub Actions à chaque push, dont des tests cachés lancés par l'enseignant |
| Code — enseignant | 25 | Architecture, lisibilité, choix justifiés, livrables écrits |
| Soutenance — groupe | 30 | Démo live face à un jury qui joue un vrai client, choix d'architecture, recul critique |
| Individuel | 20 | Question technique individuelle en soutenance (10) + contribution vérifiée dans le `git log` et les PR (10) |

Les 80 premiers points sont communs au groupe. Les 20 derniers sont propres à chaque étudiant.

Chaque groupe rend un repo GitHub via GitHub Classroom (pas de ZIP).
Voir [templates/SETUP_CLASSROOM.md](templates/SETUP_CLASSROOM.md).

---

## Organisation du repo

```
mba1-2027/
├── CALENDRIER.md
├── modules/
│   ├── 1-Fondamentaux-IA-TAL/
│   ├── 2-Prompt-Engineering/
│   └── 3-Gestion-de-projet-IA/
├── projets/
│   ├── projet_0/          # Kickoff
│   ├── projet_1/          # Observatoire
│   └── projet_2/          # NidBuyer
└── templates/             # Repos templates GitHub Classroom + scripts enseignant
    ├── projet-1-analyse-immobiliere/
    ├── projet-2-nidbot/
    └── SETUP_CLASSROOM.md
```

**Données étudiantes** : aucune note, aucun nom, aucun identifiant GitHub d'étudiant dans ce repo.
Les grilles remplies et les exports de notes restent hors de git (Drive école).
Le `.gitignore` bloque les `.csv` sous `projets/`.

---

Dernière mise à jour : septembre 2026 · la suite (MBA2) est dans le repo `mba-2027`
