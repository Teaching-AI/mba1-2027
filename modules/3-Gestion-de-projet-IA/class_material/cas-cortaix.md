# Cas pratique — Immersion dans une ESN
## Comment une ESN data mature gère ses projets IA

---

> **NOTE ENSEIGNANT** — sections marquées `[PROF]` sont des indications d'animation, non destinées aux étudiants.
> Durée estimée : 60–75 min (présentation + discussion + exercice)

---

## Introduction

Note sur la derniere ESN spécialisée en IA que j'ai visité. Ce document présente les pratiques observées lors d'une immersion, et les compare aux méthodes vues en cours.

L'objectif : comprendre comment les méthodes Scrum, les outils et les pratiques engineering se combinent dans une équipe data mature en 2025.

---

## 1. L'équipe type chez ESN

Un projet IA est porté par une équipe pluridisciplinaire avec des rôles clairement définis :

| Rôle | Responsabilité principale |
|---|---|
| **Solution Architect** | Choix d'infrastructure, arbitrage technique vs contraintes client |
| **Tech Lead** | Qualité du code, standards, décisions d'architecture équipe |
| **Data Scientist (×2)** | Modélisation, expérimentation, pair programming |
| **Data Engineer** | Pipelines de données, ingestion, qualité |
| **MLOps** | Plateforme d'entraînement des modèles, déploiement |
| **Product Owner** | Exigences métier, ROI — souvent issu de la business unit cliente |
| **Scrum Master / AIDM** | Animation des rituels agiles |
| **UX** | Intégré selon la centralité de l'interface |

> **[PROF] — Point à souligner :**
> Le PO vient de la business unit cliente. C'est une bonne pratique car il connaît le métier.
> Demander aux étudiants : "Quel problème ça pose quand le PO ne connaît pas le métier ?"

---

## 2. Le cycle de vie d'un projet — les Gates

ESN utilise un processus en entonnoir avec des **points de décision (gates)** avant de lancer un sprint.

```
Discussions business initiales
           ↓
        [GATE 1]
           ↓
     FRAMING  (2–3 semaines)
     Questions clés :
     → Est-ce un bon candidat pour l'IA ?
     → Y a-t-il un budget identifié ?
     → Le besoin est-il clairement défini ?
           ↓
        [GATE 2]
           ↓
     SCOPING  (~1 mois)
     → Tous les acteurs réunis
     → Agenda jour par jour
     → Périmètre précis
     → Go / No-go final
           ↓
     SPRINTS  (~3 mois)
     → Cycles de ~3 semaines
     → Livraisons itératives
```

### Pourquoi les gates sont essentiels

Beaucoup d'entreprises sautent la phase de Framing et lancent des projets ML qui n'auraient jamais dû l'être. Résultats typiques :
- Données inexistantes ou inaccessibles
- Problème résolvable avec une simple règle métier (pas besoin de ML)
- Pas de budget pour le déploiement

> **[PROF] — Question de discussion :**
> "Quels critères permettent de dire qu'un projet est 'un bon candidat IA' ?"
> Réponses attendues : volume de données suffisant, pattern non-trivial, coût de l'erreur acceptable, ROI identifié.

---

## 3. L'infrastructure technique

### Gestion des données sensibles

ESN distingue deux environnements selon la sensibilité des données :

| Environnement | Usage |
|---|---|
| **Azure (cloud public)** | Données mock, open source, non sensibles |
| **RTDP / TDP / TRC (on-premise)** | Données propriétaires clients sensibles |

Cette architecture est courante dans les secteurs défense, aéronautique, industrie lourde : les données ne peuvent pas partir sur le cloud public.

### Outils MLOps

- **ArgoWorkflow** — orchestrateur de workflows sur Kubernetes. Permet de chaîner des étapes de traitement/entraînement sous forme de pipelines déclaratifs en YAML.
- **Metaflow** (créé par Netflix) — framework Python pour gérer le cycle de vie des projets ML. Gère le versioning des runs, la gestion des données, le déploiement.

### Architecture applicative

Ils travaillent en **architecture hexagonale** (ports and adapters) :
- Le cœur métier (logique IA/ML) ne dépend pas des détails techniques (BDD, API, interface)
- Code plus testable et maintenable
- Signal de maturité : rare dans les équipes data

---

## 4. Cas concret — L'assistant maintenance corrective

### Contexte
Un **asset** (outil développé une fois, réutilisable sur plusieurs clients) pour aider les techniciens à retrouver des informations dans des documents de maintenance.

Architecture technique : **RAG** (Retrieval-Augmented Generation)

```
Documents de maintenance  →  Ingestion  →  Index vectoriel  →  Retrieval  →  Réponse LLM
```

### Le problème d'ingestion

La complexité vient de la combinatoire :
```
N clients × N systèmes × N formats de documents = N configurations différentes
```

### La solution : généricité par configuration YAML

Évolution en 3 étapes de l'architecture d'ingestion :

```
Étape 1 : 1 config dans Git par client (fragile, peu maintenable)
     ↓
Étape 2 : 1 fichier de config par stage de traitement (meilleure séparation)
     ↓
Étape 3 : 1 seul stage + 1 config YAML universelle (objectif)
```

**Résultat visé :** ajouter un nouveau client = modifier un fichier YAML, sans toucher au code.

> **[PROF] — Parallèle avec le cours :**
> Ce problème illustre un principe fondamental en engineering : séparer le **code** (logique) de la **configuration** (données). C'est ce que Scrum appelle "réduire la dette technique" dans le backlog.

---

## 5. Pratiques de développement

### TDD (Test-Driven Development)
L'équipe vise **80% de couverture de tests unitaires**.
- Écrire le test avant le code
- Rare dans les équipes data — signe de maturité engineering

### Pair Programming
Data Scientist + Dev sur le même code en temps réel.
Accélère la montée en compétence, réduit les erreurs.

### Code typé
Tout le Python est typé (annotations). Exemple :
```python
def process_document(doc: Document, config: DocumentConfig) -> list[str]:
    ...
```

### Pull Requests — Ship / Show / Ask

| Mode | Quand l'utiliser |
|---|---|
| **Ship** | Merger directement (changements mineurs, évidents) |
| **Show** | Merger mais informer l'équipe (pour visibilité) |
| **Ask** | Demander une review avant de merger (changements significatifs) |

### ADR — Architecture Decision Records
Documents courts dans le repo Git qui expliquent **pourquoi** une décision technique a été prise.
Exemple : "Pourquoi on utilise Pydantic plutôt que dataclasses"
→ Traçabilité des décisions dans le temps.

---

## 6. Rituels d'amélioration continue

### Kaizen (tous les 3 mois — 3 jours)
Le Kaizen (改善) est un événement trimestriel dédié à l'amélioration des pratiques.
- ~12 jours/an dédiés à ne pas produire, mais à s'améliorer
- Les sujets sont des pain points identifiés en amont
- Un Kaizen Ambassador suit les KPIs d'amélioration

Sujets actuels en cours de Kaizen chez ESN :
1. Mesurer la valeur opérationnelle d'un produit
2. Détecter les régressions software
3. Standardiser la documentation dev
4. Capitaliser les connaissances entre équipes

### Community meetings (1 fois par sprint)
Veille scientifique et technologique :
- Partage de papers et d'outils entre data scientists, ML engineers, data engineers
- Exemples vus : Docling (IBM), évaluation de modèles par bootstrapping, energy-based transformers

### Lunch & Learn
Présentations courtes sur des sujets transverses.
Exemple : framework **EROM** pour l'optimisation énergétique du code (green IT).

### GitLab organisé en groupes
```
GitLab commun
├── Use cases & Assets       ← projets en cours
└── Gold Standards           ← starter kits issus des Kaizens
```
Les **starter kits** (Gold Standards) sont générés lors des Kaizens et deviennent les templates de référence.

---

## 7. Les trois axes d'évaluation

Chez ESN, les collaborateurs sont évalués sur :

| Axe | Ce que ça signifie concrètement |
|---|---|
| **Delivery** | Tu livres ce que tu t'es engagé à livrer |
| **Team-player** | Tu aides les autres, tu partages tes connaissances |
| **Humilité** | Tu sais ce que tu ne sais pas, tu acceptes le feedback |

> **[PROF] — Question de clôture :**
> "Ces trois axes sont-ils spécifiques à une ESN IA, ou est-ce universel ? Qu'est-ce qui changerait dans une entreprise moins mature ?"

---

## Exercice de synthèse (20 min)

### Mise en situation

Vous êtes recrutés chez ESN. Un client dans l'industrie aéronautique veut un **système de classification automatique des rapports d'incident**.

En groupe, définissez :

**1. Le cycle du projet** (5 min)
- Quelles questions poser lors du Framing ?
- Quels acteurs inviter au Scoping ?
- Quel est votre critère de Go / No-go ?

**2. L'équipe** (5 min)
- Quels rôles sont indispensables pour ce projet ?
- Qui est le Product Owner idéal ?

**3. Le premier sprint** (10 min)
- Écrivez 5 user stories pour le backlog
- Priorisez-les
- Lesquelles mettez-vous dans le Sprint 1 ?

**Restitution :** chaque groupe présente son Sprint 1 backlog (2 min par groupe).

---

## Points clés à retenir

1. **Les gates évitent les projets IA qui n'auraient pas dû l'être** — le Framing est une étape non-négociable
2. **La généricité par configuration** (YAML) est un objectif d'architecture central dans les projets ML à plusieurs clients
3. **Le Kaizen** traduit l'amélioration continue Scrum en pratique réelle : temps dédié, KPIs, ownership
4. **Delivery + Team-player + Humilité** — les soft skills comptent autant que les hard skills dans les équipes matures
