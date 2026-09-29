# Mise en place GitHub Classroom — MBA1 2027

Organisation : **nidouillet-mba1-2027** (à créer, gratuite)
Groupes de 4, stables de P1 à P2 · 1 repo par groupe et par projet

Les scripts utilisent `ORG=nidouillet-mba1-2027` par défaut ; pour une autre org : `ORG=mon-org ./templates/...`

---

## 1. Pousser les templates dans l'organisation

À faire pour P1 avant le 4 mars, pour P2 avant le 26 avril.

```bash
# Projet 1
cp -r templates/projet-1-analyse-immobiliere /tmp/template-projet-1 && cd /tmp/template-projet-1
git init -b main && git add . && git commit -m "Template Projet 1 - Observatoire"
gh repo create nidouillet-mba1-2027/template-projet-1 --public --source . --push

# Projet 2
cp -r templates/projet-2-nidbot /tmp/template-projet-2 && cd /tmp/template-projet-2
git init -b main && git add . && git commit -m "Template Projet 2 - NidBuyer"
gh repo create nidouillet-mba1-2027/template-projet-2 --public --source . --push
```

Sur GitHub, dans chaque repo : Settings > General > cocher **Template repository**.

**Ne jamais pousser** `projets/*/evaluation/test_caches_*.py` dans un template : ils restent dans ce repo privé.

---

## 2. Créer la Classroom

1. https://classroom.github.com > **New classroom** > `nidouillet-mba1-2027`
2. Nom : `MBA1 IA 2027`
3. Importer la liste des étudiants (roster) pour relier comptes GitHub et noms.
   Le roster reste dans Classroom : **pas de CSV d'identifiants dans ce repo**.

---

## 3. Créer les assignments

| | P1 | P2 |
|---|---|---|
| Title | `Projet 1 - Observatoire` | `Projet 2 - NidBuyer` |
| Group assignment | oui, **réutiliser les équipes de P1** pour P2 | |
| Max members per group | 4 | 4 |
| Visibility | Public (Actions gratuites) | Public |
| Template | `template-projet-1` | `template-projet-2` |
| Deadline | 12 mars 2027, 8h | 30 avril 2027, 8h |
| Feedback pull request | oui | oui |

Le préfixe du nom de repo (`projet-1-...`, `projet-2-...`) est ce que les scripts cherchent : le garder.

---

## 4. Pendant le projet

- Score d'un groupe : repo > **Actions** > dernier run > **Summary**
- Au point de suivi : `./templates/contributions.sh projet-N` pour repérer qui ne pousse rien, et le dire ce jour-là

---

## 5. La veille de chaque soutenance

```bash
gh auth login   # une fois

# Tests publics (dernier run sur main)
./templates/collect_scores.sh projet-1
# Tests cachés
./templates/run_hidden_tests.sh projet-1 projets/projet_1/evaluation/test_caches_p1.py
# Contributions individuelles
./templates/contributions.sh projet-1
```

| Projet | collect_scores | run_hidden_tests |
|---|---|---|
| P1 | `./templates/collect_scores.sh projet-1` | `... projet-1 projets/projet_1/evaluation/test_caches_p1.py` |
| P2 | `./templates/collect_scores.sh projet-2` | `... projet-2 projets/projet_2/evaluation/test_caches_p2.py` |

Les CSV produits contiennent des noms et des notes : ils sont ignorés par git, les ranger sur le Drive école.
Puis pré-remplir les blocs A et B de la fiche d'évaluation du projet (`projets/projet_N/evaluation/`).

---

## Grille commune (P1, P2)

| Volet | Pts | Source |
|---|---|---|
| Code — automatique | 25 | 15 tests publics (`collect_scores.sh`) + 10 tests cachés (`run_hidden_tests.sh`) |
| Code — enseignant | 25 | Lecture du repo la veille |
| Soutenance — groupe | 30 | Jury |
| Individuel | 20 | Question individuelle (10) + contribution git (10) |

---

## FAQ

**Le CI ne se lance pas.**
Vérifier que le repo est public, ou que l'org a le statut GitHub Education (Actions sur repos privés).

**Un groupe a modifié `test_auto_eval.py`.**
```bash
gh api "repos/nidouillet-mba1-2027/<repo>/commits?path=tests/test_auto_eval.py" -q '.[].commit.message'
```
Plus d'un commit = modifié. Relancer alors les tests publics à la main avec le fichier du template.

**Les tests cachés échouent tous pour un groupe.**
Regarder d'abord si le repo s'installe (`pip install -r requirements.txt`) : un problème d'installation
fait tout échouer. Relancer à la main dans le repo cloné avant de noter.

**Inviter des observateurs (intervenants, jury).**
Organisation GitHub > People > Invite member (rôle Member) : accès en lecture aux repos et aux apps déployées.
