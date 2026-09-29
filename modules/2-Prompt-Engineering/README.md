# Module 2 — Prompt, contexte et évaluation

**2 mars 2027**

Le prompt engineering seul ne suffit plus. Ce qui compte en production :
ce qu'on met dans le contexte du modèle, le format de ce qu'il rend, et comment on mesure
s'il a raison. Un Product Owner IA qui ne sait pas mesurer ne peut pas arbitrer.

## Objectifs

À la fin du module, l'étudiant sait :
- écrire un prompt structuré (rôle, contexte, consignes, format, exemples) ;
- obtenir une sortie JSON exploitable par du code, et gérer les cas où elle ne l'est pas ;
- expliquer le RAG et quand il est préférable au fine-tuning ;
- construire un petit jeu d'évaluation et comparer deux versions de prompt sur des chiffres.

## Supports

- [Slides (PDF)](class_material/Prompt%20engineering.pdf)
- [Version texte des slides](class_material/Prompt-engineering.txt)

## Déroulé

1. **Fondamentaux** — anatomie d'un prompt, température, zero-shot, few-shot.
2. **Techniques de raisonnement** — chain-of-thought, prompt chaining, self-consistency, tree of thoughts.
3. **Contexte** — RAG, taille de contexte, ce qu'on met dedans et ce qu'on laisse dehors.
4. **Sorties structurées** — JSON, validation, relance en cas d'échec. → [TP 1](exercises/TP1-sorties-structurees.md)
5. **Évaluation** — jeu de test, métriques, LLM-as-judge et ses biais. → [TP 2](exercises/TP2-evaluation.md)
6. **Agents** — tool use, boucle agentique, quand c'est utile et quand c'est du théâtre.
7. **Sécurité** — injection de prompt, en particulier via des contenus scrapés (annonces).

## Mises à jour 2027 (à intégrer aux slides)

Nouveaux points 4 à 7. Cas réel à raconter pour le point 4 : un modèle à « mode
raisonnement » ajoute du texte avant le JSON, le parsing casse en production, et la
correction consiste à désactiver ce mode pour cet appel. Morale : toujours valider la
sortie avec un schéma, jamais faire confiance au format annoncé.

## Évaluation

- [QCM](exercises/QCM-Prompt-Engineering.md) en fin de séance, non noté.
- Les TP préparent directement `prompts/EXPERIMENTS.md` de P2, qui lui est noté.

## Ressources

- [Anthropic — Prompt engineering](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [OpenAI — Structured outputs](https://platform.openai.com/docs/guides/structured-outputs)
- [Gemini API — sorties structurées](https://ai.google.dev/gemini-api/docs/structured-output)

---

[← Retour au sommaire](../../README.md)
