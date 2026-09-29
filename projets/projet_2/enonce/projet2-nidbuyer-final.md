# Projet 2 — NidBuyer
### Votre acheteur IA à Toulon, déployé en ligne

**Kickoff 26 avril · suivi 28 avril · soutenance 30 avril 2027**
5 jours de travail · groupes de 4 (les mêmes qu'en P1)

---

## Le problème

BienIci liste. MeilleursAgents estime pour les vendeurs. SeLoger affiche.

Personne ne répond à la vraie question de l'acheteur :

> *« Est-ce que j'achète ce bien, à ce prix, maintenant, pour mon profil ? »*

| | BienIci | MeilleursAgents | SeLoger | NidBuyer |
|---|:---:|:---:|:---:|:---:|
| Lister des biens | ✅ | ✅ | ✅ | ✅ |
| Estimer le prix | ❌ | ✅ vendeur | ❌ | ✅ acheteur |
| Détecter les sous-évaluations | ❌ | ❌ | ❌ | ✅ |
| Alerter selon un profil | ❌ | ❌ | partiel | ✅ |
| Analyser les photos | ❌ | ❌ | ❌ | ✅ |
| Conseiller sur l'offre | ❌ | ❌ | ❌ | ✅ |

---

## Quatre profils, un seul outil

| Profil | Requête type |
|---|---|
| 🏠 Résidence principale | *« 380 k€, T3-T4, calme, proche école. »* |
| 📈 Investissement | *« 250 k€, je veux du rendement locatif. »* |
| 🌊 Résidence secondaire | *« Pied-à-terre vue mer, 200 k€ max. »* |
| 🏢 Immeuble mixte | *« J'habite en bas, je loue les autres. »* |

**Réponse attendue :**
> *« Ce T3 au Mourillon est à 3 100 €/m², soit 9 % sous la médiane DVF du quartier.
> Voici l'opportunité, voici les risques, voici le conseil de négociation. »*

---

## Ce qui est imposé

1. **Déploiement en ligne** : API et frontend accessibles par URL (Hugging Face Spaces recommandé, voir le README du template). Aucune clé dans le code.
2. **LLM Gemini (clé AI Studio), uniquement via `backend/llm.py`** (fourni). Aucun appel direct à une API LLM ailleurs dans le code.
3. **Les calculs en Python, la rédaction au LLM.** Prix au m², écart à la médiane, rendement : calculés et testés. Le LLM ne fait jamais d'arithmétique.
4. **Supabase = source de vérité** des annonces. ChromaDB = index reconstruit au démarrage.
5. **Transparence (AI Act, art. 50, en vigueur depuis août 2026)** : l'utilisateur voit qu'il parle à une IA. Chaque réponse LLM de l'API porte le champ `mention_ia`.
6. **Sources légales.** Pas de Facebook (conditions d'utilisation, données personnelles). Vérifier les conditions de chaque site scrapé ; en cas de doute, demander.
7. **300 annonces minimum** dans la base le jour de la soutenance.

---

## Organisation interne (groupe de 4)

| Périmètre | Contenu |
|---|---|
| Lead architecture + déploiement | Hébergement, secrets, synchro planifiée, `/admin/*` |
| RAG + ingestion | Supabase, ChromaDB, sources, dédoublonnage |
| Scoring + marché + prompts | Médianes DVF par quartier, score, fiche décision, `EXPERIMENTS.md` |
| R&D Vision + frontend | État du bien par les photos, interface Streamlit |

Le découpage est indicatif. Ce qui ne l'est pas : **chaque membre ouvre et fait merger des PR**,
et **chaque membre peut expliquer n'importe quelle partie** (question individuelle en soutenance).

---

## Architecture

```
GitHub Actions (7h00) ──POST /admin/sync──▶ API FastAPI (hébergée) ──▶ Gemini
                                                 │
Sources (BienIci, agences...) ─────────────────▶ │ ── Supabase (annonces, source de vérité)
                                                 │ ── ChromaDB (index local, reconstruit)
Frontend Streamlit (hébergé) ──HTTP────────────▶ │
```

Tout est détaillé dans le README du template. Points durs à anticiper :

- **Le DVF ne contient pas de quartier.** Il faut rattacher chaque vente à un quartier
  (IRIS INSEE via les coordonnées, ou table section cadastrale → quartier). Voir `backend/marche.py`.
- **Le disque de l'hébergement est effacé** à chaque redémarrage : rien d'important en fichier local.
- **Pas de planificateur interne** : le service dort sans trafic. C'est un workflow GitHub Actions planifié qui réveille `/admin/sync`, protégé par un jeton.

---

## Fiche décision : les chiffres d'abord

```python
prix_m2 = bien["prix"] / bien["surface"]
mediane = mediane_quartier(bien["quartier"])
ecart   = (prix_m2 - mediane) / mediane * 100
fiche   = fiche_decision(bien, {"mediane_prix_m2": mediane})   # texte factuel, calculé en Python
analyse = generer(prompt_avec(fiche, description, profil))       # le LLM rédige
```

Le LLM produit : **opportunité · points forts · points d'attention · recommandation**.

---

## Prompt engineering : 3 versions, mesurées

Reprenez le **jeu de test du module 2** (20 annonces annotées par le groupe) et comparez 3 versions
du prompt de fiche décision :

| Version | Approche |
|---|---|
| V1 | Prompt basique : point de départ à battre |
| V2 | Sortie structurée (schéma Pydantic) : sections fixes |
| V3 | Raisonnement guidé : le modèle relit la fiche chiffrée avant de conclure |

Pour chaque version : taux de sortie valide, chiffres recopiés sans erreur, hallucinations,
latence, coût en tokens (visible dans `/admin/status`). Tout dans `prompts/EXPERIMENTS.md`.

---

## R&D Vision : estimer les travaux par les photos

```python
evaluer_etat_bien(photos) → {
    "etat_general":       "excellent" | "bon" | "correct" | "a_renover",
    "travaux_detectes":   ["peinture", "cuisine", ...],
    "estimation_travaux": "0-5k" | "5-20k" | "20-50k" | ">50k",
    "luminosite":         1-5,
    "score_presentation": 1-10
}
```

Deux pistes : **LLM multimodal** (Gemini via `llm.generer(..., images=...)`, rapide à brancher)
ou **CNN** (plus long, demande des photos annotées : 50 par classe minimum).

Obligatoire dans les deux cas : **annoter vous-mêmes 30 biens** et mesurer la précision
de votre approche sur ces 30 biens. Un chiffre honnête, même bas, vaut plus qu'une démo choisie.

Impact sur le score, selon le profil :

| Profil | Travaux |
|---|---|
| Investisseur | Marge de négociation : pas de malus |
| Résidence principale famille | Contrainte : malus fort |

---

## Évaluation — 100 points, note individuelle

| Volet | Pts | Détail |
|---|---|---|
| **Code — automatique** | 25 | 15 pts de tests publics (onglet *Actions*) + 10 pts de tests cachés lancés la veille de la soutenance |
| **Code — enseignant** | 25 | Voir ci-dessous |
| **Soutenance — groupe** | 30 | Voir ci-dessous |
| **Individuel** | 20 | Question individuelle (10) + contribution vérifiée dans git (10) |

Les contrats testés sont écrits dans les docstrings de `scoring.py`, `rag.py` et `main.py`.
Les tests cachés vérifient **les mêmes contrats** sur d'autres cas. Lisez les docstrings.

### Code — enseignant (25 pts)

| Critère | Pts |
|---|---|
| Architecture et lisibilité : découpage, pas de calcul dans les prompts, pas de secret dans le code | 8 |
| Données : ≥ 300 annonces, sources légales, médianes par quartier justifiées | 7 |
| R&D Vision : 30 biens annotés, précision mesurée, intégration au scoring | 5 |
| `EXPERIMENTS.md` : 3 versions mesurées sur le jeu de test, conclusion argumentée | 5 |

### Soutenance — groupe (30 pts)

| Critère | Pts | Ce qu'on évalue |
|---|---|---|
| Démo live | 15 | Le jury tire un profil acheteur au sort et pose ses vraies questions |
| Choix techniques | 8 | Embedding, rattachement DVF → quartier, mise en veille de l'hébergement, coût mensuel estimé |
| Recul critique | 7 | Limites mesurées (vision, RAG, hallucinations), ce qui manque pour un vrai produit |

> **Bonus** (plafonné à 100) : alerte e-mail ou Slack reçue en direct pendant la démo **+2** · module rendement locatif **+2**

---

## Soutenance : scénarios live

20 min par groupe : 10 min de démo sur profil tiré au sort + 10 min de questions (dont 4 individuelles).

| Profil | Requête |
|---|---|
| A — RP famille | *« 380 k€, T3-T4, calme, proche école. »* |
| B — Investisseur | *« 250 k€ max, rendement locatif, appartement ou petit immeuble. »* |
| C — RS côtière | *« 200 k€, vue ou proche mer, peu importe la taille. »* |
| D — Mixte | *« Immeuble : j'habite en bas, je loue les autres. »* |

Questions typiques :
- *« Ce bien à 3 200 €/m², c'est une bonne affaire pour mon profil ? D'où vient la médiane ? »*
- *« Vous avez combien d'annonces ? D'où viennent-elles ? C'est légal ? »*
- *« Si un bien correspond à mon profil demain matin, je reçois quoi, et qui déclenche l'envoi ? »*
- *« Combien coûte NidBuyer par mois pour 2 000 annonces et 100 utilisateurs ? »*

---

## Calendrier et livrables

| Date | Séance | Attendu à la fin de la journée |
|---|---|---|
| 26 avril | Kickoff | Repo Classroom, annonces P1 dans Supabase, API déployée en ligne (même vide), rôles dans le README |
| 28 avril | Suivi et go/no-go | `/rechercher` fonctionne sur l'URL déployée, première mesure vision. Gel des fonctionnalités à la fin de la journée : ensuite, on corrige, on n'ajoute plus |
| 30 avril | Soutenance | Démo live et questions |

| # | Livrable | Exigence |
|:---:|---|---|
| 1 | Repo GitHub (Classroom) | Pas de ZIP |
| 2 | URLs déployées | API et frontend fonctionnels le jour J, dans le README |
| 3 | `README.md` | Architecture, rôles, nombre d'annonces, choix justifiés |
| 4 | `prompts/EXPERIMENTS.md` | 3 versions mesurées |
| 5 | `vision/APPROACH.md` | Approche, précision sur 30 biens annotés, limites |

---

*Une semaine. Un vrai produit. Le jury joue un vrai acheteur : il vote pour le produit qu'il utiliserait.*
