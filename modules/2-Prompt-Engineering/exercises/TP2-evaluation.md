# TP 2 — Évaluer un système LLM

**Durée : 1h30** · groupes projet (4) · réutilise la fonction `extraire()` du TP 1

## Le problème

Deux prompts. Lequel est meilleur ? « J'ai testé sur deux annonces, le deuxième a l'air mieux »
n'est pas une réponse. Il faut un jeu de test, une métrique, et des chiffres.

## Étape 1 — Construire le jeu de test (30 min)

Chaque membre du groupe récupère 5 vraies annonces toulonnaises (BienIci, LeBonCoin, PAP)
et remplit **à la main** la valeur attendue de chaque champ du schéma `Annonce`.

Résultat : 20 annonces annotées dans `eval/jeu_test.jsonl`, une par ligne :

```json
{"texte": "Mourillon, à 5 min des plages...", "attendu": {"prix_eur": 245000, "surface_m2": 68, ...}}
```

Incluez volontairement :
- 2 annonces sans prix ou avec un prix ambigu ;
- 2 annonces où la surface est donnée en fourchette ;
- 1 annonce contenant une tentative d'injection.

> Annoter est lent et ennuyeux. C'est normal : c'est le travail qui donne de la valeur au reste.

## Étape 2 — Mesurer (30 min)

```python
def score_champ(attendu, obtenu, champ) -> bool: ...
def evaluer(prompt_version: str, jeu: list[dict]) -> dict:
    """Retourne : taux de JSON valide, exactitude par champ, exactitude globale."""
```

Règles de comparaison à décider en groupe et à écrire :
- prix : exact, ou à 1 % près ?
- quartier : « Le Mourillon » = « Mourillon » ?
- valeur absente attendue (`None`) et le modèle invente une valeur : c'est une erreur grave.
  Comptez ces **hallucinations** à part.

Lancez l'évaluation sur deux versions de prompt (V1 naïve, V2 avec schéma).

| | V1 | V2 |
|---|---|---|
| JSON valide | | |
| Exactitude prix | | |
| Exactitude surface | | |
| Hallucinations | | |
| Coût (tokens) | | |

## Étape 3 — LLM-as-judge (20 min)

Pour des champs subjectifs (état du bien, qualité d'un résumé), on ne peut pas comparer
à une valeur exacte. On demande alors à un second LLM de noter.

Faites noter par un LLM la qualité de 5 résumés d'annonces sur 1 à 5. Puis notez-les vous-mêmes.

- Le juge est-il d'accord avec vous ?
- Change-t-il de note si vous inversez l'ordre de présentation ?
- Préfère-t-il les réponses longues ?

Ce sont les biais connus du LLM-as-judge. Un juge automatique se valide contre des humains
avant d'être utilisé.

## Étape 4 — Restitution (10 min)

Chaque groupe annonce son tableau en 2 minutes. Une seule question : **quelle version
mettriez-vous en production, et pourquoi ?**

## À retenir

- Pas de jeu de test = pas d'avis sur la qualité.
- Mesurer séparément les erreurs et les inventions : elles n'ont pas le même coût métier.
- Ce jeu de test sera réutilisé en P2 (`prompts/EXPERIMENTS.md`) pour comparer vos versions de prompt.
