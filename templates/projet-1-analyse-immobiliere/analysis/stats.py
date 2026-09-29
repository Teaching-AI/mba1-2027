"""
Fonctions statistiques from scratch.
Reference : Joel Grus, "Data Science From Scratch", chapitre 5.

IMPORTANT : N'importez pas numpy, pandas, scipy ou statistics dans ce fichier.
Implementez-les avec du Python pur (listes, boucles, math).
"""

import math


def mean(xs: list[float]) -> float:
    """Retourne la moyenne d'une liste de nombres."""
    # VOTRE CODE ICI
    raise NotImplementedError("Implementez mean() - voir Grus ch.5")


def median(xs: list[float]) -> float:
    """Retourne la mediane d'une liste de nombres."""
    # VOTRE CODE ICI
    raise NotImplementedError("Implementez median() - voir Grus ch.5")


def variance(xs: list[float]) -> float:
    """Retourne la variance d'echantillon (division par n - 1), comme dans Grus ch.5.
    Exemple : variance([2, 4, 4, 4, 5, 5, 7, 9]) ~= 4.571
    """
    # VOTRE CODE ICI
    raise NotImplementedError("Implementez variance() - voir Grus ch.5")


def standard_deviation(xs: list[float]) -> float:
    """Retourne l'ecart-type : racine carree de la variance d'echantillon."""
    # VOTRE CODE ICI
    raise NotImplementedError("Implementez standard_deviation() - voir Grus ch.5")


def covariance(xs: list[float], ys: list[float]) -> float:
    """Retourne la covariance d'echantillon (division par n - 1) entre deux series."""
    # VOTRE CODE ICI
    raise NotImplementedError("Implementez covariance() - voir Grus ch.5")


def correlation(xs: list[float], ys: list[float]) -> float:
    """
    Retourne le coefficient de correlation de Pearson entre deux series.
    Retourne 0 si l'une des series a un ecart-type nul.
    """
    # VOTRE CODE ICI
    raise NotImplementedError("Implementez correlation() - voir Grus ch.5")
