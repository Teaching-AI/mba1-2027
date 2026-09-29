"""
Evaluation automatique - Projet 1 : Observatoire Immobilier Toulonnais
=======================================================================
Execute par le CI a chaque push. NE MODIFIEZ PAS ce fichier.

Bareme automatique public : 15 points.
10 points supplementaires sont notes par des tests caches, lances par
l'enseignant avant la soutenance (memes fonctions, autres cas).
Le reste de la note (75 points) est evalue par l'enseignant et en soutenance.
"""

import ast
import os
import re
import sys

import pytest

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORBIDDEN_STATS = {"numpy", "pandas", "scipy", "statistics"}
FORBIDDEN_REG = {"numpy", "pandas", "scipy", "sklearn"}


def _import(module):
    sys.path.insert(0, PROJECT_ROOT)
    try:
        return __import__(module, fromlist=["_"])
    except ImportError as e:
        pytest.fail(f"{module} introuvable ou en erreur a l'import : {e}")
    finally:
        sys.path.pop(0)


def _imported_modules(path):
    with open(path) as f:
        tree = ast.parse(f.read())
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names |= {a.name.split(".")[0] for a in node.names}
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module.split(".")[0])
    return names


def _find(folder, candidates):
    for name in candidates:
        p = os.path.join(PROJECT_ROOT, folder, name)
        if os.path.exists(p):
            return p
    return None


def _find_dvf():
    return _find("data", ["dvf_toulon.csv", "dvf.csv", "dvf_83137.csv"])


def _find_annonces():
    return _find("data", ["annonces.csv", "annonces_actuelles.csv", "annonces_toulon.csv"])


# ===========================================================================
# STATISTIQUES FROM SCRATCH (5 pts)
# ===========================================================================
class TestStats:
    @pytest.fixture
    def stats(self):
        return _import("analysis.stats")

    def test_mean(self, stats):
        """[1 pt] mean()"""
        assert stats.mean([1, 2, 3, 4, 5]) == pytest.approx(3.0)

    def test_median(self, stats):
        """[1 pt] median() sur une liste de taille impaire."""
        assert stats.median([5, 1, 3]) == pytest.approx(3.0)

    def test_variance(self, stats):
        """[1 pt] variance() d'echantillon (n - 1)."""
        assert stats.variance([2, 4, 4, 4, 5, 5, 7, 9]) == pytest.approx(32 / 7, abs=1e-3)

    def test_correlation(self, stats):
        """[1 pt] correlation() vaut 1 pour deux series proportionnelles."""
        assert stats.correlation([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]) == pytest.approx(1.0, abs=1e-3)

    def test_stats_pure_python(self, stats):
        """[1 pt] stats.py n'importe ni numpy, ni pandas, ni scipy, ni statistics."""
        used = _imported_modules(os.path.join(PROJECT_ROOT, "analysis", "stats.py"))
        assert not (used & FORBIDDEN_STATS), f"Imports interdits : {used & FORBIDDEN_STATS}"


# ===========================================================================
# REGRESSION FROM SCRATCH (3 pts)
# ===========================================================================
class TestRegression:
    @pytest.fixture
    def reg(self):
        return _import("analysis.regression")

    def test_least_squares_fit(self, reg):
        """[1 pt] least_squares_fit() retrouve y = 2x + 1."""
        alpha, beta = reg.least_squares_fit([1, 2, 3, 4, 5], [3, 5, 7, 9, 11])
        assert beta == pytest.approx(2.0, abs=1e-3)
        assert alpha == pytest.approx(1.0, abs=1e-3)

    def test_r_squared(self, reg):
        """[1 pt] r_squared() vaut 1 pour un ajustement parfait."""
        x, y = [1, 2, 3, 4, 5], [3, 5, 7, 9, 11]
        alpha, beta = reg.least_squares_fit(x, y)
        assert reg.r_squared(alpha, beta, x, y) == pytest.approx(1.0, abs=1e-3)

    def test_regression_pure_python(self, reg):
        """[1 pt] regression.py n'importe ni sklearn, ni numpy, ni pandas, ni scipy."""
        used = _imported_modules(os.path.join(PROJECT_ROOT, "analysis", "regression.py"))
        assert not (used & FORBIDDEN_REG), f"Imports interdits : {used & FORBIDDEN_REG}"


# ===========================================================================
# DONNEES REELLES (4 pts)
# ===========================================================================
class TestDonnees:
    def test_dvf(self):
        """[2 pts] DVF present dans data/ avec au moins 500 transactions."""
        path = _find_dvf()
        assert path, "Aucun fichier DVF dans data/ (dvf_toulon.csv attendu)."
        import pandas as pd
        n = len(pd.read_csv(path, low_memory=False))
        assert n >= 500, f"DVF : {n} lignes, minimum 500."

    def test_annonces(self):
        """[2 pts] Au moins 100 annonces reelles avec prix et surface."""
        path = _find_annonces()
        assert path, "Aucun fichier d'annonces dans data/ (annonces.csv attendu)."
        import pandas as pd
        df = pd.read_csv(path)
        cols = {c.lower() for c in df.columns}
        assert {"prix", "surface"} <= cols, f"Colonnes 'prix' et 'surface' attendues, trouve : {sorted(cols)}"
        assert len(df) >= 100, f"{len(df)} annonces, minimum 100."


# ===========================================================================
# APPLICATION ET TESTS (3 pts)
# ===========================================================================
class TestApplication:
    def test_app_file(self):
        """[1 pt] Application Streamlit presente."""
        assert any(
            os.path.exists(os.path.join(PROJECT_ROOT, p))
            for p in ["app/streamlit_app.py", "app.py", "streamlit_app.py"]
        ), "Attendu : app/streamlit_app.py ou app.py a la racine."

    def test_readme_url(self):
        """[1 pt] README contient l'URL publique de l'application."""
        with open(os.path.join(PROJECT_ROOT, "README.md")) as f:
            content = f.read()
        patterns = [
            r"https://[\w\-]+\.streamlit\.app",
            r"https://[\w\-]+\.run\.app",
            r"https://[\w\-]+\.onrender\.com",
            r"https://[\w\-]+\.fly\.dev",
            r"https://huggingface\.co/spaces/",
        ]
        assert any(re.search(p, content) for p in patterns), "URL de deploiement absente du README."

    def test_student_tests(self):
        """[1 pt] Au moins 5 tests ecrits par l'equipe."""
        total = 0
        tests_dir = os.path.join(PROJECT_ROOT, "tests")
        for name in os.listdir(tests_dir):
            if name.startswith("test_") and name.endswith(".py") and name != "test_auto_eval.py":
                with open(os.path.join(tests_dir, name)) as f:
                    total += len(re.findall(r"def test_\w+", f.read()))
        assert total >= 5, f"{total} test(s) ecrits par l'equipe, minimum 5."
