# Kickoff P2 — NidBuyer · 26 avril 2027
## Guide enseignant

---

## Avant la séance

- [ ] Demander aux étudiants, avant le 26 avril : une clé AI Studio (https://aistudio.google.com), un compte Hugging Face, un compte Supabase
- [ ] Template poussé dans l'org Classroom, assignment `Projet 2 - NidBuyer` créé (groupes = ceux de P1)
- [ ] Modèle Gemini choisi et testé avec une clé AI Studio → valeur de `LLM_MODEL` à donner en séance
- [ ] Avoir déployé toi-même le template sur un Space Hugging Face (30 min) pour anticiper les blocages
- [ ] Ton profil acheteur personnel prêt pour la soutenance

---

## Déroulé J1

| Heure | Étape |
|---|---|
| 9h00 | Intro : d'où on vient (P1), ce qu'on construit, ce qui est imposé (15 min) |
| 9h15 | Organisation : périmètres, lead architecture, déclaration dans le README (20 min) |
| 9h35 | **Données** : fusion et dédoublonnage des annonces P1 → Supabase (1h) |
| 10h35 | **Premier déploiement** : API du template sur Hugging Face Spaces, `/health` et `/admin/status` en ligne (1h) |
| 11h35 | Lecture des contrats (docstrings) et des tests publics, en groupe (25 min) |
| 12h00 | Pause |
| 13h30 | Travail en groupe, passage dans chaque groupe (30 min par groupe) |
| 16h30 | Tour de table : chaque groupe montre son URL et son nombre d'annonces |

Script d'intro :
> « En P1, vous avez construit l'observatoire. Vous avez les données.
> Cette fois, vous construisez l'outil qu'un vrai acheteur utilise. Je suis cet acheteur.
> Le jour de la soutenance, je pose mes vraies questions. Et ça tourne en ligne, pas sur votre laptop. »

**Pourquoi déployer dès le J1 ?** Les problèmes de déploiement (droits, mémoire, secrets)
arrivent toujours à la fin et tuent les démos. Un service vide qui répond `/health` le J1
les fait apparaître quand on a encore le temps.

---

## Points de vigilance

**Moins de 300 annonces après fusion**
Urgence n°1. `SourceGenerique` peut extraire des annonces de pages d'agences locales.
BienIci : API JSON du site, voir `sources/bienici.py`.

**Le DVF sans quartier**
Tous les groupes butent dessus vers le J2. Anticiper dès le J1 : montrer les contours IRIS
sur data.gouv.fr, ou proposer une table section cadastrale → quartier pour 6-8 quartiers.

**Mémoire de l'hébergement**
Les offres gratuites à 512 Mo (Render, Railway) tuent le conteneur au chargement du modèle d'embedding.
Symptôme : le déploiement réussit, puis 503. D'où Hugging Face Spaces (16 Go). Faire lire les logs.

**R&D Vision sans vérité terrain**
Exiger l'annotation de 30 biens **avant** d'écrire du code de vision. Sans ça, pas de mesure possible.

**Un membre qui ne pousse rien**
Vérifier au suivi du 28 avril avec `templates/contributions.sh projet-2`.
Le dire au groupe ce jour-là, pas le jour de la soutenance.

---

## Checkpoints

| Date | À vérifier |
|---|---|
| 26 avril soir | README : rôles + nombre d'annonces · `/health` en ligne |
| 28 avril | `/rechercher` fonctionne sur l'URL déployée · contributions de chacun · premier chiffre vision · démo de 5 min · gel des fonctionnalités · synchro planifiée en place |
| 29 avril soir | `run_hidden_tests.sh` + `collect_scores.sh` + `contributions.sh` → pré-remplir les fiches |
| 30 avril | Soutenance |

---

## FAQ étudiants

**« On peut utiliser quelle source de données ? »**
Toute source dont les conditions d'utilisation le permettent. Pas de Facebook. En cas de doute, demander avant de scraper.

**« On peut appeler l'API OpenAI / Claude directement ? »**
Non. Tout passe par `backend/llm.py`. C'est ce qui permet de changer de modèle (ou de passer sur un modèle local) sans réécrire le produit.

**« Ça coûte combien ? »**
Regardez `/admin/status` : latence et nombre d'appels. Le coût par token est sur la page de tarifs de l'API Gemini. Le jury vous demandera le coût mensuel.

**« CNN ou LLM pour la vision ? »**
Libre. Dans les deux cas : 30 biens annotés à la main, précision mesurée.
