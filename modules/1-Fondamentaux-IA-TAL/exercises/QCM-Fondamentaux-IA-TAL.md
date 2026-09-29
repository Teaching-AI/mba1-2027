# QCM - Fondamentaux de l'Intelligence Artificielle et du Traitement Automatique du Langage Naturel

## Instructions
Choisissez la ou les bonne(s) reponse(s) pour chaque question.

---

### Section 1 : Data Science et Concepts de Base

**Question 1** : Qu'est-ce qu'un data scientist selon la definition humoristique du cours ?

A) Un expert en bases de donnees
B) Quelqu'un qui s'y connait mieux en statistiques qu'un informaticien et mieux en informatique qu'un statisticien
C) Un programmeur specialise en Python
D) Un analyste de donnees certifie

<details>
<summary>Reponse</summary>
B) Quelqu'un qui s'y connait mieux en statistiques qu'un informaticien et mieux en informatique qu'un statisticien
</details>

---

**Question 2** : Quelle structure de donnees Python est recommandee pour stocker les relations d'amitie afin d'optimiser les consultations ?

A) Une liste de tuples
B) Un dictionnaire (dict)
C) Un ensemble (set)
D) Une chaine de caracteres

<details>
<summary>Reponse</summary>
B) Un dictionnaire (dict) - Les consultations dans un dict sont tres rapides.
</details>

---

**Question 3** : Que mesure le "degre de centralite" dans un reseau social ?

A) Le nombre de messages envoyes
B) Le nombre de connexions d'une personne dans le reseau
C) La frequence de connexion au site
D) L'age du compte utilisateur

<details>
<summary>Reponse</summary>
B) Le nombre de connexions d'une personne dans le reseau
</details>

---

### Section 2 : Python - Structures de Donnees

**Question 4** : Quelle est la difference principale entre une liste et un tuple en Python ?

A) Les tuples sont plus rapides
B) Les listes peuvent contenir des nombres, pas les tuples
C) Les tuples sont invariants (immutables), les listes sont mutables
D) Les tuples utilisent des crochets, les listes des parentheses

<details>
<summary>Reponse</summary>
C) Les tuples sont invariants (immutables), les listes sont mutables
</details>

---

**Question 5** : A quoi sert la classe `Counter` du module `collections` ?

A) Compter le temps d'execution
B) Transformer une sequence de valeurs en un objet qui fait correspondre des cles a des comptages
C) Creer des boucles numerotees
D) Generer des identifiants uniques

<details>
<summary>Reponse</summary>
B) Transformer une sequence de valeurs en un objet qui fait correspondre des cles a des comptages
</details>

---

**Question 6** : Quel est l'avantage d'utiliser un generateur plutot qu'une liste en Python ?

A) Les generateurs sont plus rapides a creer
B) Les generateurs permettent de traiter des elements un a un sans les conserver tous en memoire
C) Les generateurs permettent l'acces par index
D) Les generateurs sont plus faciles a debugger

<details>
<summary>Reponse</summary>
B) Les generateurs permettent de traiter des elements un a un sans les conserver tous en memoire
</details>

---

### Section 3 : Algebre Lineaire

**Question 7** : Comment represente-t-on generalement un vecteur en Python selon le cours ?

A) Comme un dictionnaire
B) Comme une liste de nombres
C) Comme une chaine de caracteres
D) Comme un tuple nomme

<details>
<summary>Reponse</summary>
B) Comme une liste de nombres
</details>

---

**Question 8** : Qu'est-ce qu'une matrice ?

A) Une collection de nombres a une dimension
B) Une collection de nombres a deux dimensions (liste de listes)
C) Un type special de vecteur
D) Une fonction mathematique

<details>
<summary>Reponse</summary>
B) Une collection de nombres a deux dimensions (liste de listes)
</details>

---

### Section 4 : Probabilites et Statistiques

**Question 9** : Quelle est la formule de la probabilite conditionnelle P(E|F) ?

A) P(E) + P(F)
B) P(E) * P(F)
C) P(E,F) / P(F)
D) P(E) / P(F)

<details>
<summary>Reponse</summary>
C) P(E,F) / P(F)
</details>

---

**Question 10** : Qu'est-ce que le theoreme de Bayes permet de faire ?

A) Calculer la moyenne d'une distribution
B) Inverser les probabilites conditionnelles
C) Determiner l'ecart-type
D) Calculer la variance

<details>
<summary>Reponse</summary>
B) Inverser les probabilites conditionnelles
</details>

---

**Question 11** : Pourquoi la distribution normale est-elle appelee "la reine des distributions" ?

A) Elle est la plus facile a calculer
B) Elle est completement determinee par deux parametres (mu et sigma) et apparait naturellement grace au theoreme de la limite centrale
C) Elle est la plus ancienne
D) Elle est utilisee uniquement en finance

<details>
<summary>Reponse</summary>
B) Elle est completement determinee par deux parametres (mu et sigma) et apparait naturellement grace au theoreme de la limite centrale
</details>

---

**Question 12** : Que stipule le theoreme de la limite centrale ?

A) Toutes les distributions sont normales
B) La moyenne d'un grand nombre de variables aleatoires independantes suit approximativement une loi normale
C) Les extremes d'une distribution sont toujours negatifs
D) La variance tend vers zero

<details>
<summary>Reponse</summary>
B) La moyenne d'un grand nombre de variables aleatoires independantes suit approximativement une loi normale
</details>

---

### Section 5 : Tests d'Hypotheses

**Question 13** : Qu'est-ce qu'une erreur de type 1 (faux positif) ?

A) Ne pas rejeter une hypothese fausse
B) Rejeter une hypothese nulle alors qu'elle est vraie
C) Accepter une hypothese alternative
D) Ne pas avoir assez de donnees

<details>
<summary>Reponse</summary>
B) Rejeter une hypothese nulle alors qu'elle est vraie
</details>

---

**Question 14** : Quel seuil de significativite est traditionnellement utilise pour les tests statistiques ?

A) 1% ou 5%
B) 10% ou 20%
C) 50%
D) 0.001%

<details>
<summary>Reponse</summary>
A) 1% ou 5%
</details>

---

**Question 15** : Qu'est-ce que le "p-hacking" ?

A) Une technique de securite informatique
B) Tester de nombreuses hypotheses jusqu'a en trouver une significative par hasard
C) Une methode pour accelerer les calculs
D) Un type de visualisation de donnees

<details>
<summary>Reponse</summary>
B) Tester de nombreuses hypotheses jusqu'a en trouver une significative par hasard
</details>

---

**Question 16** : Dans un test A/B, que compare-t-on generalement ?

A) Deux versions d'un element pour determiner laquelle est la plus efficace
B) Les performances de deux algorithmes
C) Les salaires de deux employes
D) Deux bases de donnees

<details>
<summary>Reponse</summary>
A) Deux versions d'un element pour determiner laquelle est la plus efficace
</details>

---

### Section 6 : Descente de Gradient

**Question 17** : Que represente le gradient d'une fonction ?

A) La valeur minimale de la fonction
B) Le vecteur des derivees partielles, indiquant la direction d'augmentation la plus rapide
C) La moyenne de la fonction
D) L'integrale de la fonction

<details>
<summary>Reponse</summary>
B) Le vecteur des derivees partielles, indiquant la direction d'augmentation la plus rapide
</details>

---

**Question 18** : Pour minimiser une fonction avec la descente de gradient, dans quelle direction doit-on se deplacer ?

A) Dans la direction du gradient
B) Dans la direction opposee au gradient
C) Dans une direction aleatoire
D) Perpendiculairement au gradient

<details>
<summary>Reponse</summary>
B) Dans la direction opposee au gradient
</details>

---

**Question 19** : Qu'est-ce qu'un "epoch" dans le contexte de la descente de gradient ?

A) Une erreur de calcul
B) Une passe complete sur l'ensemble des donnees
C) Un parametre fixe du modele
D) La taille du mini-lot

<details>
<summary>Reponse</summary>
B) Une passe complete sur l'ensemble des donnees
</details>

---

**Question 20** : Quel est l'avantage de la descente de gradient par mini-lots par rapport a la descente de gradient classique ?

A) Elle est toujours plus precise
B) Elle permet de faire des mises a jour plus frequentes sans evaluer tout l'ensemble de donnees
C) Elle ne necessite pas de calculer de gradient
D) Elle converge toujours vers le minimum global

<details>
<summary>Reponse</summary>
B) Elle permet de faire des mises a jour plus frequentes sans evaluer tout l'ensemble de donnees
</details>

---

### Section 7 : Exploration des Donnees

**Question 21** : Quelle est la premiere etape recommandee apres avoir obtenu des donnees ?

A) Construire immediatement un modele
B) Explorer les donnees
C) Publier les resultats
D) Supprimer les valeurs extremes

<details>
<summary>Reponse</summary>
B) Explorer les donnees
</details>

---

**Question 22** : Quel outil Python est considere comme la base pour nettoyer, transformer et manipuler les donnees ?

A) NumPy
B) Matplotlib
C) pandas
D) scikit-learn

<details>
<summary>Reponse</summary>
C) pandas
</details>

---

### Section 8 : Expressions Rationnelles

**Question 23** : Que fait `re.search("a", "cat")` en Python ?

A) Retourne False car "cat" ne commence pas par "a"
B) Retourne un objet Match car "cat" contient un "a"
C) Leve une exception
D) Retourne la position de "a"

<details>
<summary>Reponse</summary>
B) Retourne un objet Match car "cat" contient un "a"
</details>

---

### Section 9 : Intervalle de Confiance

**Question 24** : Que signifie un intervalle de confiance a 95% ?

A) Il y a 95% de chance que la vraie valeur soit dans l'intervalle
B) Si on repetait l'experience plusieurs fois, 95% des intervalles contiendraient la vraie valeur
C) 95% des donnees sont dans l'intervalle
D) L'erreur est de 5%

<details>
<summary>Reponse</summary>
B) Si on repetait l'experience plusieurs fois, 95% des intervalles contiendraient la vraie valeur
</details>

---

**Question 25** : Avant d'utiliser des tests bases sur la loi normale, que doit-on verifier ?

A) Que les donnees sont triees
B) Que les donnees suivent approximativement une loi normale
C) Que les donnees sont entieres
D) Que les donnees sont positives

<details>
<summary>Reponse</summary>
B) Que les donnees suivent approximativement une loi normale
</details>

---

## Bareme
- 25 questions
- 1 point par bonne reponse
- Note sur 25, convertible en pourcentage

| Score | Appreciation |
|-------|--------------|
| 23-25 | Excellent |
| 20-22 | Tres bien |
| 17-19 | Bien |
| 14-16 | Assez bien |
| 10-13 | Passable |
| < 10  | Insuffisant |
