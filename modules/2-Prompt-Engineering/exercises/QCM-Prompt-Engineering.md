# QCM - Prompt Engineering

## Instructions
Choisissez la ou les bonne(s) reponse(s) pour chaque question.

---

### Section 1 : Introduction au Prompt Engineering

**Question 1** : Qu'est-ce que le prompt engineering ?

A) Une technique de programmation classique
B) Une discipline pour developper et optimiser des prompts afin d'utiliser efficacement les modeles de langage
C) Un langage de programmation
D) Une methode de compression de donnees

<details>
<summary>Reponse</summary>
B) Une discipline pour developper et optimiser des prompts afin d'utiliser efficacement les modeles de langage
</details>

---

**Question 2** : A quoi sert le prompt engineering pour les chercheurs ?

A) A creer de nouveaux modeles de langage
B) A ameliorer la capacite des LLMs sur des taches complexes comme le raisonnement arithmetique
C) A reduire la taille des modeles
D) A accelerer l'entrainement des modeles

<details>
<summary>Reponse</summary>
B) A ameliorer la capacite des LLMs sur des taches complexes comme le raisonnement arithmetique
</details>

---

### Section 2 : Parametres des LLM

**Question 3** : Que controle le parametre "Temperature" dans un LLM ?

A) La vitesse de generation
B) Le niveau de determinisme/aleatoire des reponses
C) La longueur maximale de la reponse
D) Le nombre de tokens en entree

<details>
<summary>Reponse</summary>
B) Le niveau de determinisme/aleatoire des reponses - Une temperature basse donne des resultats plus deterministes, une temperature haute plus de diversite.
</details>

---

**Question 4** : Quelle est la recommandation generale concernant Temperature et Top P ?

A) Toujours utiliser les deux au maximum
B) Modifier l'un ou l'autre, mais pas les deux en meme temps
C) Toujours les mettre a zero
D) Les ignorer completement

<details>
<summary>Reponse</summary>
B) Modifier l'un ou l'autre, mais pas les deux en meme temps
</details>

---

**Question 5** : Que fait le parametre "Max Length" ?

A) Limite la taille du prompt en entree
B) Gere le nombre de tokens que le modele genere en sortie
C) Definit la taille du vocabulaire
D) Controle la memoire utilisee

<details>
<summary>Reponse</summary>
B) Gere le nombre de tokens que le modele genere en sortie
</details>

---

**Question 6** : Quelle est la difference entre "Frequency Penalty" et "Presence Penalty" ?

A) Il n'y a pas de difference
B) Frequency Penalty penalise proportionnellement au nombre d'apparitions, Presence Penalty applique une penalite fixe pour tout token repete
C) Presence Penalty est plus fort que Frequency Penalty
D) Frequency Penalty ne fonctionne qu'en anglais

<details>
<summary>Reponse</summary>
B) Frequency Penalty penalise proportionnellement au nombre d'apparitions, Presence Penalty applique une penalite fixe pour tout token repete
</details>

---

### Section 3 : Elements d'un Prompt

**Question 7** : Quels sont les quatre elements possibles d'un prompt ?

A) Titre, Corps, Conclusion, Signature
B) Instruction, Contexte, Input Data, Output Indicator
C) Question, Reponse, Exemple, Reference
D) Introduction, Developpement, Conclusion, Annexe

<details>
<summary>Reponse</summary>
B) Instruction, Contexte, Input Data, Output Indicator
</details>

---

**Question 8** : Est-il obligatoire d'avoir les quatre elements dans chaque prompt ?

A) Oui, toujours
B) Non, le format depend de la tache a accomplir
C) Oui, sinon le modele ne comprend pas
D) Non, un seul element suffit toujours

<details>
<summary>Reponse</summary>
B) Non, le format depend de la tache a accomplir
</details>

---

### Section 4 : Zero-Shot et Few-Shot Prompting

**Question 9** : Qu'est-ce que le "zero-shot prompting" ?

A) Un prompt sans aucun mot
B) Demander directement au modele une reponse sans fournir d'exemples
C) Un prompt qui echoue systematiquement
D) Un prompt avec zero token

<details>
<summary>Reponse</summary>
B) Demander directement au modele une reponse sans fournir d'exemples
</details>

---

**Question 10** : Qu'est-ce que le "few-shot prompting" ?

A) Un prompt tres court
B) Fournir quelques exemples (demonstrations) dans le prompt pour guider le modele
C) Un prompt qui genere peu de tokens
D) Une technique pour reduire les couts

<details>
<summary>Reponse</summary>
B) Fournir quelques exemples (demonstrations) dans le prompt pour guider le modele
</details>

---

**Question 11** : Selon les recherches, qu'est-ce qui est plus important dans le few-shot prompting que la correction des labels individuels ?

A) La longueur des exemples
B) L'espace des labels et la distribution du texte d'entree specifies par les demonstrations
C) La langue utilisee
D) Le nombre exact d'exemples

<details>
<summary>Reponse</summary>
B) L'espace des labels et la distribution du texte d'entree specifies par les demonstrations
</details>

---

### Section 5 : Chain-of-Thought (CoT) Prompting

**Question 12** : Qu'est-ce que le "Chain-of-Thought Prompting" ?

A) Enchainer plusieurs prompts independants
B) Amener le modele a generer des etapes de raisonnement intermediaires avant la reponse finale
C) Utiliser plusieurs modeles en sequence
D) Creer une chaine de blocs

<details>
<summary>Reponse</summary>
B) Amener le modele a generer des etapes de raisonnement intermediaires avant la reponse finale
</details>

---

**Question 13** : Quelle phrase magique peut declencher le Chain-of-Thought de maniere automatique (Zero-Shot CoT) ?

A) "Give me the answer"
B) "Let's think step by step"
C) "Calculate now"
D) "Answer immediately"

<details>
<summary>Reponse</summary>
B) "Let's think step by step"
</details>

---

**Question 14** : Qu'est-ce que l'Auto-CoT propose par Zhang et al. ?

A) Un modele qui s'entraine automatiquement
B) Une approche pour generer automatiquement des chaines de raisonnement en utilisant la diversite des questions
C) Un correcteur automatique de prompts
D) Un traducteur automatique

<details>
<summary>Reponse</summary>
B) Une approche pour generer automatiquement des chaines de raisonnement en utilisant la diversite des questions
</details>

---

### Section 6 : Self-Consistency

**Question 15** : Quel est le principe de la technique "Self-Consistency" ?

A) Verifier que le modele donne toujours la meme reponse
B) Echantillonner plusieurs chemins de raisonnement et selectionner la reponse la plus coherente/frequente
C) Entrainer le modele sur ses propres erreurs
D) Comparer plusieurs modeles

<details>
<summary>Reponse</summary>
B) Echantillonner plusieurs chemins de raisonnement et selectionner la reponse la plus coherente/frequente
</details>

---

### Section 7 : Generated Knowledge Prompting

**Question 16** : Que fait le "Generated Knowledge Prompting" ?

A) Genere des connaissances aleatoires
B) Utilise le modele pour generer des connaissances pertinentes avant de faire une prediction
C) Supprime les connaissances incorrectes
D) Traduit les connaissances dans d'autres langues

<details>
<summary>Reponse</summary>
B) Utilise le modele pour generer des connaissances pertinentes avant de faire une prediction
</details>

---

### Section 8 : Prompt Chaining

**Question 17** : Qu'est-ce que le "Prompt Chaining" ?

A) Repeter le meme prompt plusieurs fois
B) Decomposer une tache en sous-taches et utiliser la reponse d'un prompt comme entree du suivant
C) Enchainer des mots-cles
D) Creer des liens hypertextes

<details>
<summary>Reponse</summary>
B) Decomposer une tache en sous-taches et utiliser la reponse d'un prompt comme entree du suivant
</details>

---

**Question 18** : Quels sont les avantages du Prompt Chaining ?

A) Reduction des couts uniquement
B) Transparence, controlabilite et fiabilite accrues de l'application LLM
C) Vitesse de reponse amelioree uniquement
D) Reduction de la taille du modele

<details>
<summary>Reponse</summary>
B) Transparence, controlabilite et fiabilite accrues de l'application LLM
</details>

---

### Section 9 : Tree of Thoughts (ToT)

**Question 19** : Qu'est-ce que le "Tree of Thoughts" prompting ?

A) Un prompt en forme d'arbre
B) Une generalisation du CoT permettant l'exploration systematique de pensees avec retour en arriere possible
C) Un algorithme de tri
D) Une technique de compression

<details>
<summary>Reponse</summary>
B) Une generalisation du CoT permettant l'exploration systematique de pensees avec retour en arriere possible
</details>

---

**Question 20** : Quels algorithmes de recherche peuvent etre utilises avec Tree of Thoughts ?

A) Recherche binaire uniquement
B) BFS (Breadth-First Search) et DFS (Depth-First Search)
C) Tri a bulles
D) Recherche lineaire

<details>
<summary>Reponse</summary>
B) BFS (Breadth-First Search) et DFS (Depth-First Search)
</details>

---

### Section 10 : RAG (Retrieval Augmented Generation)

**Question 21** : Qu'est-ce que le RAG ?

A) Un type de modele de langage
B) Une methode combinant un composant de recherche d'information avec un generateur de texte
C) Un format de fichier
D) Un langage de programmation

<details>
<summary>Reponse</summary>
B) Une methode combinant un composant de recherche d'information avec un generateur de texte
</details>

---

**Question 22** : Quels problemes le RAG aide-t-il a resoudre ?

A) La lenteur des modeles
B) Les hallucinations et le manque d'informations a jour
C) La consommation electrique
D) La taille des modeles

<details>
<summary>Reponse</summary>
B) Les hallucinations et le manque d'informations a jour
</details>

---

### Section 11 : Hallucinations

**Question 23** : Qu'est-ce qu'une "hallucination" dans le contexte des LLM ?

A) Une erreur de syntaxe
B) Une reponse factuellement incorrecte, absurde ou deconnectee du prompt
C) Un bug du systeme
D) Une reponse trop longue

<details>
<summary>Reponse</summary>
B) Une reponse factuellement incorrecte, absurde ou deconnectee du prompt
</details>

---

### Section 12 : Techniques Avancees

**Question 24** : Que fait le ReAct Prompting ?

A) Reagit aux erreurs
B) Genere des traces de raisonnement et des actions specifiques de maniere entrelacee, permettant l'interaction avec des environnements externes
C) Reactive les anciens modeles
D) Reduit les temps de reponse

<details>
<summary>Reponse</summary>
B) Genere des traces de raisonnement et des actions specifiques de maniere entrelacee, permettant l'interaction avec des environnements externes
</details>

---

**Question 25** : Que fait PAL (Program-Aided Language Models) ?

A) Cree des programmes visuels
B) Genere des programmes comme etapes de raisonnement intermediaires et delegue l'execution a un interpreteur
C) Traduit du code
D) Corrige les erreurs de programmation

<details>
<summary>Reponse</summary>
B) Genere des programmes comme etapes de raisonnement intermediaires et delegue l'execution a un interpreteur
</details>

---

### Section 13 : Metriques d'Evaluation

**Question 26** : Que mesure la metrique BLEU ?

A) La qualite du son
B) La precision des n-grammes de mots entre le texte genere et le texte de reference
C) La vitesse de generation
D) La taille du vocabulaire

<details>
<summary>Reponse</summary>
B) La precision des n-grammes de mots entre le texte genere et le texte de reference
</details>

---

**Question 27** : Quelle est la difference principale entre BLEU et ROUGE ?

A) BLEU est plus ancien
B) BLEU mesure la precision, ROUGE mesure le rappel
C) ROUGE est plus rapide
D) Il n'y a pas de difference

<details>
<summary>Reponse</summary>
B) BLEU mesure la precision, ROUGE mesure le rappel
</details>

---

**Question 28** : Qu'est-ce que BERTScore ?

A) Un score de popularite
B) Une metrique utilisant les embeddings contextuels de BERT pour comparer les textes
C) Un classement des modeles BERT
D) Un test de performance

<details>
<summary>Reponse</summary>
B) Une metrique utilisant les embeddings contextuels de BERT pour comparer les textes
</details>

---

### Section 14 : Bonnes Pratiques

**Question 29** : Pour une tache de QA factuelle, quelle temperature est recommandee ?

A) Tres haute pour plus de creativite
B) Basse pour des reponses plus determinstes et concises
C) Moyenne
D) Aleatoire

<details>
<summary>Reponse</summary>
B) Basse pour des reponses plus determinstes et concises
</details>

---

**Question 30** : Quel type de tache beneficie d'une temperature plus elevee ?

A) Les calculs mathematiques
B) La generation creative (poemes, histoires)
C) La traduction technique
D) L'extraction de donnees

<details>
<summary>Reponse</summary>
B) La generation creative (poemes, histoires)
</details>

---

## Bareme
- 30 questions
- 1 point par bonne reponse
- Note sur 30, convertible en pourcentage

| Score | Appreciation |
|-------|--------------|
| 27-30 | Excellent |
| 24-26 | Tres bien |
| 20-23 | Bien |
| 16-19 | Assez bien |
| 12-15 | Passable |
| < 12  | Insuffisant |
