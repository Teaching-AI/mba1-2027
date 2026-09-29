#!/bin/bash
# run_hidden_tests.sh — lance les tests caches sur tous les repos d'un projet.
# ENSEIGNANT. A lancer la veille de la soutenance.
#
# Usage :
#   ./templates/run_hidden_tests.sh projet-1 projets/projet_1/evaluation/test_caches_p1.py
#
# Prerequis : gh CLI authentifie (gh auth login), python3, pytest, pandas.
# Sortie : hidden_<projet>_<date>.csv (groupe, tests passes, points)

set -u
ORG="${ORG:-nidouillet-mba1-2027}"
PROJECT="${1:?Usage: $0 <projet-N> <fichier_tests_caches.py>}"
TESTS="$(realpath "${2:?Fichier de tests caches manquant}")"
OUTPUT="hidden_${PROJECT}_$(date +%Y%m%d).csv"
WORK="$(mktemp -d)"

# Points par test : lus dans les docstrings "[N pt]" / "[N pts]"
python3 - "$TESTS" > "$WORK/points.json" <<'EOF'
import ast, json, re, sys
tree = ast.parse(open(sys.argv[1]).read())
pts = {}
for n in ast.walk(tree):
    if isinstance(n, ast.FunctionDef) and n.name.startswith("test_"):
        m = re.search(r"\[(\d+) pts?\]", ast.get_docstring(n) or "")
        pts[n.name] = int(m.group(1)) if m else 0
print(json.dumps(pts))
EOF

echo "Groupe,Tests passes,Points,Total" > "$OUTPUT"

gh repo list "$ORG" --json name --limit 100 -q ".[].name" | grep "^$PROJECT" | sort | while read -r repo; do
  echo "== $repo"
  dir="$WORK/$repo"
  if ! gh repo clone "$ORG/$repo" "$dir" -- --depth 1 -q 2>/dev/null; then
    echo "$repo,clone impossible,0," >> "$OUTPUT"; continue
  fi
  (cd "$dir" && pip install -q -r requirements.txt >/dev/null 2>&1; \
   python3 -m pytest "$TESTS" -q -p no:cacheprovider --junitxml="$WORK/$repo.xml" >/dev/null 2>&1)
  python3 - "$WORK/$repo.xml" "$WORK/points.json" "$repo" >> "$OUTPUT" <<'EOF'
import json, sys, xml.etree.ElementTree as ET
xml, pts, repo = sys.argv[1], json.load(open(sys.argv[2])), sys.argv[3]
total = sum(pts.values())
try:
    cases = list(ET.parse(xml).getroot().iter("testcase"))
except Exception:
    print(f"{repo},erreur pytest,0,{total}"); sys.exit()
ok = [c.get("name") for c in cases if c.find("failure") is None and c.find("error") is None and c.find("skipped") is None]
print(f"{repo},{len(ok)}/{len(pts)},{sum(pts.get(n, 0) for n in ok)},{total}")
EOF
done

rm -rf "$WORK"
echo; column -s, -t < "$OUTPUT"
echo; echo "Resultats : $OUTPUT (ne pas commiter : donnees etudiantes)"
