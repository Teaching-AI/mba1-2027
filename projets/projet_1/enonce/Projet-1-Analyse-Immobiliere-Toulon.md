# Projet 1 : Observatoire du Marché Immobilier Toulonnais

**Kickoff 4 mars · suivi 8 et 10 mars · soutenance 12 mars 2027** · 5 jours de travail · groupes de 4

## Contexte

NidDouillet accompagne des jeunes couples primo-accédants a Toulon (budget max 450 000€). Jusqu'ici, leurs conseillers faisaient les recherches manuellement. Votre mission : **remplacer ce travail manuel par un outil en ligne, vivant, alimenté par des données réelles**.

Ceci n'est pas qu'un exercice : le produit doit être utilisable par les conseillers de NidDouillet dès le lendemain de la soutenance.

---

## Livrable Final

Une **application Streamlit deployée** (Streamlit Community Cloud ou équivalent) qui :

- Affiche l'état actuel du marché immobilier toulonnais a partir de données réelles
- Permet de filtrer les biens par critères (budget, surface, quartier, type)
- Montre les tendances : prix/m² par quartier, distribution des prix, opportunités
- Identifie les biens sous-evalués par rapport a la moyenne de leur quartier

---

## Contraintes Non-Négociables

- **Données réelles uniquement** : pas de CSV fabriqué. Donnees DVF + annonces collectées en vrai.
- **Application deployée** : une URL publique fonctionnelle le jour de la soutenance.
- **Algorithmes from scratch** : les fonctions statistiques et la régression de prix doivent être implementées sans sklearn (voir ci-dessous).
- **Git workflow** : chaque membre doit avoir des commits significatifs. Utiliser des branches et des pull requests.

---

## Collecte des Données

### Données DVF (obligatoire)

Les Demandes de Valeurs Foncières sont des données publiques sur les transactions immobilières depuis 2014.

**Téléchargement direct (recommandé) — DVF géocodées, département 83 (Var) :**

```
https://files.data.gouv.fr/geo-dvf/latest/csv/83/communes/83137.csv
```
`83137` = code INSEE de Toulon. Remplacer par d'autres codes pour les communes limitrophes
(La Seyne-sur-Mer : `83126`, Hyères : `83069`, La Garde : `83061`).

**Ou télécharger tout le département 83 d'un coup :**
```
https://files.data.gouv.fr/geo-dvf/latest/csv/83/
```

**Page du dataset :** https://www.data.gouv.fr/datasets/demandes-de-valeurs-foncieres-geolocalisees

- Filtrer sur les transactions des 2 à 3 dernières années (`date_mutation`)
- Filtrer sur `type_local` = Appartement ou Maison
- Viser minimum 500 transactions
- Enregistrer le résultat filtré dans `data/dvf_toulon.csv`

> **Piège DVF** : une vente de plusieurs lots apparaît sur plusieurs lignes avec la même
> `valeur_fonciere`. Sans dédoublonnage (`id_mutation`), le prix au m² est faux.

### Annonces Actuelles

**Option A - GumLoop** (recommande pour aller vite) :

Créer un workflow GumLoop qui :
1. Scrape SeLoger, PAP ou LeBonCoin automatiquement
2. Extrait les champs utiles (prix, surface, quartier, pièces, description)
3. Exporte vers un Google Sheet ou fichier JSON accessible depuis l'app
4. Peut être re-déclenché pour mettre a jour les données

**Option B - Scraper Python** :

```python
# Avec requests + BeautifulSoup ou playwright
# Viser 100+ annonces réelles a Toulon < 500 000€
# Sortie : data/annonces.csv avec au minimum les colonnes prix, surface
```

Quel que soit le choix, **documenter la méthode dans le README** et garder les données brutes versionnées (ou un lien stable vers la source).

---

## Analyse From Scratch

Cette partie est au coeur du projet. L'objectif est de comprendre les algorithmes en les implémentant, pas de savoir appeler une librairie.

**Assistants IA autorisés** (Copilot, Claude, ChatGPT...). En revanche, en soutenance,
**chaque membre** doit pouvoir expliquer et refaire à la main un calcul de sa partie
(voir « Question individuelle » plus bas). Du code que personne ne sait expliquer ne rapporte rien.

Si les formules vous font peur : [fiche de révision stats et régression](fiche-revision-stats-regression.md),
en français, avec des exemples toulonnais. 20 minutes de lecture.

**Reference : Joel Grus, "Data Science From Scratch"**

### Chapitre 5 - Statistiques

Implémenter dans `analysis/stats.py` :

```python
def mean(xs: list[float]) -> float: ...
def median(xs: list[float]) -> float: ...
def variance(xs: list[float]) -> float: ...
def standard_deviation(xs: list[float]) -> float: ...
def covariance(xs: list[float], ys: list[float]) -> float: ...
def correlation(xs: list[float], ys: list[float]) -> float: ...
```

Convention : **variance et covariance d'échantillon (division par n − 1)**, comme Grus.

Interdictions dans `analysis/stats.py` et `analysis/regression.py` : `numpy`, `pandas`, `scipy`, `statistics`, `sklearn`.
Pandas reste autorisé partout ailleurs (chargement des CSV, dashboard).
Ces fonctions doivent tourner sur des listes Python simples.

### Chapitre 14 - Régression Linéaire Simple

Implémenter dans `analysis/regression.py` :

```python
def predict(alpha: float, beta: float, x_i: float) -> float: ...
def error(alpha: float, beta: float, x_i: float, y_i: float) -> float: ...
def sum_of_sqerrors(alpha: float, beta: float, x: list, y: list) -> float: ...
def least_squares_fit(x: list[float], y: list[float]) -> tuple[float, float]: ...
def r_squared(alpha: float, beta: float, x: list, y: list) -> float: ...
```

Application concrète : prédire le prix au m² d'un bien à partir de sa surface, ou prédire
le prix à partir d'un score de quartier. Afficher le R² obtenu et l'interpréter.

### Chapitre 12 - k-NN (bonus)

Implémenter un "trouver des biens similaires" sans sklearn :

```python
def distance(v1: list[float], v2: list[float]) -> float: ...
def knn_similar(k: int, all_properties: list, target: dict) -> list: ...
```

---

## Enrichissement IA (recommande)

Utiliser Claude API ou OpenAI pour enrichir les annonces :

- Extraire des informations structurées depuis les descriptions textuelles
- Générer un résumé de chaque quartier
- Classifier chaque annonce : opportunité / prix de marché / surevalué

Cette étape peut etre intégrée dans le pipeline GumLoop ou exécutée en Python.

---

## Structure Suggerée du Projet

```
observatoire-toulon/
├── data/
│   ├── dvf_toulon.csv       # DVF filtré (lu par le CI)
│   └── annonces.csv         # Annonces collectées (lu par le CI)
├── collecte/
│   ├── collect.py           # Scraping ou intégration GumLoop
│   └── dvf.py               # Téléchargement et nettoyage DVF
├── analysis/
│   ├── stats.py            # Fonctions statistiques from scratch (Grus ch.5)
│   ├── regression.py       # Régression from scratch (Grus ch.14)
│   └── scoring.py          # Score d'opportunité par bien
├── app/
│   └── streamlit_app.py    # Dashboard principal
├── tests/
│   ├── test_stats.py
│   ├── test_regression.py
│   └── test_scoring.py
├── .github/
│   └── workflows/
│       └── ci.yml          # Tests automatiques à chaque push
├── requirements.txt
└── README.md
```

La répartition exacte est libre, mais la structure doit refléter une séparation claire
entre collecte, analyse et présentation.

---

## Collaboration et Git

Le README doit inclure une section **"Répartition du travail"** expliquant qui a fait quoi.
Le jury vérifiera le `git log` pour s'assurer que le travail est bien réparti.

Exemple de répartition possible (libre d'adapter) :

| Rôle | Responsabilité principale |
|------|--------------------------|
| Data Engineer | Pipeline de collecte, nettoyage DVF |
| Data Scientist | Stats et régression from scratch |
| AI Engineer | Enrichissement LLM, scoring |
| Frontend | Dashboard Streamlit, déploiement, CI |

Un membre = au moins une branche + au moins une PR mergée. Les groupes de 4 sont conservés pour P2.

---

## Évaluation — 100 points, note individuelle

| Volet | Pts | Détail |
|---|---|---|
| **Code — automatique** | 25 | 15 pts de tests publics (onglet *Actions* à chaque push) + 10 pts de tests cachés lancés par l'enseignant la veille de la soutenance |
| **Code — enseignant** | 25 | Voir ci-dessous |
| **Soutenance — groupe** | 30 | Voir ci-dessous |
| **Individuel** | 20 | Question individuelle (10) + contribution vérifiée dans git (10) |

Les tests cachés vérifient les mêmes fonctions sur d'autres cas (listes paires, corrélation
négative, vos propres données DVF...). Un code juste les passe sans effort ; un code écrit
pour faire passer les tests publics, non.

### Code — enseignant (25 pts)

| Critère | Pts | Ce qu'on regarde |
|---|---|---|
| Pipeline de collecte | 8 | Données réelles, méthode documentée et relançable, DVF dédoublonné |
| Score d'opportunité | 7 | Défini, justifié, cohérent avec la médiane du quartier |
| Application | 5 | Filtres qui marchent, visualisations lisibles, pas de crash |
| Qualité et tests | 5 | Découpage collecte / analyse / présentation, tests utiles (pas `assert True`) |

### Soutenance — groupe (30 pts)

| Critère | Pts | Ce qu'on évalue |
|---|---|---|
| Démo live | 10 | Le jury joue un conseiller NidDouillet et pose une vraie question métier |
| Architecture et choix techniques | 10 | Pourquoi ces outils, ces sources, ce découpage ? |
| Recul critique | 10 | Limites des données, R² obtenu et ce qu'il veut dire, ce que vous changeriez |

### Individuel (20 pts)

**Question individuelle (10 pts).** Chaque membre reçoit une question sur une partie du
projet **qu'il n'a pas forcément codée**. Exemples :
- « Voici 4 prix au m² : 2 800, 3 100, 3 400, 4 900. Calculez la médiane. Pourquoi est-elle plus utile que la moyenne ici ? »
- « Votre R² vaut 0,42. Qu'est-ce que ça veut dire pour un conseiller NidDouillet ? »
- « Montrez-moi dans le code où vous filtrez les maisons. »

**Contribution (10 pts).** Commits et PR de chaque membre sur `main`, relus par l'enseignant.
Un membre sans PR mergée a 0 sur cette ligne.

### Questions typiques du jury

- « Montrez-moi votre régression. Pourquoi les moindres carrés ? Que vous dit le R² ? »
- « Comment votre pipeline se met-il à jour ? Que se passe-t-il si le site change son HTML ? »
- « Votre corrélation entre surface et prix, elle est de combien ? C'est attendu ? »
- « Qu'est-ce qui vous a bloqués ? Comment avez-vous débloqué ? »
- « Avec 2 semaines de plus, que feriez-vous en premier ? »

---

## Calendrier et livrables

| Date | Séance | Attendu |
|---|---|---|
| 4 mars | Kickoff | Repo créé via GitHub Classroom, DVF chargé, premier push avec tests publics qui tournent |
| 8 mars | Suivi | Point d'étape : DVF nettoyé, premières fonctions stats vertes, qui fait quoi |
| 10 mars | Suivi | Démo intermédiaire : stats from scratch vertes, données réelles dans `data/`, app qui démarre en local |
| 12 mars | Soutenance | 20 min par groupe : 10 min de démo live + 10 min de questions (dont 4 questions individuelles) |

À rendre pour la soutenance :
- **Repo GitHub** via Classroom (pas de ZIP)
- **URL déployée** dans le README, fonctionnelle le jour J
- **README** : installation locale, architecture, répartition des rôles, source et date des données
