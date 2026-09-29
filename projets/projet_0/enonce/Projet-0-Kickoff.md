# Projet 0 — Kickoff NidDouillet

**1er mars 2027, après-midi** · groupes de 4

## Le contexte

**NidDouillet** est une agence immobilière toulonnaise qui accompagne des jeunes couples primo-accédants (budget max 450 000€).

Aujourd'hui, leurs conseillers cherchent les biens manuellement : SeLoger, PAP, LeBonCoin, des tableurs Excel, des appels à des agents locaux. C'est lent, non-reproductible, et souvent trop tard — le bon bien est déjà parti.

Vous avez été mandatés pour transformer ça.

---

## Ce que vous allez construire

Le projet se déroule en deux temps, avec le même groupe du début à la fin :

**Projet 1 — L'Observatoire** (4 → 12 mars)
Un tableau de bord vivant alimenté par des données réelles : prix/m² par quartier, biens sous-évalués, tendances. Les conseillers NidDouillet l'utilisent dès le lendemain de votre soutenance.

**Projet 2 — NidBuyer** (26 → 30 avril)
Un acheteur IA déployé en ligne. Un couple décrit sa situation, NidBuyer cherche dans les vraies annonces, compare au marché et argumente : j'achète ou pas, à quel prix.

> Aujourd'hui : vous posez les fondations. Vous formez votre équipe, vous choisissez vos outils, et vous construisez le backlog du Projet 1.

---

## Déroulé de la séance (2h)

### Étape 1 — Formation des groupes (20 min)

**Groupes de 4 étudiants.** Ces groupes restent les mêmes pour P1 et P2 : choisissez bien.

Conseil : mélangez les profils. Un groupe de 4 profils business sans personne à l'aise avec le code, ou l'inverse, souffrira en P1.

Une fois le groupe formé, décidez d'un **nom de projet** (ce sera le nom de votre repo GitHub).

Répartissez les rôles — à titre indicatif, vous pouvez les faire évoluer :

| Rôle | Responsabilité principale sur P1 |
|---|---|
| **Data Engineer** | Pipeline de collecte DVF + scraping |
| **Data Scientist** | Statistiques et régression from scratch |
| **AI Engineer** | Enrichissement LLM, scoring des biens |
| **Frontend / DevOps** | Dashboard Streamlit, déploiement, CI |

> Un rôle ne veut pas dire travailler seul. Le pair programming est encouragé.

---

### Étape 2 — Choix des outils (20 min)

Chaque groupe choisit ses outils et les documente immédiatement. Ce choix sera présenté dans la vidéo.

**Suivi de projet** — choisissez un seul outil :

| Outil | Quand le choisir |
|---|---|
| GitHub Projects | Vous vivez dans GitHub, équipe technique |
| Linear | Vous voulez la meilleure UX sans overhead |
| Trello | Vous voulez démarrer en 5 minutes, Kanban simple |
| Jira | Vous voulez simuler un contexte grand compte |

**Versionning du code** — recommandé : **GitHub** (intégration CI/CD native, utilisé en entreprise).

**Documentation** — choisissez un outil :

| Outil | Quand le choisir |
|---|---|
| Notion | Flexible, gratuit, bon pour les équipes mixtes |
| Markdown dans le repo | Si tout le monde est à l'aise en dev |
| Google Docs | Si vous voulez démarrer vite sans friction |
| Confluence | Si vous utilisez Jira |

**Actions à faire maintenant :**
- Rejoindre l'assignment GitHub Classroom P0 (lien donné en séance) avec le nom du groupe
- Inviter tous les membres + l'enseignant
- Créer le board de suivi
- Créer l'espace de documentation

---

### Étape 3 — Construction du backlog P1 (45 min)

Lisez l'énoncé du Projet 1. Vous avez 45 minutes pour produire un **backlog de 6 à 10 user stories** priorisées.

**Format d'une user story :**
```
[US-XX] En tant que [qui], je veux [quoi] afin de [pourquoi].
Critères d'acceptation : [comment on sait que c'est fait ?]
Priorité : Must / Should / Could
```

**Pour vous aider à démarrer — grandes familles de tâches P1 :**

```
Collecte des données
  → DVF (données publiques transactions)
  → Scraping annonces actuelles

Analyse from scratch
  → Statistiques descriptives (mean, median, variance...)
  → Régression linéaire (prix ~ surface)

Application Streamlit
  → Affichage des données de base
  → Filtres (budget, surface, quartier, type)
  → Visualisations (prix/m² par quartier)
  → Détection des biens sous-évalués

Infrastructure
  → Tests unitaires (pytest)
  → CI/CD (GitHub Actions)
  → Déploiement (Streamlit Cloud)
```

Votre backlog doit répondre à : **"Si on a 1 semaine, dans quel ordre on fait quoi et pourquoi ?"**

---

### Étape 4 — Préparation de la restitution (35 min)

Préparez votre vidéo. Elle sera enregistrée et publiée sur la plateforme de votre choix (YouTube non-listé, Loom, Google Drive...) et le lien déposé dans votre repo GitHub (section README).

---

## Livrable — Vidéo de restitution

**Délai : 1 semaine**
**Durée : 3 à 5 minutes maximum**
**Format : vidéo enregistrée, lien dans le README du repo**

### Ce que la vidéo doit contenir

**1. Présentation de l'équipe** (30 sec)
- Prénom et rôle de chaque membre

**2. Vos choix d'outils** (1 min)
- Quel outil de suivi ? Pourquoi ce choix et pas un autre ?
- GitHub ? Autre plateforme ?
- Outil de documentation ?
- Montrez le board et le repo, même vides

**3. Votre backlog** (2 min)
- Listez vos user stories
- Expliquez votre ordre de priorité : qu'est-ce qui est Must / Should / Could ?
- Quelle est votre US n°1, et pourquoi commencer par là ?

**4. Répartition du travail** (30 sec)
- Qui s'occupe de quoi pour la semaine à venir ?

> La vidéo n'est pas évaluée sur la qualité de montage. Elle l'est sur la clarté des choix et la cohérence du backlog avec l'énoncé P1.

---

## Critères d'évaluation du Projet 0

| Critère | Ce qu'on regarde |
|---|---|
| **Repo GitHub créé et partagé** | Accessible, membres invités, README présent |
| **Board de suivi opérationnel** | Les US du backlog sont dans l'outil choisi |
| **Backlog cohérent** | 6–10 US, format correct, priorités justifiées |
| **Vidéo déposée dans les délais** | Lien dans le README, durée < 5 min |
| **Justification des choix d'outils** | Pas "on a pris Trello parce que c'est simple" — pourquoi c'est adapté à votre contexte |

---

## Ce que vous ne savez pas encore

À l'issue du Projet 1, vous aurez des données réelles sur le marché toulonnais.

Le Projet 2 utilisera ces données pour construire quelque chose que des vrais couples pourraient utiliser.

Vous ne construisez pas des exercices. Vous construisez des produits.
