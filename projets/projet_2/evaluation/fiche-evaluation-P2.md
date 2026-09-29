# Fiche d'évaluation — Projet 2 : NidBuyer

> ENSEIGNANT. Copier une fiche par groupe **hors du repo** (Drive école). Ne jamais commiter une fiche remplie.

| | |
|---|---|
| Groupe | |
| URL API / frontend | |
| Date | 30 avril 2027 |
| Profil tiré au sort | A · B · C · D |
| Évaluateur tech | |
| Jury acheteur | |

Format : 20 min = 10 min démo + 10 min questions (dont 4 individuelles).
Dépassement de la démo : −1 pt par minute au-delà de 11 min, sur la note de groupe.

---

## A. Code — automatique (/25)

| | Source | Score |
|---|---|---|
| Tests publics | `collect_scores.sh projet-2` | /15 |
| Tests cachés | `run_hidden_tests.sh projet-2 projets/projet_2/evaluation/test_caches_p2.py` | /10 |

## B. Code — enseignant (/25)

| Critère | Pts | Score | Note |
|---|---|---|---|
| Architecture : découpage, calculs hors prompt, aucun secret dans le code, tout LLM via `llm.py` | 8 | | |
| Données : ≥ 300 annonces, sources légales, médianes par quartier justifiées | 7 | | |
| R&D Vision : 30 biens annotés, précision mesurée, branchée au scoring | 5 | | |
| `EXPERIMENTS.md` : 3 versions mesurées, conclusion argumentée | 5 | | |

Vérifs rapides : `grep -rn "sk-\|api_key\|SUPABASE_KEY=" --include=*.py .` · `grep -rn "genai\|openai\|anthropic" backend/ | grep -v llm.py`

## C. Soutenance — groupe (/30)

| Critère | Pts | Score |
|---|---|---|
| Démo live sur le profil tiré au sort | 15 | |
| Choix techniques (embedding, DVF → quartier, cold start, coût mensuel) | 8 | |
| Recul critique (limites mesurées, ce qui manque pour un vrai produit) | 7 | |
| Pénalité de temps | − | |

## D. Individuel (/20 par étudiant)

Poser la question sur une partie que l'étudiant **n'a pas** codée (voir `contributions.sh projet-2`).

| Étudiant | Question posée | Question /10 | Contribution /10 | Total D |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |

Banque de questions :
- Pourquoi l'index ChromaDB est-il reconstruit au démarrage ? Que se passerait-il sinon ?
- Qui déclenche la synchro de 7h ? Pourquoi pas un planificateur dans l'API ?
- Montrer où l'écart à la médiane est calculé. Pourquoi pas par le LLM ?
- Comment est rattachée une vente DVF à un quartier ?
- Quelle précision pour la vision ? Sur combien de biens ? Qui a annoté ?
- Que contient `mention_ia` et pourquoi est-il obligatoire ?
- Combien coûte un appel `/rechercher` ? D'où vient ce chiffre ?

---

## Note finale par étudiant

**A + B + C + D = /100** · Bonus éventuels (+2 alerte live, +2 rendement locatif), plafonné à 100.
