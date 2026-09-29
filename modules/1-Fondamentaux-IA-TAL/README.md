# Module 1 — Fondamentaux de l'IA et du TAL

**1er mars 2027** · avec le kickoff P0 l'après-midi

## Objectifs

À la fin du module, l'étudiant sait :
- expliquer la différence entre règle codée, apprentissage supervisé et modèle génératif ;
- dire ce qu'un embedding représente et pourquoi deux textes proches ont des vecteurs proches ;
- situer un LLM dans la chaîne tokens → embeddings → prédiction du token suivant ;
- repérer ce qu'un LLM fait mal par construction (calcul exact, faits récents, sources).

## Supports

- [Slides (PDF)](class_material/Fondamentaux-de-l-Intelligence-Artificielle-et-du-Traitement-Automatique-du-Langage-Naturel.pdf)
- [Version texte des slides](class_material/Fondamentaux-de-l-Intelligence-Artificielle-et-du-Traitement-Automatique-du-Langage-Naturel.txt) (recherche, copier-coller du code)

## Déroulé

1. **Data science : le cas DataSciencester** (Grus, ch. 1)
   Représentation des données, métriques de centralité, suggestion d'amis, centres d'intérêt.
2. **Cours accéléré de Python**
   Juste ce qu'il faut pour lire et modifier le code des projets.
3. **NLP et word embeddings**
   Vocabulaire, tokenisation, Word2Vec, puis passage aux LLM.

## Mises à jour 2027 (à intégrer aux slides)

- **Multimodal** : un même modèle lit texte et images. C'est ce qu'utilise la R&D vision de P2
  (estimer l'état d'un bien à partir des photos d'annonce).
- **Petits modèles ouverts** : un modèle de quelques milliards de paramètres tourne sur un
  laptop ou un serveur interne, sans envoyer de données dans le cloud (sujet repris en MBA2).
- **Limites à montrer en live** : demander un calcul de prix au m² sur 20 biens, puis
  le refaire en Python. L'écart justifie tout le « from scratch » de P1.

## Évaluation

[QCM](exercises/QCM-Fondamentaux-IA-TAL.md) en fin de séance, non noté, pour se situer.

## Pour aller plus loin

- Joel Grus, *Data Science From Scratch*, 2e éd. (O'Reilly) — référence de P1
- [Hugging Face — cours NLP](https://huggingface.co/learn/llm-course)

---

[← Retour au sommaire](../../README.md)
