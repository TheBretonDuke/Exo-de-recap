# 📁 Dossier Helpers

Ce dossier contient tous les fichiers helper pour les notebooks Jupyter.

## 📋 Liste des helpers :

### 🐍 `python_basics_helper.py`
- **Pour :** `1_Python.ipynb`
- **Contient :** Fonctions d'aide pour les exercices Python de base
- **Fonctionnalités :** Boutons d'installation, système d'aide, vérifications

### 📊 `setup_helper.py`
- **Pour :** `2_Pandas.ipynb`
- **Contient :** Fonctions d'aide pour Pandas et manipulation de données
- **Fonctionnalités :** Installation packages, PandasHelper class, boutons d'aide

### 🔄 `etl_helper.py`
- **Pour :** `3_ETL.ipynb`
- **Contient :** Fonctions d'aide pour Extract-Transform-Load
- **Fonctionnalités :** Installation packages ETL, ETLHelper class, génération de données

### 🗄️ `sqlite_helper.py`
- **Pour :** `4_SQLite_BDD.ipynb`
- **Contient :** Fonctions d'aide pour bases de données SQLite
- **Fonctionnalités :** Installation packages SQLite, SQLiteHelper class, gestion BDD

### 🐳 `docker_helper.py`
- **Pour :** `5_Docker.ipynb`
- **Contient :** Fonctions d'aide pour Docker et containerisation
- **Fonctionnalités :** Installation packages Docker, DockerHelper class, gestion containers

### 🍃 `mongo_helper.py`
- **Pour :** `6_MongoDB_NOSQL.ipynb`
- **Contient :** Fonctions d'aide pour MongoDB NoSQL
- **Fonctionnalités :** Installation packages MongoDB, MongoHelper class, gestion collections

## 🚀 Utilisation dans les notebooks :

Chaque notebook charge son helper avec une seule ligne :
```python
exec(open('helpers/nom_du_helper.py').read())
```

Cette ligne :
- Installe automatiquement les packages nécessaires
- Charge la classe helper correspondante
- Affiche les boutons d'aide interactifs
- Prépare l'environnement pour les exercices

## ✨ Avantages de cette organisation :

- **Interface propre** : Plus de "pavés" de code dans les notebooks
- **Maintenance facile** : Tout le code complexe centralisé dans les helpers
- **Réutilisabilité** : Les helpers peuvent être réutilisés dans d'autres projets
- **Organisation claire** : Séparation entre contenu pédagogique et code technique