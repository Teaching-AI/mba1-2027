# Fiche d'évaluation — Projet 1 : Observatoire

> ENSEIGNANT. Copier une fiche par groupe **hors du repo** (Drive école). Ne jamais commiter une fiche remplie.

| | |
|---|---|
| Groupe | |
| Repo / URL app | |
| Date | 12 mars 2027 |
| Évaluateur tech | |
| Évaluateur PO (jury client) | |

Format : 20 min = 10 min démo + 10 min questions (dont 4 questions individuelles, ~1 min 30 chacune).
Dépassement de la démo : −1 pt par minute au-delà de 11 min, sur la note de groupe.

---

## A. Code — automatique (/25)

*Pré-rempli la veille.*

| | Source | Score |
|---|---|---|
| Tests publics | onglet Actions, dernier run sur `main` (`collect_scores.sh`) | /15 |
| Tests cachés | `run_hidden_tests.sh projet-1 projets/projet_1/evaluation/test_caches_p1.py` | /10 |
| **Total A** | | **/25** |

## B. Code — enseignant (/25)

*Pré-rempli la veille, en lisant le repo.*

| Critère | Pts | Score | Note |
|---|---|---|---|
| Pipeline de collecte : réel, documenté, relançable, DVF dédoublonné | 8 | | |
| Score d'opportunité : défini, justifié, cohérent avec la médiane | 7 | | |
| Application : filtres, visualisations, pas de crash | 5 | | |
| Qualité et tests : découpage, tests utiles | 5 | | |
| **Total B** | **25** | | |

## C. Soutenance — groupe (/30)

| Critère | Pts | Score | Qui |
|---|---|---|---|
| Démo live : question métier du jury traitée avec l'outil | 10 | | PO |
| Architecture et choix techniques | 10 | | Tech |
| Recul critique : données, R², limites, suite | 10 | | PO + Tech |
| Pénalité de temps | − | | |
| **Total C** | **30** | | |

Questions PO possibles :
- « J'ai un couple, 350 k€, deux enfants, proche école. Votre outil m'aide comment ? »
- « Quelle est la différence avec SeLoger ? »
- « Qu'est-ce que votre outil fait mal aujourd'hui ? »

## D. Individuel (/20 par étudiant)

Question individuelle : poser la question sur une partie que l'étudiant **n'a pas** codée
(vérifier avec `contributions.sh`). Barème : 0 = ne sait pas · 5 = confus · 8 = juste mais hésitant · 10 = clair.

Contribution git : 0 = aucune PR mergée · 5 = contributions mineures (README, CSV) · 10 = une partie du code porte clairement sa marque.

| Étudiant | Question posée | Question /10 | Contribution /10 | Total D /20 |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |

Banque de questions :
- Calculer à la main la médiane de 4 prix au m² donnés. Pourquoi la médiane plutôt que la moyenne ?
- Pourquoi la variance divise-t-elle par n − 1 ?
- Le R² vaut X : qu'est-ce que ça veut dire pour un conseiller ?
- Montrer dans le code le filtre maisons / appartements, ou le dédoublonnage DVF.
- Que se passe-t-il dans `correlation()` si toutes les surfaces sont identiques ?
- D'où viennent les annonces ? Comment les remettre à jour demain ?

---

## Note finale par étudiant

**A + B + C + D = /100** · Bonus éventuel (k-NN from scratch fonctionnel) : +2, plafonné à 100.
