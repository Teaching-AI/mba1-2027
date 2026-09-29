# Comparatif des outils de gestion de projet Agile

## Pourquoi l'outil compte

La méthode Scrum ou Kanban n'existe que sur le papier sans outil pour la supporter.
Le choix de l'outil impacte directement la collaboration, la visibilité du projet et l'adoption par l'équipe.

---

## Outils de suivi de projet (task tracking)

### GitHub Projects
- **Éditeur :** GitHub (Microsoft)
- **Modèle :** Gratuit (inclus dans GitHub)
- **Type :** Kanban / Scrum léger, intégré au repo

**Forces :**
- Natif avec le code — une issue = une user story = potentiellement un commit/PR lié
- Zéro friction pour les équipes qui travaillent déjà sur GitHub
- Automatisations simples (quand une PR est mergée → issue passe en Done)
- Gratuit même pour les équipes

**Limites :**
- Moins adapté aux équipes larges (50+ personnes, 10+ projets)
- Reporting et métriques Scrum limités (pas de burndown chart natif)
- Peu adapté aux stakeholders non-techniques

**Usage typique :** équipes dev de 3–15 personnes, startups, projets open source

---

### Jira
- **Éditeur :** Atlassian
- **Modèle :** ~8–15 $/user/mois (gratuit jusqu'à 10 users)
- **Type :** Scrum + Kanban complet, hautement configurable

**Forces :**
- Standard de facto dans les ESN et grands comptes
- Scrum board complet : backlog, sprints, burndown chart, velocity
- Gestion fine des permissions, des workflows, des champs personnalisés
- Intégrations avec Confluence (documentation), Bitbucket, GitHub, Slack
- Reporting avancé (dashboards, métriques d'équipe)

**Limites :**
- Courbe d'apprentissage élevée
- Interface souvent critiquée (complexe, lente)
- Coûteux à grande échelle
- Sur-configurable → les équipes passent du temps à configurer plutôt qu'à produire

**Usage typique :** grandes équipes, projets multi-équipes, ESN, entreprises avec des processus formels

---

### Linear
- **Éditeur :** Linear (startup indépendante)
- **Modèle :** Gratuit (équipes < 250 issues) / ~8–16 $/user/mois
- **Type :** Scrum / Kanban, orienté vitesse et simplicité

**Forces :**
- Expérience utilisateur considérée comme la meilleure du marché
- Rapide — raccourcis clavier, interface fluide
- Cycles (= sprints) avec priorités claires
- Intégrations natives GitHub, GitLab, Figma, Slack, Notion
- Roadmap visuelle intégrée

**Limites :**
- Moins adopté dans les grands groupes / ESN (marché encore jeune)
- Moins de personnalisation que Jira pour les gros workflows
- Reporting moins puissant que Jira

**Usage typique :** startups tech, scale-ups, équipes produit modernes

---

### Trello
- **Éditeur :** Atlassian
- **Modèle :** Gratuit (fonctionnalités de base) / ~5$/user/mois
- **Type :** Kanban pur, très simple

**Forces :**
- Prise en main immédiate — 0 formation nécessaire
- Visuel, intuitif, drag & drop
- Adapté aux petites équipes et projets early-stage

**Limites :**
- Pas de sprint natif (Kanban uniquement)
- Pas de reporting, pas de burndown
- Limité dès que le projet grossit

**Usage typique :** side projects, petites équipes non-tech, gestion perso

---

## Tableau comparatif

| Critère | Trello | GitHub Projects | Linear | Jira |
|---|---|---|---|---|
| **Prix** | Freemium | Gratuit | Freemium | ~10$/user/mois |
| **Courbe d'apprentissage** | Très faible | Faible | Très faible | Élevée |
| **Intégration code** | Faible | Native (GitHub) | Bonne | Bonne |
| **Scrum complet** | Non | Partiel | Oui | Oui |
| **Kanban** | Oui | Oui | Oui | Oui |
| **Burndown chart** | Non | Non | Oui | Oui |
| **Multi-équipes** | Non | Limité | Bon | Excellent |
| **UX / Ergonomie** | Excellente | Correcte | Excellente | Critiquée |
| **Adoption grands comptes** | Faible | Moyenne | Faible | Très haute |
| **Adapté aux non-tech** | Oui | Non | Oui | Oui |

---

## Ce qu'on retrouve en entreprise

| Contexte | Outil souvent utilisé |
|---|---|
| Side project / équipe < 5 | Trello ou Notion |
| Startup early-stage | GitHub Projects ou Linear |
| Scale-up / PME tech | Linear ou Jira |
| ESN / cabinet de conseil | Jira |
| Grand compte (banque, industrie) | Jira + Confluence |
| Équipe dev dans une DSI | GitHub Projects |

---

## Les concepts communs à tous les outils

Peu importe l'outil, vous retrouverez toujours :

- **Backlog** → liste priorisée des fonctionnalités
- **Sprint / Cycle / Milestone** → itération de 2–4 semaines
- **Board** → visualisation Kanban (To Do / In Progress / Done)
- **Issue / Ticket** → unité de travail (user story, bug, tâche)
- **Assignee** → responsable de la tâche
- **Labels / Tags** → classification (feature, bug, documentation...)

> **Conclusion :** apprenez à maîtriser un outil, vous adapterez rapidement aux autres.
> Ce qui compte, c'est de comprendre le processus sous-jacent, pas l'interface.

---

## Outils de documentation

La gestion de projet ne s'arrête pas au suivi des tâches — la documentation est le deuxième pilier.

| Outil | Type | Prix | Usage typique |
|---|---|---|---|
| **Confluence** | Wiki d'équipe | ~5–10$/user/mois | Grands comptes, intégré à Jira |
| **Notion** | Tout-en-un (notes + BDD + projet) | Gratuit (solo) | Startups, équipes flexibles |
| **Markdown / Obsidian** | Fichiers texte versionnés | Gratuit | Équipes dev, documentation dans Git |
| **Google Docs** | Collaboratif simple | Gratuit | Tout contexte, stakeholders non-tech |

**Règle empirique :**
- Confluence si vous êtes déjà dans l'écosystème Atlassian (Jira)
- Notion si vous voulez un outil flexible sans budget
- Markdown dans le repo si vous voulez que la doc vive avec le code

---

## Outils de diagrammes

Indispensables pour documenter une architecture, un workflow, un parcours utilisateur.

| Outil | Prix | Points forts |
|---|---|---|
| **Excalidraw** | Gratuit | Schémas rapides façon tableau blanc, collaboratif |
| **Mermaid** | Gratuit | Diagrammes en code (dans Markdown/Notion/GitHub) |
| **draw.io** | Gratuit | Diagrammes formels (UML, flowcharts), export propre |
| **Figma** | Freemium | Maquettes UI, prototypage, collaboratif |

**Conseil :** Mermaid est particulièrement utile car les diagrammes vivent dans le repo Git — ils évoluent avec le code.
