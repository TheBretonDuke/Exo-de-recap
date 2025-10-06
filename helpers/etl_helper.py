import subprocess
import sys
import ipywidgets as widgets
import pandas as pd
import numpy as np
import json
import csv
import os
import random
from datetime import datetime, timedelta
from pathlib import Path
from IPython.display import HTML, display
from IPython import get_ipython

def install_etl_packages():
    """Installe les packages nécessaires pour le notebook ETL."""
    packages = [
        "pandas>=1.5.0",
        "numpy>=1.20.0", 
        "ipywidgets>=7.6.0",
        "requests>=2.28.0",
        "openpyxl>=3.0.0",
        "xlsxwriter>=3.0.0"
    ]
    
    print("🚀 Démarrage de l'installation des packages ETL...")
    print("Cette opération peut prendre quelques instants.")
    
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
            print(f"✅ {package} installé.")
        except subprocess.CalledProcessError:
            print(f"❌ Erreur lors de l'installation de {package}.")
            
    print("\\n✨ Installation terminée !")

class ETLHelper:
    def __init__(self):
        self.success_style = """
        <div style="background: linear-gradient(90deg, #FF6B35, #F7931E); color: white; padding: 15px; border-radius: 10px; margin: 10px 0; text-align: center; font-weight: bold; font-size: 16px;">
            🏭 {message} 🏭
        </div>
        """
        self.data_dir = Path("data_etl")
        self.data_dir.mkdir(exist_ok=True)
        
        # Base de données des aides cachées
        self.helps = {
            "3.1.1": {
                "hint": "Utilisez pd.read_csv('chemin/fichier.csv'). Le fichier sera dans le dossier data_etl/",
                "solution": """# Extract - Lire le fichier CSV des ventes
df_ventes = pd.read_csv('data_etl/ventes.csv')

print(f"📊 Ventes extraites: {len(df_ventes)} lignes")
print("📋 Colonnes:", list(df_ventes.columns))
print("\\n🔍 Aperçu:")
print(df_ventes.head())""",
                "explanation": "pd.read_csv() lit un fichier CSV et le convertit en DataFrame. Vérifiez toujours la structure après extraction."
            },
            "3.1.2": {
                "hint": "Utilisez pd.read_json('chemin/fichier.json'). Les données JSON peuvent avoir une structure complexe.",
                "solution": """# Extract - Lire le fichier JSON des clients  
df_clients = pd.read_json('data_etl/clients.json')

print(f"👥 Clients extraits: {len(df_clients)} lignes") 
print("📋 Colonnes:", list(df_clients.columns))
print("\\n🔍 Aperçu:")
print(df_clients.head())""",
                "explanation": "pd.read_json() convertit les données JSON en DataFrame. JSON peut contenir des structures imbriquées."
            },
            "3.2.1": {
                "hint": "Utilisez .dropna(), .fillna(), .astype() pour nettoyer. pd.to_datetime() pour les dates.",
                "solution": """# Transform - Nettoyer les données de ventes
df_ventes_clean = df_ventes.copy()

# Supprimer les lignes avec des valeurs manquantes critiques
df_ventes_clean = df_ventes_clean.dropna(subset=['produit', 'prix'])

# Convertir les dates
df_ventes_clean['date'] = pd.to_datetime(df_ventes_clean['date'])

# Nettoyer les prix (convertir en float)
df_ventes_clean['prix'] = pd.to_numeric(df_ventes_clean['prix'], errors='coerce')

# Supprimer les prix invalides
df_ventes_clean = df_ventes_clean.dropna(subset=['prix'])

print(f"🧹 Données nettoyées: {len(df_ventes_clean)} lignes (était {len(df_ventes)})")""",
                "explanation": "Transform nettoie et transforme les données: suppression des nulls, conversion de types, validation."
            },
            "3.2.2": {
                "hint": "Utilisez les mêmes techniques de nettoyage. Attention aux données clients qui peuvent être plus complexes.",
                "solution": """# Transform - Nettoyer les données clients
df_clients_clean = df_clients.copy()

# Supprimer les doublons basés sur l'email
df_clients_clean = df_clients_clean.drop_duplicates(subset=['email'], keep='first')

# Nettoyer les âges (valeurs raisonnables)
df_clients_clean = df_clients_clean[(df_clients_clean['age'] >= 18) & (df_clients_clean['age'] <= 100)]

# Nettoyer les noms (pas de valeurs vides)
df_clients_clean = df_clients_clean.dropna(subset=['nom', 'email'])

print(f"👥 Clients nettoyés: {len(df_clients_clean)} lignes (était {len(df_clients)})")""",
                "explanation": "Nettoyage spécifique aux clients: suppression doublons, validation âges, données obligatoires."
            },
            "3.3.2": {
                "hint": "Utilisez .to_json() avec les paramètres orient et indent pour un JSON lisible.",
                "solution": """# Load - Sauvegarder en JSON
# Fusion des données pour créer un dataset complet
df_final = df_ventes_clean.merge(df_clients_clean, left_on='client_id', right_on='id', how='inner')

# Sauvegarder en JSON avec formatage
output_json = 'data_etl/rapport_final.json'
df_final.to_json(output_json, orient='records', indent=2, date_format='iso')

print(f"💾 Données sauvegardées en JSON: {output_json}")
print(f"📊 {len(df_final)} enregistrements dans le fichier final")""",
                "explanation": "to_json() sauvegarde un DataFrame en JSON. orient='records' crée un format liste de dictionnaires."
            },
            "3.4.1": {
                "hint": "Un pipeline ETL automatise Extract→Transform→Load. Structurez avec des phases claires et mesurez les performances.",
                "solution": """def pipeline_etl():
    \"\"\"Pipeline ETL complet automatisé\"\"\"
    import time
    start_time = time.time()
    print("🏭 DÉMARRAGE PIPELINE ETL")
    print("="*30)
    
    # 📥 EXTRACT
    print("📥 Phase EXTRACT...")
    df_ventes = pd.read_csv('data_etl/ventes.csv')
    with open('data_etl/clients.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    df_clients = pd.DataFrame(data['clients'])
    
    # 🔄 TRANSFORM  
    print("🔄 Phase TRANSFORM...")
    # Ventes
    df_ventes_clean = df_ventes.copy()
    df_ventes_clean['date'] = pd.to_datetime(df_ventes_clean['date'])
    df_ventes_clean['montant_total'] = df_ventes_clean['quantite'] * df_ventes_clean['prix_unitaire']
    df_ventes_clean['mois'] = df_ventes_clean['date'].dt.month
    df_ventes_clean['categorie_prix'] = np.where(
        df_ventes_clean['prix_unitaire'] < 50, 'Économique',
        np.where(df_ventes_clean['prix_unitaire'] < 200, 'Moyen', 'Premium')
    )
    
    # Clients
    df_clients_clean = df_clients.copy()
    df_clients_clean['nom_complet'] = df_clients_clean['prenom'] + " " + df_clients_clean['nom']
    df_clients_clean['tranche_age'] = np.where(
        df_clients_clean['age'] < 30, 'Jeune',
        np.where(df_clients_clean['age'] < 50, 'Adulte', 'Senior')
    )
    mapping_region = {
        'Paris': 'Nord', 'Lyon': 'Nord',
        'Marseille': 'Sud', 'Nice': 'Sud', 'Toulouse': 'Sud'
    }
    df_clients_clean['region'] = df_clients_clean['ville'].map(mapping_region)
    
    # 💾 LOAD
    print("💾 Phase LOAD...")
    df_ventes_clean.to_csv('data_etl/ventes_clean.csv', index=False)
    df_clients_clean.to_csv('data_etl/clients_clean.csv', index=False)
    
    rapport_ventes = {
        'total_ventes': float(df_ventes_clean['montant_total'].sum()),
        'nb_transactions': int(len(df_ventes_clean)),
        'vente_moyenne': float(df_ventes_clean['montant_total'].mean()),
        'date_rapport': datetime.now().isoformat()
    }
    
    with open('data_etl/rapport_ventes.json', 'w', encoding='utf-8') as f:
        json.dump(rapport_ventes, f, ensure_ascii=False, indent=2)
    
    # 📊 Métriques
    duree = time.time() - start_time
    metriques = {
        'ventes_lues': len(df_ventes),
        'clients_lus': len(df_clients), 
        'ventes_transformees': len(df_ventes_clean),
        'clients_transformes': len(df_clients_clean),
        'fichiers_crees': 3,
        'duree': round(duree, 2)
    }
    
    print(f"✅ PIPELINE TERMINÉ en {duree:.2f}s")
    return metriques

# Test du pipeline
# metriques = pipeline_etl()
# print("📊 Métriques:", metriques)""",
                "explanation": "Un pipeline ETL structure le processus en 3 phases : Extract (lecture), Transform (nettoyage), Load (sauvegarde). Mesurez les performances et gérez les erreurs."
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
            <summary style="cursor: pointer; background: #fff3e0; padding: 10px; border-radius: 3px; font-weight: bold; color: #ef6c00;">
                💡 Conseil ETL (cliquer pour dérouler)
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
                🔍 Solution ETL (cliquer pour dérouler)
            </summary>
            <div style="padding: 15px; margin-top: 10px; background: white; border-radius: 3px;">
                <p><strong>🏭 Explication :</strong> {help_data['explanation']}</p>
                <pre style="background: #f5f5f5; padding: 10px; border-radius: 3px; overflow-x: auto; border-left: 3px solid #ff6b35;"><code>{help_data['solution']}</code></pre>
            </div>
        </details>
        """
        
        display(HTML(html_hint))
        display(HTML(html_solution))
    
    def solution(self, code, explanation=""):
        html = f"""
        <details style="margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; padding: 5px;">
            <summary style="cursor: pointer; background: #fff3e0; padding: 10px; border-radius: 3px; font-weight: bold;">
                🔍 Solution ETL (cliquer pour révéler)
            </summary>
            <div style="background: #fafafa; padding: 15px; margin-top: 10px; border-radius: 3px;">
                {f'<p><strong>🏭 Explication ETL:</strong> {explanation}</p>' if explanation else ''}
                <pre style="background: #f8f8f8; padding: 10px; border-radius: 3px; overflow-x: auto;"><code>{code}</code></pre>
            </div>
        </details>
        """
        display(HTML(html))
    
    def hint(self, text):
        html = f"""
        <details style="margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; padding: 5px;">
            <summary style="cursor: pointer; background: #fff3e0; padding: 10px; border-radius: 3px; font-weight: bold;">
                💡 Conseil ETL (cliquer pour révéler)
            </summary>
            <div style="background: #fffdf7; padding: 15px; margin-top: 10px; border-radius: 3px;">
                {text}
            </div>
        </details>
        """
        display(HTML(html))
    
    def success(self, message):
        html = self.success_style.format(message=message)
        display(HTML(html))
        
    def create_sample_data(self):
        """Crée des fichiers de données d'exemple pour les exercices"""
        # CSV des ventes
        sales_data = {
            'date': [f"2024-{random.randint(1,12):02d}-{random.randint(1,28):02d}" for _ in range(100)],
            'produit': [random.choice(['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Phone']) for _ in range(100)],
            'quantite': [random.randint(1, 10) for _ in range(100)],
            'prix_unitaire': [round(random.uniform(10, 1000), 2) for _ in range(100)],
            'vendeur': [random.choice(['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']) for _ in range(100)]
        }
        
        sales_df = pd.DataFrame(sales_data)
        sales_df.to_csv(self.data_dir / 'ventes.csv', index=False)
        
        # JSON des clients
        clients_data = {
            'clients': [
                {
                    'id': i,
                    'nom': random.choice(['Martin', 'Dubois', 'Moreau', 'Laurent', 'Bernard']),
                    'prenom': random.choice(['Jean', 'Marie', 'Pierre', 'Sophie', 'Nicolas']),
                    'email': f"client{i}@email.com",
                    'age': random.randint(18, 70),
                    'ville': random.choice(['Paris', 'Lyon', 'Marseille', 'Toulouse', 'Nice'])
                }
                for i in range(1, 51)
            ]
        }
        
        with open(self.data_dir / 'clients.json', 'w', encoding='utf-8') as f:
            json.dump(clients_data, f, ensure_ascii=False, indent=2)
        
        return True

def load_etl_helper():
    """Charge le système d'aide ETL et crée les données d'exemple."""
    if 'etl_helper' not in get_ipython().user_ns:
        helper = ETLHelper()
        helper.create_sample_data()
        get_ipython().user_ns['etl_helper'] = helper
        print("🏭 Système d'aide ETL chargé !")
        print("📁 Dossier data_etl créé avec fichiers d'exemple")
        print("✨ Prêt pour Extract, Transform, Load !")
    else:
        print("✅ Le système d'aide ETL est déjà chargé.")