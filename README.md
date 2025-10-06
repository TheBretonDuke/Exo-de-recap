# Exo de récap

Ensemble de 6 notebooks Jupyter pour réviser Python, Pandas, ETL, SQLite, Docker et MongoDB.

## Contenu
- `1_Python.ipynb` — Rappels Python (syntaxe, structures, fonctions).
- `2_Pandas.ipynb` — Manipulation de données avec Pandas.
- `3_ETL.ipynb` — Pipeline ETL: extraction, transformation, chargement.
- `4_SQLite_BDD.ipynb` — Bases de données SQLite, SQL de base.
- `5_Docker.ipynb` — Docker: images, containers, volumes, via SDK Python.
- `6_MongoDB_NOSQL.ipynb` — MongoDB avec PyMongo: CRUD, index, agrégations.

## Prérequis
- macOS (testé), Python 3.12 recommandé.
- VS Code + extensions Python/Jupyter, ou Jupyter Lab/Notebook.
- Docker Desktop (obligatoire pour l’exo 5 — Docker).
- MongoDB (local ou hébergé, ex: MongoDB Atlas) pour l’exo 6 — MongoDB.

## Installation rapide
1) Créer un environnement virtuel et l’activer (exemple zsh/macOS):

```bash
python3 -m venv .venvexoultime
source .venvexoultime/bin/activate
python -m pip install -U pip
```

2) Installer les dépendances:

```bash
pip install -r requirements.txt
```

3) Ouvrir dans VS Code ou Jupyter et sélectionner l’interpréteur/Kernel associé à `.venvexoultime`.

## Conseils d’exécution
- Chaque notebook contient en général une cellule d’install/check d’imports. Exécutez-la en premier au besoin.
- SQLite (exo 4): si aucune base n’existe, le notebook peut créer la BDD et les tables automatiquement lors des cellules de setup.
- ETL (exo 3): les données d’exemple peuvent être régénérées par les cellules de préparation prévues dans le notebook.
- Docker (exo 5): assurez-vous que Docker Desktop est démarré. Sinon, les appels au SDK lèveront des erreurs de connexion.
- MongoDB (exo 6): par défaut, PyMongo tentera `mongodb://localhost:27017`. Pour une instance distante (Atlas), adaptez l’URI dans le notebook (variable de connexion ou cellule dédiée).

## Dépannage
- Erreurs Docker: démarrez Docker Desktop, puis relancez les cellules.
- Connexion Mongo refusée: vérifiez que le serveur tourne, l’URI, le firewall, et l’authentification si nécessaire.
- ipywidgets/visualisations: si un widget ne s’affiche pas, assurez-vous d’être dans VS Code (Jupyter intégré) ou Jupyter Lab récent.

## Licence
Contenu pédagogique. Usage libre dans un cadre éducatif.
