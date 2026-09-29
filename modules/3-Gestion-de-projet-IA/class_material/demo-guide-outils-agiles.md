# Guide de démo — Outils Agiles en pratique
> **ENSEIGNANT — document interne**
> Durée estimée : 45–60 min | Prérequis : avoir un compte GitHub, un repo de démo prêt

---

## Objectif pédagogique
Montrer comment Scrum se concrétise dans les outils utilisés en entreprise.
Partir du concret (GitHub Projects) avant d'élargir à l'écosystème (Jira, Linear).

---

## PARTIE 1 — Démo live GitHub Projects (30 min)

### Préparation avant le cours (à faire la veille)
- Créer un repo GitHub public : `mba-demo-scrum`
- Activer **GitHub Projects** (onglet Projects sur le repo ou via github.com/users/TON_USERNAME/projects)
- Choisir le template **"Scrum"** ou **"Board"**

---

### Étape 1 — Créer le Product Backlog (5 min)

Montrer la création d'**Issues** = User Stories.

> **Script oral :**
> "Une Issue GitHub, c'est l'équivalent d'une User Story Scrum. Elle a un titre, une description, un responsable, des labels."

Créer en live 4-5 issues avec ce format :

| Titre de l'issue | Label | Priorité |
|---|---|---|
| `[US-01] En tant qu'utilisateur, je veux me connecter avec mon email` | `feature` | High |
| `[US-02] En tant qu'admin, je veux voir la liste des utilisateurs` | `feature` | Medium |
| `[US-03] Corriger le bug de déconnexion automatique` | `bug` | High |
| `[US-04] Ajouter la documentation API` | `documentation` | Low |
| `[US-05] Mettre en place les tests unitaires` | `testing` | Medium |

**Point clé à souligner :** le backlog est vivant, il évolue à chaque sprint.

---

### Étape 2 — Configurer le Board Kanban/Scrum (5 min)

Dans GitHub Projects, montrer les colonnes standard :

```
Backlog  →  Sprint actuel  →  In Progress  →  In Review  →  Done
```

> **Script oral :**
> "Ces colonnes correspondent aux états d'une tâche dans un sprint. Le WIP limit (limite du travail en cours) s'applique à 'In Progress' — en théorie, on ne commence pas quelque chose de nouveau si on a déjà trop en cours."

Montrer comment **déplacer une carte** d'une colonne à l'autre.

---

### Étape 3 — Sprint Planning (10 min)

Simuler un Sprint Planning avec les étudiants :

1. Afficher le backlog complet
2. Demander : "On a 2 semaines. Quelles issues on prend ?"
3. Glisser 3 issues dans la colonne **"Sprint actuel"**
4. Montrer comment assigner à un membre de l'équipe

> **Point pédagogique :**
> Le Product Owner priorise, l'équipe s'engage sur ce qu'elle PEUT livrer (pas ce que le PO VOUDRAIT).
> C'est la tension centrale de Scrum.

**Montrer les Milestones :**
Aller dans Issues > Milestones > New Milestone
Créer : `Sprint 1 — 4 mars au 12 mars`
Associer les issues du sprint à ce Milestone.

---

### Étape 4 — Daily Scrum simulé (5 min)

> **Script oral :**
> "Chaque matin, 15 min debout devant ce board. Trois questions :
> 1. Qu'est-ce que j'ai fait hier ?
> 2. Qu'est-ce que je fais aujourd'hui ?
> 3. Ai-je un blocage ?"

Montrer comment **créer une issue 'blocked'** avec un label rouge.
Montrer le filtre par assignee pour voir la charge de chaque personne.

---

### Étape 5 — Sprint Review / Retrospective (5 min)

> **Script oral :**
> "En fin de sprint, on regarde les issues Done vs celles qui n'ont pas été finies.
> En rétrospective : ce qui a bien marché / ce qui bloque / ce qu'on améliore."

Montrer comment **fermer les issues terminées** et **reporter les issues non finies** dans le sprint suivant.

---

### Points de discussion à lancer après la démo (5 min)

- "GitHub Projects est gratuit et intégré au code — c'est son principal avantage. Qu'est-ce qui pourrait manquer pour une grande équipe ?"
- "Comment vous imaginez qu'une équipe de 50 personnes sur 10 projets gère ça ?"
- → Transition naturelle vers Jira et la comparaison

---

## PARTIE 2 — Comparaison des outils (15 min)

Passer au document **`comparatif-outils-agiles.md`** (support étudiant).

> **Script oral :**
> "Maintenant qu'on a vu GitHub Projects en pratique, regardons où il se situe par rapport aux outils que vous croiserez en entreprise."

### Points à insister lors de la présentation du comparatif

**Sur Jira :**
- Standard de facto dans les grands comptes et les ESN
- Puissant mais complexe — une vraie courbe d'apprentissage
- Chez Cortaix (qu'on verra après), le standard est souvent Jira ou un outil similaire

**Sur GitHub Projects :**
- Idéal pour les équipes dev qui vivent dans GitHub
- Limite : moins adapté quand les stakeholders (PO, client) ne sont pas techniques

**Sur Linear :**
- Outil émergent, très apprécié dans les startups tech
- Expérience utilisateur nettement meilleure que Jira
- Intégration native avec GitHub, GitLab, Slack

### Question de clôture à poser aux étudiants
> "Si vous créiez votre startup demain avec 5 devs, quel outil vous choisiriez et pourquoi ?"

---

## Timing global de cette séquence

| Étape | Durée |
|---|---|
| Démo GitHub Projects | 30 min |
| Comparaison outils (support étudiant) | 15 min |
| Questions / discussion | 10 min |
| **Total** | **~55 min** |
