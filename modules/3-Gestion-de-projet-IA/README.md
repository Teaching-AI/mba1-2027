# Module 3 — Gestion de projet IA

**3 mars 2027**

## Objectifs

À la fin du module, l'étudiant sait :
- choisir entre Kanban, Scrum et cycle en V selon le projet, et le justifier ;
- écrire un backlog de user stories avec critères d'acceptation mesurables ;
- dire si un système IA tombe sous l'AI Act, et avec quelles obligations ;
- estimer le coût de fonctionnement d'une feature IA avant de la lancer.

## Supports

- [Slides — Gestion de projet IA (PDF)](class_material/Gestion%20de%20projet%20IA.pdf)
- [Slides — Gestion de projet et collaboration (PDF)](class_material/Module%203%20-%20Gestion%20de%20projet%20_%20collaboration.pptx.pdf)
- [Guide de démo — outils agiles](class_material/demo-guide-outils-agiles.md) *(enseignant, script live GitHub Projects)*
- [Comparatif outils agiles](class_material/comparatif-outils-agiles.md) *(étudiant, Jira vs GitHub vs Linear)*
- [Cas pratique — Immersion Cortaix](class_material/cas-cortaix.md) *(étudiant + guide d'animation)*

## Déroulé

1. **Méthodologies** — Kanban, Scrum, cycle en V, cycle en W. Comment choisir.
2. **Cycle de vie d'un projet IA** — cadre Confiance.AI, de la donnée au déploiement.
3. **Juridique** — RGPD, propriété intellectuelle, AI Act.
4. **Coût d'une feature IA** — tokens, GPU, CPU, latence : qui paie quoi.
5. **Cas Cortaix** — mise en situation.

## Mises à jour 2027 (à intégrer aux slides)

**AI Act : calendrier modifié.** Le règlement « Digital Omnibus » est entré en vigueur le
27 juillet 2026 et a repoussé une partie des échéances :

| Obligation | Date d'application |
|---|---|
| Transparence (art. 50) : dire à l'utilisateur qu'il parle à une IA | 2 août 2026 — **déjà en vigueur** |
| Marquage des contenus générés (systèmes déjà sur le marché avant le 2 août 2026) | 2 décembre 2026 |
| Systèmes à haut risque autonomes (annexe III) | 2 décembre 2027 |
| Systèmes à haut risque intégrés à un produit (annexe I) | 2 août 2028 |

**Exercice à faire sur NidBuyer** : le chatbot doit annoncer qu'il est une IA (art. 50, déjà
applicable). Et si un groupe ajoute un simulateur qui évalue la solvabilité d'un acheteur,
on entre dans l'annexe III (accès au crédit) : haut risque. Faire trouver ça aux étudiants.

**Coût d'une feature IA.** Point de départ : le même traitement ne coûte pas pareil selon
qu'il tourne sur une API, un GPU loué ou un CPU interne, et le GPU n'est pas toujours
gagnant sur de petits volumes. Faire estimer le coût mensuel de la fiche décision NidBuyer
(nombre d'annonces × appels × prix du token). Ce chiffre sera demandé par le jury en P2.

## Évaluation

[QCM](exercises/QCM-Gestion-Projet-IA.md) en fin de séance, non noté.

## Ressources

- [Scrum Guide](https://scrumguides.org/)
- [Texte de l'AI Act (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [CNIL — IA et RGPD](https://www.cnil.fr/fr/intelligence-artificielle)

---

[← Retour au sommaire](../../README.md)
