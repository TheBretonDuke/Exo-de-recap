import subprocess
import sys
import ipywidgets as widgets
import pandas as pd
import numpy as np
import json
import random
from datetime import datetime, timedelta
from IPython.display import HTML, display
from IPython import get_ipython

def install_mongo_packages():
    """Installe les packages nécessaires pour le notebook MongoDB."""
    packages = [
        "pandas>=1.5.0",
        "numpy>=1.20.0", 
        "ipywidgets>=7.6.0",
        "pymongo>=4.0.0"
    ]
    
    print("🚀 Démarrage de l'installation des packages MongoDB...")
    print("Cette opération peut prendre quelques instants.")
    
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
            print(f"✅ {package} installé.")
        except subprocess.CalledProcessError:
            print(f"❌ Erreur lors de l'installation de {package}.")
            
    print("\\n✨ Installation terminée !")

class MongoHelper:
    def __init__(self):
        self.success_style = """
        <div style="background: linear-gradient(90deg, #4CAF50, #2E7D32); color: white; padding: 15px; border-radius: 10px; margin: 10px 0; text-align: center; font-weight: bold; font-size: 16px;">
            🍃 {message} 🍃
        </div>
        """
        
        # Vérifier si PyMongo est disponible
        try:
            import pymongo
            self.pymongo_available = True
        except ImportError:
            self.pymongo_available = False
        
        # Base de données des aides cachées
        self.helps = {
            "6.1.1": {
                "hint": "Utilisez MongoClient() pour créer la connexion. Pas besoin d'URL si MongoDB est local.",
                "solution": """# Connexion à MongoDB (local)
from pymongo import MongoClient

try:
    # Connexion locale par défaut (localhost:27017)
    client = MongoClient()
    
    # Ou explicitement:
    # client = MongoClient('mongodb://localhost:27017/')
    
    # Tester la connexion
    client.admin.command('ping')
    print("✅ Connexion à MongoDB réussie")
    
    # Sélectionner la base de données
    db = client['entreprise_db']
    print(f"📁 Base de données sélectionnée: {db.name}")
    
except Exception as e:
    print(f"❌ Erreur de connexion: {e}")
    print("💡 Assurez-vous que MongoDB est démarré")""",
                "explanation": "MongoClient() crée une connexion. MongoDB utilise des bases et collections (équivalent des tables SQL)."
            },
            "6.1.2": {
                "hint": "Les collections MongoDB sont créées automatiquement lors de la première insertion. Utilisez db['nom_collection'].",
                "solution": """# Sélectionner/créer une collection
collection = db['employes']

print(f"📦 Collection sélectionnée: {collection.name}")
print("💡 La collection sera créée automatiquement lors de la première insertion")

# Vérifier les collections existantes
collections = db.list_collection_names()
print(f"📋 Collections dans la base: {collections}")""",
                "explanation": "Les collections MongoDB sont créées automatiquement. Pas besoin de définir un schéma à l'avance."
            },
            "6.2.1": {
                "hint": "Utilisez insert_one() pour un document ou insert_many() pour plusieurs. Format: dictionnaire Python.",
                "solution": """# Insérer des documents (employés)
employes = [
    {
        "nom": "Alice Martin",
        "departement": "IT",
        "salaire": 45000,
        "skills": ["Python", "MongoDB", "Docker"],
        "date_embauche": datetime(2023, 1, 15),
        "actif": True
    },
    {
        "nom": "Bob Dupont", 
        "departement": "RH",
        "salaire": 38000,
        "skills": ["Communication", "Recrutement"],
        "date_embauche": datetime(2022, 11, 3),
        "actif": True
    },
    {
        "nom": "Charlie Dubois",
        "departement": "Finance", 
        "salaire": 52000,
        "skills": ["Excel", "Analytics", "Budget"],
        "date_embauche": datetime(2023, 3, 20),
        "actif": True
    }
]

# Insérer plusieurs documents
result = collection.insert_many(employes)
print(f"✅ {len(result.inserted_ids)} employés ajoutés")
print(f"🆔 IDs générés: {result.inserted_ids}")""",
                "explanation": "insert_many() ajoute plusieurs documents. MongoDB génère automatiquement des _id uniques."
            },
            "6.2.2": {
                "hint": "Utilisez find() pour tout récupérer, find(query) pour filtrer. Exemples: {'salaire': {'$gt': 40000}}",
                "solution": """# Différentes requêtes de lecture
print("👥 TOUS LES EMPLOYÉS:")
for employe in collection.find():
    print(f"  {employe['nom']} - {employe['departement']} - {employe['salaire']}€")

print("\\n💰 EMPLOYÉS BIEN PAYÉS (> 40000€):")
for employe in collection.find({"salaire": {"$gt": 40000}}):
    print(f"  {employe['nom']}: {employe['salaire']}€")

print("\\n💻 EMPLOYÉS IT:")
for employe in collection.find({"departement": "IT"}):
    print(f"  {employe['nom']}: {employe['skills']}")

print("\\n🔢 NOMBRE TOTAL D'EMPLOYÉS:")
count = collection.count_documents({})
print(f"  {count} employés dans la collection")""",
                "explanation": "find() récupère les documents. Utilisez les opérateurs MongoDB: $gt (>), $lt (<), $in, etc."
            },
            "6.3.1": {
                "hint": "Utilisez update_many() avec les opérateurs $set, $inc, $push. Format: update_many(filter, update)",
                "solution": """# Augmenter les salaires du département IT
result = collection.update_many(
    {"departement": "IT"},  # Filtre
    {"$inc": {"salaire": 2000}}  # Augmenter de 2000€
)

print(f"✅ {result.modified_count} salaires augmentés dans le département IT")

# Ajouter une compétence à tous les employés Finance
result2 = collection.update_many(
    {"departement": "Finance"},
    {"$push": {"skills": "PowerBI"}}  # Ajouter à la liste
)

print(f"✅ Compétence PowerBI ajoutée à {result2.modified_count} employés Finance")

# Vérifier les changements
print("\\n💻 Nouveaux salaires IT:")
for employe in collection.find({"departement": "IT"}):
    print(f"  {employe['nom']}: {employe['salaire']}€")""",
                "explanation": "update_many() modifie plusieurs documents. $inc incrémente, $push ajoute à un array, $set remplace."
            },
            "6.3.2": {
                "hint": "Utilisez delete_many() avec un filtre. Attention: sans filtre, tous les documents sont supprimés !",
                "solution": """# Supprimer les employés inactifs (s'il y en a)
result = collection.delete_many({"actif": False})
print(f"❌ {result.deleted_count} employés inactifs supprimés")

# Marquer un employé comme inactif plutôt que le supprimer
collection.update_one(
    {"nom": "Bob Dupont"},
    {"$set": {"actif": False}}
)
print("⚠️ Bob Dupont marqué comme inactif")

# Compter les employés restants actifs
actifs = collection.count_documents({"actif": True})
print(f"👥 {actifs} employés actifs restants")""",
                "explanation": "delete_many() supprime selon un filtre. Préférez marquer comme inactif plutôt que supprimer."
            }
        }
    
    def help(self, step):
        """Affiche l'aide pour une étape donnée"""
        if step not in self.helps:
            print(f"❌ Aide non trouvée pour l'étape {step}")
            return
            
        help_data = self.helps[step]
        
        # Conseil caché
        html_hint = f"""
        <details style="margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; padding: 5px; background: #f9f9f9;">
            <summary style="cursor: pointer; background: #e8f5e8; padding: 10px; border-radius: 3px; font-weight: bold; color: #2e7d32;">
                💡 Conseil MongoDB (cliquer pour dérouler)
            </summary>
            <div style="padding: 15px; margin-top: 10px; background: white; border-radius: 3px;">
                <p style="margin: 0; color: #333;">{help_data['hint']}</p>
            </div>
        </details>
        """
        
        # Solution cachée
        html_solution = f"""
        <details style="margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; padding: 5px; background: #f9f9f9;">
            <summary style="cursor: pointer; background: #e8f5e8; padding: 10px; border-radius: 3px; font-weight: bold; color: #2e7d32;">
                🔍 Solution MongoDB (cliquer pour dérouler)
            </summary>
            <div style="padding: 15px; margin-top: 10px; background: white; border-radius: 3px;">
                <p><strong>🍃 Explication :</strong> {help_data['explanation']}</p>
                <pre style="background: #f5f5f5; padding: 10px; border-radius: 3px; overflow-x: auto; border-left: 3px solid #4caf50;"><code>{help_data['solution']}</code></pre>
            </div>
        </details>
        """
        
        display(HTML(html_hint))
        display(HTML(html_solution))
    
    def solution(self, code, explanation=""):
        html = f"""
        <details style="margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; padding: 5px;">
            <summary style="cursor: pointer; background: #e8f5e8; padding: 10px; border-radius: 3px; font-weight: bold;">
                🔍 Solution MongoDB (cliquer pour révéler)
            </summary>
            <div style="background: #fafafa; padding: 15px; margin-top: 10px; border-radius: 3px;">
                {f'<p><strong>🍃 Explication MongoDB:</strong> {explanation}</p>' if explanation else ''}
                <pre style="background: #f8f8f8; padding: 10px; border-radius: 3px; overflow-x: auto;"><code>{code}</code></pre>
            </div>
        </details>
        """
        display(HTML(html))
    
    def hint(self, text):
        html = f"""
        <details style="margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; padding: 5px;">
            <summary style="cursor: pointer; background: #e8f5e8; padding: 10px; border-radius: 3px; font-weight: bold;">
                💡 Conseil MongoDB (cliquer pour révéler)
            </summary>
            <div style="background: #f0fff0; padding: 15px; margin-top: 10px; border-radius: 3px;">
                {text}
            </div>
        </details>
        """
        display(HTML(html))
    
    def success(self, message):
        html = self.success_style.format(message=message)
        display(HTML(html))
    
    def check_mongo_connection(self):
        """Vérifie la connexion à MongoDB"""
        if not self.pymongo_available:
            return False, "PyMongo n'est pas installé"
        
        try:
            from pymongo import MongoClient
            client = MongoClient()
            client.admin.command('ping')
            return True, "Connexion réussie"
        except Exception as e:
            return False, str(e)
    
    def check_connection_button(self):
        """Bouton pour vérifier la connexion MongoDB"""
        output = widgets.Output()
        button = widgets.Button(
            description="🔗 Vérifier MongoDB",
            button_style='success',
            layout=widgets.Layout(width='200px', height='35px')
        )
        
        def on_click(b):
            with output:
                output.clear_output()
                success, message = self.check_mongo_connection()
                if success:
                    print("✅ MongoDB connecté")
                    print(f"🍃 {message}")
                else:
                    print("❌ Erreur MongoDB:")
                    print(f"🚨 {message}")
                    print("💡 Vérifiez que MongoDB est démarré")
        
        button.on_click(on_click)
        display(widgets.VBox([button, output]))
    
    def show_sample_data(self):
        """Affiche des exemples de documents MongoDB"""
        sample_docs = [
            {
                "_id": "ObjectId('...')",
                "nom": "Alice Martin",
                "departement": "IT", 
                "salaire": 45000,
                "skills": ["Python", "MongoDB", "Docker"],
                "date_embauche": "2023-01-15",
                "actif": True
            },
            {
                "_id": "ObjectId('...')",
                "nom": "Bob Dupont",
                "departement": "RH",
                "salaire": 38000, 
                "skills": ["Communication", "Recrutement"],
                "date_embauche": "2022-11-03",
                "actif": True
            }
        ]
        
        print("📄 EXEMPLES DE DOCUMENTS MONGODB:")
        print("="*50)
        for i, doc in enumerate(sample_docs, 1):
            print(f"Document {i}:")
            print(json.dumps(doc, indent=2, ensure_ascii=False))
            print("-" * 30)

def load_mongo_helper():
    """Charge le système d'aide MongoDB."""
    if 'mongo_helper' not in get_ipython().user_ns:
        helper = MongoHelper()
        get_ipython().user_ns['mongo_helper'] = helper
        print("🍃 Système d'aide MongoDB chargé !")
        print("✨ Prêt pour les bases de données NoSQL !")
        
        # Vérifier si PyMongo est disponible
        if helper.pymongo_available:
            print("📦 PyMongo détecté")
        else:
            print("⚠️  PyMongo non installé - certaines fonctionnalités seront limitées")
    else:
        print("✅ Le système d'aide MongoDB est déjà chargé.")