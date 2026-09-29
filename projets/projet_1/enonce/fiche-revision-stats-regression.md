# Fiche de révision — statistiques et régression

Pour le Projet 1. Tout ce qu'il faut pour coder `analysis/stats.py` et `analysis/regression.py`,
et pour répondre à la question individuelle de la soutenance. Exemples sur des prix
toulonnais inventés mais réalistes.

---

## 1. Moyenne et médiane

Cinq T2 au Mourillon, prix au m² : **3 000 · 3 200 · 3 300 · 3 500 · 6 000**

**Moyenne** = somme ÷ nombre = 19 000 ÷ 5 = **3 800 €/m²**

**Médiane** = la valeur du milieu une fois triées = **3 300 €/m²**
(si le nombre de valeurs est pair, on prend la moyenne des deux du milieu)

Le T2 à 6 000 €/m² (vue mer, refait à neuf) tire la moyenne vers le haut. La médiane l'ignore.
**C'est pour ça que NidBuyer compare un bien à la médiane du quartier, pas à la moyenne.**

```python
def mean(xs):
    return sum(xs) / len(xs)
```

---

## 2. Variance et écart-type

Question : les prix sont-ils serrés autour de la moyenne, ou très dispersés ?

1. On calcule l'écart de chaque valeur à la moyenne : 3 000 − 3 800 = −800, etc.
2. On met chaque écart au carré (pour que les négatifs ne compensent pas les positifs).
3. On fait la somme, puis on divise par **n − 1** (4 ici, pas 5).

C'est la **variance**. Son unité est bizarre (€²/m⁴) ; on prend donc sa racine carrée :
l'**écart-type**, en €/m², directement lisible.

> Pourquoi n − 1 ? On estime la dispersion de *tout* le marché à partir d'un *échantillon*
> de 5 ventes. Diviser par n sous-estimerait systématiquement cette dispersion. C'est la
> convention de Grus, et celle des tests.

---

## 3. Covariance et corrélation

Question : quand la surface augmente, le prix augmente-t-il ?

**Covariance** : pour chaque bien, (écart de la surface à sa moyenne) × (écart du prix à sa moyenne),
on somme, on divise par n − 1. Positive = ils montent ensemble. Mais sa valeur dépend des unités : illisible.

**Corrélation** = covariance ÷ (écart-type des surfaces × écart-type des prix).
Toujours entre −1 et 1.

| Corrélation | Lecture |
|---|---|
| proche de 1 | plus c'est grand, plus c'est cher, de façon très régulière |
| proche de 0 | pas de lien *linéaire* |
| proche de −1 | plus c'est grand, moins c'est cher |

Cas limite : si toutes les surfaces sont identiques, l'écart-type vaut 0 → on renvoie 0
au lieu de diviser par zéro.

---

## 4. Régression linéaire

On cherche la droite **prix = α + β × surface** qui colle le mieux aux ventes DVF.

- **β** (la pente) : combien coûte un m² de plus. Formule : β = covariance(surface, prix) ÷ variance(surface)
- **α** (l'ordonnée à l'origine) : α = moyenne(prix) − β × moyenne(surface)

« Qui colle le mieux » = qui minimise la somme des erreurs au carré entre le prix prédit
et le vrai prix. D'où le nom : **moindres carrés**.

Exemple : β = 3 067 €/m² et α = 15 000 €. Un 60 m² est prédit à 15 000 + 3 067 × 60 ≈ **199 000 €**.
S'il est affiché 170 000 €, il est 15 % sous la droite : **opportunité à regarder**.

---

## 5. Le R²

Question : la surface explique-t-elle bien le prix ?

**R² = 1 − (erreurs de la droite ÷ erreurs si on prédisait toujours la moyenne)**

| R² | Lecture pour un conseiller |
|---|---|
| 0,9 | la surface explique presque tout le prix |
| 0,4 | la surface compte, mais le quartier, l'étage, l'état, la vue comptent autant |
| 0,05 | la surface seule ne sert à rien pour prédire |

Sur Toulon, attendez-vous à un R² moyen : un 50 m² au Mourillon et un 50 m² à la
Beaucaire ne valent pas le même prix. **Un R² moyen n'est pas un échec : c'est une information.**
L'expliquer en soutenance vaut plus qu'un R² élevé obtenu sans comprendre.

---

## Pour s'entraîner à la main

Surfaces : 30, 45, 60, 75, 90 m² · Prix : 110 k, 150 k, 205 k, 230 k, 300 k€

1. Moyenne des surfaces ? des prix ?
2. Médiane des prix ?
3. Le 60 m² est-il au-dessus ou en dessous de la droite de régression ?

Réponses : 60 m² et 199 k€ · 205 k€ · au-dessus (prédit ≈ 199 k€, réel 205 k€).
