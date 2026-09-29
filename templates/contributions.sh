#!/bin/bash
# contributions.sh — contribution de chaque membre d'un groupe, pour la note individuelle.
# ENSEIGNANT. A lancer avant la soutenance ; sert de base aux questions individuelles.
#
# Usage :
#   ./templates/contributions.sh projet-1
#
# Pour chaque repo : commits sur main, lignes ajoutees/supprimees, PR ouvertes et mergees,
# par auteur GitHub. Ce n'est pas une note automatique : un gros diff peut etre un CSV
# commite, un petit diff peut etre le coeur de l'algo. On regarde, puis on questionne.
#
# Prerequis : gh CLI authentifie.
# Sortie : contributions_<projet>_<date>.csv (ne pas commiter : donnees etudiantes)

set -u
ORG="${ORG:-nidouillet-mba1-2027}"
PROJECT="${1:?Usage: $0 <projet-N>}"
OUTPUT="contributions_${PROJECT}_$(date +%Y%m%d).csv"

echo "Groupe,Auteur,Commits,Lignes +,Lignes -,PR ouvertes,PR mergees" > "$OUTPUT"

gh repo list "$ORG" --json name --limit 100 -q ".[].name" | grep "^$PROJECT" | sort | while read -r repo; do
  stats=$(gh api "repos/$ORG/$repo/stats/contributors" 2>/dev/null)
  # GitHub calcule ces stats en asynchrone : 202 au premier appel, on reessaie
  for _ in 1 2 3; do
    [ -n "$stats" ] && [ "$stats" != "{}" ] && break
    sleep 3; stats=$(gh api "repos/$ORG/$repo/stats/contributors" 2>/dev/null)
  done
  prs=$(gh pr list --repo "$ORG/$repo" --state all --limit 200 --json author,mergedAt 2>/dev/null || echo "[]")

  python3 - "$repo" "$stats" "$prs" >> "$OUTPUT" <<'EOF'
import json, sys
repo, stats, prs = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    stats = json.loads(stats) or []
except Exception:
    stats = []
prs = json.loads(prs or "[]")
rows = {}
for c in stats if isinstance(stats, list) else []:
    login = (c.get("author") or {}).get("login", "?")
    rows[login] = [c["total"], sum(w["a"] for w in c["weeks"]), sum(w["d"] for w in c["weeks"]), 0, 0]
for p in prs:
    login = (p.get("author") or {}).get("login", "?")
    r = rows.setdefault(login, [0, 0, 0, 0, 0])
    r[3] += 1
    r[4] += 1 if p.get("mergedAt") else 0
for login, r in sorted(rows.items(), key=lambda kv: -kv[1][0]):
    print(",".join([repo, login] + [str(v) for v in r]))
EOF
done

column -s, -t < "$OUTPUT"
echo; echo "Resultats : $OUTPUT (ne pas commiter : donnees etudiantes)"
