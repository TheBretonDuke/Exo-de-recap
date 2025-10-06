# 🎓 Exo de Récap - Formation Python Data

Ensemble de 6 notebooks Jupyter interactifs pour maîtriser Python, Pandas, ETL, SQLite, Docker et MongoDB avec un système d'aide progressif.

## 📚 Contenu des Exercices

### 🐍 **1_Python.ipynb** — Fondamentaux Python
- Syntaxe, structures de données, fonctions
- Classes et programmation orientée objet
- Gestion des erreurs et bonnes pratiques
- **Aide interactive** avec conseils et solutions masqués

### 📊 **2_Pandas.ipynb** — Manipulation de Données
- DataFrames et Series, lecture/écriture de fichiers
- Nettoyage, transformation et analyse de données  
- Visualisations et statistiques descriptives
- **Système d'aide progressif** pour l'apprentissage

### 🏭 **3_ETL.ipynb** — Pipeline ETL Complet
- **Extract** : Lecture CSV, JSON, APIs
- **Transform** : Nettoyage, enrichissement, agrégation
- **Load** : Sauvegarde multi-format
- **Pipeline automatisé** avec métriques de performance

### 🗄️ **4_SQLite_BDD.ipynb** — Bases de Données SQLite
- Connexion, création et exploration de bases
- Requêtes SQL avec pandas intégration
- CRUD : INSERT, UPDATE, DELETE
- **Index et optimisation** des performances

### 🐳 **5_Docker.ipynb** — Containerisation Docker
- Images, conteneurs, volumes et réseaux
- Docker SDK Python pour l'automation
- Dockerfile et construction d'images
- **Bonnes pratiques** de containerisation

### 🍃 **6_MongoDB_NOSQL.ipynb** — MongoDB et NoSQL
- PyMongo : connexion et CRUD operations
- **Agrégations avancées** et pipelines
- Index et optimisation MongoDB
- **Intégration avec pandas** pour l'analyse

## ✨ Fonctionnalités Pédagogiques

### 🎯 **Système d'Aide Progressif**
Chaque exercice dispose d'un helper interactif avec :
- **💡 Conseils cachés** : Cliquer pour révéler les indices
- **🔍 Solutions masquées** : Code complet avec explications
- **🎬 Démonstrations** : Boutons d'exécution automatique
- **Interface uniforme** dans tous les notebooks

### 📋 **Exercices Structurés**
- **Instructions claires** pour chaque étape
- **Progression logique** des concepts
- **Validation automatique** des résultats
- **Métriques et feedback** en temps réel

## 🛠️ Prérequis Techniques

### 📦 **Environnement**
- **macOS** (testé) ou Linux/Windows
- **Python 3.12+** recommandé
- **VS Code** + extensions Python/Jupyter, ou Jupyter Lab/Notebook

### 🔧 **Services Externes**
- **Docker Desktop** (obligatoire pour l'exercice 5)
- **MongoDB** (local ou hébergé, ex: MongoDB Atlas) pour l'exercice 6

## 🚀 Installation Rapide

### 1️⃣ **Environnement Virtuel**
```bash
# Créer et activer l'environnement
python3 -m venv .venvexoultime
source .venvexoultime/bin/activate  # macOS/Linux
# .venvexoultime\Scripts\activate   # Windows

# Mettre à jour pip
python -m pip install -U pip
```

### 2️⃣ **Dépendances**
```bash
pip install -r requirements.txt
```

### 3️⃣ **Ouverture**
- Ouvrir dans VS Code ou Jupyter
- Sélectionner l'interpréteur/Kernel `.venvexoultime`
- Exécuter la première cellule de chaque notebook

## 💡 Guide d'Utilisation

### 🎯 **Démarrage d'un Exercice**
1. **Charger le helper** : Exécuter la cellule `exec(open('helpers/...').read())`
2. **Suivre les étapes** : Instructions claires pour chaque section
3. **Utiliser l'aide** : Cliquer sur les sections d'aide pour révéler conseils et solutions
4. **Valider** : Exécuter les cellules de démonstration pour vérifier

### 📚 **Helpers Spécialisés**
Chaque notebook dispose d'un helper dédié dans le dossier `helpers/` :
- `python_basics_helper.py` — Python fondamentaux
- `setup_helper.py` — Pandas et manipulation de données  
- `etl_helper.py` — Pipelines ETL
- `sqlite_helper.py` — Bases de données SQLite
- `docker_helper.py` — Containerisation Docker
- `mongo_helper.py` — MongoDB et NoSQL

## 🔧 Conseils par Exercice

### 🐍 **Python (1_Python.ipynb)**
- Exécuter la cellule d'import en premier
- Tester chaque concept avec les exemples fournis
- Utiliser l'aide interactive pour approfondir

### 📊 **Pandas (2_Pandas.ipynb)**  
- Les datasets d'exemple se génèrent automatiquement
- Suivre l'ordre des sections pour une progression logique
- Expérimenter avec les visualisations interactives

### 🏭 **ETL (3_ETL.ipynb)**
- Les données d'exemple peuvent être régénérées automatiquement
- Tester chaque phase (Extract, Transform, Load) individuellement
- Mesurer les performances du pipeline complet

### 🗄️ **SQLite (4_SQLite_BDD.ipynb)**
- La base de données se crée automatiquement au premier lancement
- Tester les requêtes avec les boutons de démonstration
- Analyser les plans d'exécution pour l'optimisation

### 🐳 **Docker (5_Docker.ipynb)**
- **Obligatoire** : Démarrer Docker Desktop avant de commencer
- Tester la connexion avec `docker --version` dans le terminal
- Les containers d'exemple se nettoient automatiquement

### 🍃 **MongoDB (6_MongoDB_NOSQL.ipynb)**
- Par défaut : connexion `mongodb://localhost:27017`
- Pour MongoDB Atlas : adapter l'URI dans les cellules de connexion
- Tester les requêtes avec des datasets générés automatiquement

## 🆘 Dépannage

### ❌ **Erreurs Courantes**

#### 🐳 **Docker**
```bash
# Vérifier Docker
docker --version
docker run hello-world
```
**Solution** : Démarrer Docker Desktop et relancer les cellules

#### 🍃 **MongoDB**  
```bash
# Test de connexion locale
mongosh --eval "db.runCommand('ping')"
```
**Solutions** :
- Vérifier que MongoDB tourne localement
- Adapter l'URI pour Atlas : `mongodb+srv://user:pass@cluster.mongodb.net/`
- Vérifier firewall et authentification

#### 📦 **Packages manquants**
```bash
# Réinstaller les dépendances
pip install -r requirements.txt --force-reinstall
```

#### 🎨 **Widgets non affichés**
- **VS Code** : Utiliser l'extension Jupyter officielle
- **Jupyter Lab** : `jupyter labextension install @jupyter-widgets/jupyterlab-manager`

## 🎯 Objectifs Pédagogiques

À la fin de cette formation, vous maîtriserez :
- ✅ **Python avancé** : POO, gestion d'erreurs, bonnes pratiques
- ✅ **Analyse de données** : Pandas, visualisation, statistiques
- ✅ **Pipelines ETL** : Automatisation des flux de données
- ✅ **Bases de données** : SQL, NoSQL, optimisation
- ✅ **DevOps** : Containerisation, déploiement
- ✅ **Intégration** : APIs, formats de données, outils modernes

## 📈 Progression Recommandée

1. **🐍 Python** → Bases solides
2. **📊 Pandas** → Manipulation de données  
3. **🏭 ETL** → Pipelines automatisés
4. **🗄️ SQLite** → Bases relationnelles
5. **🐳 Docker** → Containerisation
6. **🍃 MongoDB** → NoSQL et Big Data

**⏱️ Durée estimée** : 2-3 heures par exercice

## 📄 Licence

**Contenu pédagogique open source**  
Usage libre dans un cadre éducatif et professionnel.

---

*Formation créée avec ❤️ pour l'apprentissage du stack Python Data moderne*
