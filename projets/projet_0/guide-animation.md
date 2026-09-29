# Guide d'animation — Projet 0 (2h)
> **ENSEIGNANT — document interne**

---

## Objectif de la séance

Pas de code aujourd'hui. L'objectif est que chaque groupe reparte avec :
1. Un repo GitHub créé et partagé
2. Un board de suivi opérationnel avec leurs user stories dedans
3. Une compréhension réelle de P1 (pas juste "lu en diagonale")
4. Un plan clair pour la semaine

---

## Timing détaillé

| Heure | Étape | Notes |
|---|---|---|
| +0:00 | **Intro** — dévoiler le contexte NidDouillet | 5 min, garder le suspense sur P2 |
| +0:05 | **Teaser P1 & P2** — montrer les deux énoncés | Ne pas tout expliquer, laisser lire |
| +0:15 | **Formation des groupes** | Circuler, s'assurer que les groupes sont équilibrés |
| +0:35 | **Choix des outils** — chaque groupe décide | Passer dans les groupes, questionner les choix |
| +0:55 | **Lecture P1 + construction du backlog** | C'est le cœur — 45 min |
| +1:40 | **Préparation vidéo** | Certains groupes peuvent commencer à enregistrer |
| +1:55 | **Wrap-up** — rappel livrable, délai, format | 5 min |
| +2:00 | Fin |  |

---

## Introduction (5 min) — script

> "Vous allez passer les deux prochains mois à construire un produit, en deux étapes, pour une vraie agence immobilière. Pas des exercices, pas des démos, des produits. Aujourd'hui on pose les bases : équipes, outils, plan."

Afficher l'énoncé P0. Ne pas encore distribuer P1 et P2 — les révéler progressivement pendant la présentation du contexte NidDouillet.

**Révélation progressive :**
- D'abord le contexte NidDouillet (conseillers, couples, 450k€, travail manuel)
- Puis "voilà ce que vous allez construire" → afficher P1
- Puis "et c'est seulement la première partie" → afficher P2 rapidement, sans entrer dans les détails
- Insister : les groupes de 4 sont fixes jusqu'à fin avril. Équilibrer les profils (au moins une personne à l'aise en Python par groupe)

---

## Formation des groupes (20 min)

Laisser les étudiants se former librement, mais intervenir si :
- Un groupe fait 5+ personnes → scinder
- Un groupe fait 2 personnes → encourager à fusionner

**Questions à poser pour aider à la répartition des rôles :**
- "Qui est à l'aise avec Python ?"
- "Qui a déjà fait du web / du déploiement ?"
- "Qui aime plutôt les données ou plutôt les interfaces ?"

Les rôles sont indicatifs — l'important c'est que chaque membre sache ce qu'il fait semaine 1.

---

## Choix des outils (20 min)

Passer dans les groupes et questionner les choix. Ne pas valider passivement.

**Questions à poser :**
- "Pourquoi Trello et pas Linear ?" → forcer une vraie justification
- "Vous avez déjà utilisé GitHub Projects ?" → si non, c'est l'occasion
- "Votre Notion, qui va l'alimenter ?" → pointer le risque de documentation qui se vide en semaine 2

**Erreurs courantes à anticiper :**
- Groupe qui choisit Jira sans jamais l'avoir utilisé → potentiellement 1h de configuration perdue
- Groupe qui choisit 2 outils de documentation → simplifier
- Repo GitHub créé mais pas partagé avec l'enseignant → vérifier avant la fin

**Objectif à la fin de cette étape :**
Chaque groupe a un repo GitHub avec un README, un board visible, un espace de doc.
Vérifier en passant dans les groupes.

---

## Construction du backlog (45 min)

C'est l'étape la plus importante. Beaucoup de groupes vont survoler P1 — les forcer à rentrer dans le détail.

**Questions à poser pour débloquer :**
- "C'est quoi votre US numéro 1 ? Pourquoi pas les stats d'abord ?"
- "Comment vous savez que la collecte DVF est terminée ? Quel est votre critère d'acceptation ?"
- "Si vous n'avez que 3 jours et pas 7, vous gardez quelles US ?"

**Signe que le backlog est trop vague :**
- US du type "Faire le dashboard" sans critère d'acceptation
- Aucune US sur la collecte des données (oubli fréquent)
- Tout est marqué "Must" → demander de re-prioriser

**Signe que le backlog est bien fait :**
- L'US numéro 1 est la collecte des données (on ne peut rien faire sans data)
- Les US techniques (CI/CD, tests) sont en Should ou Could
- Chaque US a un responsable désigné

**Backlog minimum viable pour P1 (pour référence) :**

```
[US-01] Collecter les données DVF (dept. 83, 2 dernières années) — Must
[US-02] Scraper 100+ annonces réelles à Toulon — Must
[US-03] Implémenter mean, median, variance, correlation from scratch — Must
[US-04] Implémenter la régression linéaire from scratch — Must
[US-05] Dashboard Streamlit : affichage brut des données — Must
[US-06] Filtres : budget, surface, quartier, type — Must
[US-07] Visualisation prix/m² par quartier — Should
[US-08] Détection des biens sous-évalués — Should
[US-09] Tests unitaires sur les algos from scratch — Should
[US-10] Déploiement Streamlit Cloud + CI GitHub Actions — Could
```

---

## Préparation vidéo (35 min)

La vidéo se tourne cette semaine, pas forcément dans la séance. Mais certains groupes avancés peuvent commencer.

**Rappeler le format :**
- 3 à 5 min maximum (au-delà = malus implicite sur la clarté)
- Loom ou YouTube non-listé → lien dans le README
- Pas besoin de montage, une seule prise suffit

**Ce qu'on évalue dans la vidéo :**
- Est-ce qu'ils ont compris P1 ? (visible dans la justification du backlog)
- Est-ce que les choix d'outils sont argumentés ? (pas juste "on aime bien")
- Est-ce que la répartition est crédible ? (chaque membre parle de son rôle)

---

## Wrap-up (5 min)

Rappeler :
- **Délai :** 1 semaine
- **Livrable :** lien vidéo dans le README du repo GitHub
- **Partage :** repo partagé avec l'enseignant avant la fin de séance

Annoncer que la semaine suivante commence directement sur P1 — pas de rappel de l'énoncé, on suppose qu'ils ont lu.

---

## Ce qu'il faut vérifier avant de quitter la salle

- [ ] Chaque groupe a un repo GitHub nommé et partagé
- [ ] Le board de suivi est créé et contient au moins quelques US
- [ ] Les rôles sont définis (même provisoirement)
- [ ] Chaque groupe sait comment déposer le lien vidéo
