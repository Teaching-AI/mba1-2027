#!/bin/bash
# collect_scores.sh
# Lance avant chaque soutenance pour recuperer les scores CI de tous les groupes.
# Necessite : gh CLI installe et authentifie (gh auth login)
#
# Usage :
#   chmod +x collect_scores.sh
#   ./collect_scores.sh projet-1   # pour le projet 1
#   ./collect_scores.sh projet-2   # pour le projet 2

ORG="${ORG:-nidouillet-mba1-2027}"
PROJECT="${1:-projet-1}"
WORKFLOW="${WORKFLOW:-eval.yml}"
ARTIFACT="${ARTIFACT:-evaluation-report}"
REPORT="${REPORT:-evaluation_report.md}"
OUTPUT="scores_${PROJECT}_$(date +%Y%m%d).csv"

echo "Collecte des scores pour $PROJECT dans $ORG..."
echo "Groupe,Score CI,Total CI,URL Actions" > "$OUTPUT"

# Liste tous les repos du projet dans l'org
gh repo list "$ORG" --json name --limit 50 -q ".[].name" \
  | grep "$PROJECT" \
  | while read -r repo; do

    # Recupere le dernier workflow run
    run_info=$(gh run list \
      --repo "$ORG/$repo" \
      --workflow "$WORKFLOW" \
      --limit 1 \
      --json conclusion,url,databaseId \
      2>/dev/null)

    if [ -z "$run_info" ] || [ "$run_info" = "[]" ]; then
      echo "$repo,N/A,N/A,Aucun run trouve" >> "$OUTPUT"
      continue
    fi

    run_id=$(echo "$run_info" | python3 -c "import sys,json; print(json.load(sys.stdin)[0]['databaseId'])" 2>/dev/null)
    run_url=$(echo "$run_info" | python3 -c "import sys,json; print(json.load(sys.stdin)[0]['url'])" 2>/dev/null)

    # Telecharge le rapport d'evaluation
    tmpdir=$(mktemp -d)
    gh run download "$run_id" \
      --repo "$ORG/$repo" \
      --name "$ARTIFACT" \
      --dir "$tmpdir" 2>/dev/null

    if [ -f "$tmpdir/$REPORT" ]; then
      # Extrait le score depuis le rapport
      score=$(grep -oP '\*\*\K\d+ / \d+(?=\*\*)' "$tmpdir/$REPORT" | tail -1)
      echo "$repo,${score// \/ /,},$run_url" >> "$OUTPUT"
    else
      echo "$repo,rapport absent,,$run_url" >> "$OUTPUT"
    fi

    rm -rf "$tmpdir"
done

echo ""
echo "Scores sauvegardes dans $OUTPUT"
echo ""
cat "$OUTPUT"
