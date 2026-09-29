---
marp: true
theme: default
paginate: true
style: |
  section {
    font-family: 'Helvetica Neue', sans-serif;
    background: #0f0f0f;
    color: #f5f5f5;
  }
  h1 { color: #4ade80; font-size: 2em; }
  h2 { color: #4ade80; }
  strong { color: #4ade80; }
  table { font-size: 0.8em; }
  th { background: #1a1a1a; color: #4ade80; }
  td { background: #1a1a1a; }
  blockquote { border-left: 4px solid #4ade80; padding-left: 1em; color: #aaa; }
---

# P2 — NidBuyer
## L'acheteur IA qui travaille pour vous

*Toulon · 2027*

---

## Vous avez construit l'observatoire.

En une semaine, vos équipes ont :

- Collecté des milliers de **transactions DVF** sur Toulon
- Scrapé des **centaines d'annonces réelles**
- Calculé des **prix médians par quartier**
- Détecté des **biens sous-évalués**

Vous avez la mémoire du marché.

> Maintenant Antoine veut acheter à Toulon.
> Il a 40 minutes. Il a besoin d'une réponse, pas d'un tableau Excel.

---

## Quatre acheteurs. Un seul outil.

```
👤 "380k, T3-T4, calme, proche école."          → résidence principale
👤 "250k, je veux du rendement locatif."         → investisseur
👤 "Pied-à-terre vue mer, 200k max."             → résidence secondaire
👤 "Immeuble : j'habite en bas, je loue en haut."→ mixte
```

```
🤖 "Ce T3 au Mourillon, 3 100 €/m², soit 9% sous
    la médiane du quartier. Voici pourquoi c'est
    une opportunité — et voici ce qui m'inquiète."
```

**Pas un chatbot générique. Un acheteur IA ancré dans les données de Toulon.**

---

## Ce que les concurrents ne font pas

| | BienIci | MeilleursAgents | SeLoger | **NidBuyer** |
|---|---|---|---|---|
| Lister des biens | ✅ | ✅ | ✅ | ✅ |
| Estimer le prix | ❌ | ✅ vendeur | ❌ | ✅ **acheteur** |
| Détecter les sous-évaluations | ❌ | ❌ | ❌ | ✅ |
| Alerter sur profil | ❌ | ❌ | partiel | ✅ |
| Conseiller sur l'offre | ❌ | ❌ | ❌ | ✅ |

---

## Comment ça marche

```
Profil Antoine → Recherche sémantique (RAG)
                          ↓
               Biens les plus proches
                          ↓
         Prix vs médiane DVF du quartier
                          ↓
              LLM → Fiche décision argumentée
                          ↓
         "Faites une offre à 3 000 €/m² max"
```

Ce pipeline s'appelle **RAG** — Retrieval-Augmented Generation.
Vos données P1 **deviennent** le cerveau de NidBuyer.

---

## Vos 4 groupes

Les mêmes qu'en P1. Vous repartez de **vos** données et de **votre** observatoire.

Chaque groupe construit NidBuyer en entier, et le **déploie en ligne**.

**Même objectif. Quatre produits en compétition.**
Le jury vote pour celui qu'il utiliserait vraiment.

---

## Ce que vous allez apprendre

| Concept | Ce que c'est | Pourquoi ça compte |
|---------|-------------|-------------------|
| **RAG** | Donner de la mémoire à un LLM | Tout assistant IA en prod l'utilise |
| **Vector DB** | Chercher par sens, pas par mot-clé | Chroma, Pinecone, Weaviate |
| **Prompt engineering** | Contrôler ce que le LLM dit | La différence entre un bot raté et un produit |
| **FastAPI** | API Python production-ready | Standard industrie |
| **Déploiement + secrets** | Mettre un produit IA en ligne sans exposer ses clés | Une clé qui fuit se paie en quelques heures |

---

## D'ici le 26 avril

**3 choses. Pas plus.**

**1. Regarder (30 min)**
→ *"What is RAG?"* — IBM Technology sur YouTube

**2. Tester (1h)**
→ Créer une clé gratuite sur aistudio.google.com et refaire le TP 1 du module 2 avec 5 de vos annonces P1 : l'extraction est-elle juste ?
→ Noter ce qui rate : c'est votre premier jeu de test.

**3. Préparer (20 min)**
→ Relisez vos données P1. Combien d'annonces avec une vraie description ?
→ C'est votre matière première pour P2.

---

## La soutenance

**Le jury tire un profil acheteur au sort. En live.**

> Profil A — RP famille · Profil B — Investisseur
> Profil C — RS côtière · Profil D — Immeuble mixte

Vous avez 10 minutes de démo pour prouver que votre produit
répond mieux que 3h sur SeLoger — quel que soit le profil.

**Le jury vote pour le produit qu'il utiliserait vraiment.**

---

# On se retrouve le 26 avril.

*Construisez quelque chose dont un vrai acheteur aura besoin.*

---
