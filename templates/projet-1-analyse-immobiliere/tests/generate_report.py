#!/usr/bin/env python3
"""Generateur de rapport de notation - Projet 1 : Observatoire Immobilier."""

import os
import xml.etree.ElementTree as ET

SCORE_MAP = {
    "test_mean":                  (1, "Statistiques from scratch"),
    "test_median":                (1, "Statistiques from scratch"),
    "test_variance":              (1, "Statistiques from scratch"),
    "test_correlation":           (1, "Statistiques from scratch"),
    "test_stats_pure_python":     (1, "Statistiques from scratch"),
    "test_least_squares_fit":     (1, "Regression from scratch"),
    "test_r_squared":             (1, "Regression from scratch"),
    "test_regression_pure_python": (1, "Regression from scratch"),
    "test_dvf":                   (2, "Donnees reelles"),
    "test_annonces":              (2, "Donnees reelles"),
    "test_app_file":              (1, "Application et tests"),
    "test_readme_url":            (1, "Application et tests"),
    "test_student_tests":         (1, "Application et tests"),
}

# Reste de la note (voir README du repo cours) : affiche pour information
SOUTENANCE_ITEMS = [
    ("Tests caches (enseignant, avant soutenance)", 10),
    ("Code - enseignant", 25),
    ("Soutenance - groupe", 30),
    ("Individuel (question + contribution git)", 20),
]


def parse_results(xml_path):
    results = {}
    if not os.path.exists(xml_path):
        return results
    root = ET.parse(xml_path).getroot()
    for tc in root.iter("testcase"):
        name = tc.get("name", "")
        failed = tc.find("failure") is not None or tc.find("error") is not None
        skipped = tc.find("skipped") is not None
        results[name] = "skip" if skipped else ("fail" if failed else "pass")
    return results


def generate_report(results):
    lines = [
        "# Rapport d'Evaluation - Projet 1 : Observatoire Immobilier",
        "",
        "## Score automatique (GitHub CI)",
        "",
    ]

    categories = list(dict.fromkeys(v[1] for v in SCORE_MAP.values()))
    total_earned = total_possible = 0

    for cat in categories:
        lines += [f"### {cat}", "", "| Critere | Points | Resultat |",
                  "|---------|--------|----------|"]
        for test, (pts, c) in SCORE_MAP.items():
            if c != cat:
                continue
            status = results.get(test, "not_run")
            icon = {"pass": "PASS", "fail": "FAIL", "skip": "SKIP"}.get(status, "N/A")
            earned = pts if status == "pass" else 0
            total_earned += earned
            total_possible += pts
            display = test.replace("test_", "").replace("_", " ").title()
            lines.append(f"| {display} | {earned}/{pts} | {icon} |")
        lines.append("")

    lines += [
        "---",
        "",
        "## Reste de la note (evalue par l'enseignant)",
        "",
        "| Critere | Points |",
        "|---------|--------|",
    ]
    soutenance_total = 0
    for label, pts in SOUTENANCE_ITEMS:
        lines.append(f"| {label} | ?/{pts} |")
        soutenance_total += pts
    lines += [
        "",
        "---",
        "",
        "## Resume",
        "",
        f"| | Score |",
        f"|--|-------|",
        f"| **CI automatique** | **{total_earned} / {total_possible}** |",
        f"| Reste de la note | ? / {soutenance_total} |",
        f"| **Total** | **/ {total_possible + soutenance_total}** |",
        "",
    ]

    if total_earned == total_possible:
        lines.append("> Tous les tests CI passent.")
    elif total_earned >= total_possible * 0.7:
        lines.append("> Bon travail. Quelques tests en echec a corriger.")
    else:
        lines.append("> Plusieurs tests echouent. Consultez les details ci-dessus.")

    lines += ["", "---", "*Rapport genere automatiquement par le CI.*"]
    return "\n".join(lines)


def main():
    results = parse_results("eval_results.xml")
    report = generate_report(results)
    with open("evaluation_report.md", "w") as f:
        f.write(report)
    print(report)


if __name__ == "__main__":
    main()
