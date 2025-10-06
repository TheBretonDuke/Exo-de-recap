import subprocess
import sys
import ipywidgets as widgets
import pandas as pd
import numpy as np
import sqlite3
import os
import random
from datetime import datetime, timedelta
from IPython.display import HTML, display
from IPython import get_ipython

def install_sqlite_packages():
    """Installe les packages nécessaires pour le notebook SQLite."""
    packages = [
        "pandas>=1.5.0",
        "numpy>=1.20.0", 
        "ipywidgets>=7.6.0",
        "matplotlib>=3.5.0"
    ]
    
    print("🚀 Démarrage de l'installation des packages SQLite...")
    print("📝 Note: SQLite est inclus dans Python, aucune installation supplémentaire nécessaire")
    
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
            print(f"✅ {package} installé.")
        except subprocess.CalledProcessError:
            print(f"❌ Erreur lors de l'installation de {package}.")
            
    print("\\n✨ Installation terminée !")

class SQLiteHelper:
    def __init__(self):
        self.success_style = """
        <div style="background: linear-gradient(90deg, #2196F3, #0D47A1); color: white; padding: 15px; border-radius: 10px; margin: 10px 0; text-align: center; font-weight: bold; font-size: 16px;">
            🗄️ {message} 🗄️
        </div>
        """
        self.db_name = "entreprise.db"
        
        # Base de données des aides cachées
        self.helps = {
            "4.1.1": {
                "hint": "Utilisez sqlite3.connect('nom_db.db') pour créer la connexion. N'oubliez pas le .close()",
                "solution": """# Créer une connexion à la base de données
conn = sqlite3.connect('entreprise.db')
cursor = conn.cursor()

print("✅ Connexion à la base de données établie")
print(f"📁 Fichier de base de données: {os.path.abspath('entreprise.db')}")

# N'oubliez pas de fermer la connexion à la fin
# conn.close()""",
                "explanation": "sqlite3.connect() crée une connexion à une base SQLite. Si le fichier n'existe pas, il sera créé."
            },
            "4.1.2": {
                "hint": "Utilisez CREATE TABLE avec les colonnes et leurs types (INTEGER, TEXT, REAL). PRIMARY KEY pour l'ID.",
                "solution": """# Créer la table employes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        departement TEXT NOT NULL,
        salaire REAL NOT NULL,
        date_embauche DATE
    )
''')

# Valider les changements
conn.commit()
print("✅ Table 'employes' créée avec succès")""",
                "explanation": "CREATE TABLE définit la structure. IF NOT EXISTS évite les erreurs si la table existe déjà."
            },
            "4.2.1": {
                "hint": "Utilisez INSERT INTO table (colonnes) VALUES (valeurs). Plusieurs façons: une ligne ou plusieurs.",
                "solution": """# Insérer des données d'exemple
employes_data = [
    ('Alice Martin', 'IT', 45000, '2023-01-15'),
    ('Bob Dupont', 'RH', 38000, '2022-11-03'),
    ('Charlie Dubois', 'Finance', 52000, '2023-03-20'),
    ('Diana Moreau', 'Marketing', 41000, '2022-09-12'),
    ('Eve Laurent', 'IT', 48000, '2023-02-08')
]

cursor.executemany('''
    INSERT INTO employes (nom, departement, salaire, date_embauche)
    VALUES (?, ?, ?, ?)
''', employes_data)

conn.commit()
print(f"✅ {len(employes_data)} employés ajoutés à la base de données")""",
                "explanation": "INSERT INTO ajoute des données. executemany() permet d'insérer plusieurs lignes efficacement."
            },
            "4.2.2": {
                "hint": "Utilisez SELECT avec WHERE pour filtrer. Exemples: WHERE salaire > 40000, WHERE departement = 'IT'",
                "solution": """# Différentes requêtes SELECT
print("👥 TOUS LES EMPLOYÉS:")
cursor.execute("SELECT * FROM employes")
tous_employes = cursor.fetchall()
for emp in tous_employes:
    print(f"  {emp}")

print("\\n💰 EMPLOYÉS BIEN PAYÉS (> 45000):")
cursor.execute("SELECT nom, salaire FROM employes WHERE salaire > 45000")
bien_payes = cursor.fetchall()
for emp in bien_payes:
    print(f"  {emp[0]}: {emp[1]}€")

print("\\n💻 EMPLOYÉS IT:")
cursor.execute("SELECT nom, salaire FROM employes WHERE departement = 'IT'")
it_employes = cursor.fetchall()
for emp in it_employes:
    print(f"  {emp[0]}: {emp[1]}€")""",
                "explanation": "SELECT récupère les données. WHERE filtre selon des conditions. fetchall() récupère tous les résultats."
            },
            "4.3.1": {
                "hint": "Utilisez UPDATE SET colonne = valeur WHERE condition. N'oubliez pas le WHERE !",
                "solution": """# Augmenter les salaires du département IT de 5%
cursor.execute('''
    UPDATE employes 
    SET salaire = salaire * 1.05 
    WHERE departement = 'IT'
''')

rows_affected = cursor.rowcount
conn.commit()

print(f"✅ {rows_affected} salaires augmentés de 5% dans le département IT")

# Vérifier les changements
cursor.execute("SELECT nom, salaire FROM employes WHERE departement = 'IT'")
nouveaux_salaires = cursor.fetchall()
print("\\n💻 Nouveaux salaires IT:")
for emp in nouveaux_salaires:
    print(f"  {emp[0]}: {emp[1]:.2f}€")""",
                "explanation": "UPDATE modifie les données existantes. rowcount indique combien de lignes ont été affectées."
            },
            "4.3.2": {
                "hint": "Utilisez DELETE FROM table WHERE condition. Attention: sans WHERE, toutes les lignes sont supprimées !",
                "solution": """# Supprimer les employés avec un salaire < 40000
cursor.execute("DELETE FROM employes WHERE salaire < 40000")
rows_deleted = cursor.rowcount
conn.commit()

print(f"❌ {rows_deleted} employés supprimés (salaire < 40000€)")

# Voir les employés restants
cursor.execute("SELECT COUNT(*) FROM employes")
count = cursor.fetchone()[0]
print(f"👥 {count} employés restants dans la base")""",
                "explanation": "DELETE supprime des lignes selon une condition. Toujours utiliser WHERE pour éviter de vider la table."
            },
            "4.4.1": {
                "hint": "Créez des index avec CREATE INDEX nom_index ON table(colonne). IF NOT EXISTS évite les erreurs. EXPLAIN QUERY PLAN montre l'utilisation des index.",
                "solution": """# Créer des index pour optimiser les performances
cursor = conn.cursor()

# 1. Index sur département (requêtes fréquentes)
cursor.execute("CREATE INDEX IF NOT EXISTS idx_departement ON employes(departement)")

# 2. Index sur salaire (tri et filtres)
cursor.execute("CREATE INDEX IF NOT EXISTS idx_salaire ON employes(salaire)")

# 3. Index composite nom/prenom (recherches nominatives)
cursor.execute("CREATE INDEX IF NOT EXISTS idx_nom_prenom ON employes(nom, prenom)")

conn.commit()

# Test de performance - voir l'utilisation des index
cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM employes WHERE departement = 'IT'")
plan = cursor.fetchall()
print("📊 Plan d'exécution (avec index):")
for step in plan:
    print(f"  {step[3]}")

print("\n✅ Index créés et performance optimisée")
print("🔒 N'oubliez pas: conn.close() pour fermer la connexion")""",
                "explanation": "Les index accélèrent les recherches WHERE, ORDER BY et JOIN. Les index composés optimisent les requêtes multi-colonnes."
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
            <summary style="cursor: pointer; background: #e3f2fd; padding: 10px; border-radius: 3px; font-weight: bold; color: #1976d2;">
                💡 Conseil SQL (cliquer pour dérouler)
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
                🔍 Solution SQL (cliquer pour dérouler)
            </summary>
            <div style="padding: 15px; margin-top: 10px; background: white; border-radius: 3px;">
                <p><strong>🗄️ Explication :</strong> {help_data['explanation']}</p>
                <pre style="background: #f5f5f5; padding: 10px; border-radius: 3px; overflow-x: auto; border-left: 3px solid #2196f3;"><code>{help_data['solution']}</code></pre>
            </div>
        </details>
        """
        
        display(HTML(html_hint))
        display(HTML(html_solution))
    
    def solution(self, code, explanation=""):
        html = f"""
        <details style="margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; padding: 5px;">
            <summary style="cursor: pointer; background: #e3f2fd; padding: 10px; border-radius: 3px; font-weight: bold;">
                🔍 Solution SQL (cliquer pour révéler)
            </summary>
            <div style="background: #fafafa; padding: 15px; margin-top: 10px; border-radius: 3px;">
                {f'<p><strong>🗄️ Explication SQL:</strong> {explanation}</p>' if explanation else ''}
                <pre style="background: #f8f8f8; padding: 10px; border-radius: 3px; overflow-x: auto;"><code>{code}</code></pre>
            </div>
        </details>
        """
        display(HTML(html))
    
    def hint(self, text):
        html = f"""
        <details style="margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; padding: 5px;">
            <summary style="cursor: pointer; background: #e3f2fd; padding: 10px; border-radius: 3px; font-weight: bold;">
                💡 Conseil SQL (cliquer pour révéler)
            </summary>
            <div style="background: #f3f9ff; padding: 15px; margin-top: 10px; border-radius: 3px;">
                {text}
            </div>
        </details>
        """
        display(HTML(html))
    
    def success(self, message):
        html = self.success_style.format(message=message)
        display(HTML(html))
        
    def check_db_connection(self):
        """Vérifie la connexion à la base de données"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            conn.close()
            return True, [table[0] for table in tables]
        except Exception as e:
            return False, str(e)
    
    def check_table_exists(self, table_name):
        """Vérifie si une table existe"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (table_name,))
            result = cursor.fetchone()
            conn.close()
            return result is not None
        except Exception:
            return False
    
    def check_connection_button(self):
        """Bouton pour vérifier la connexion à la base"""
        output = widgets.Output()
        button = widgets.Button(
            description="🔗 Vérifier Connexion",
            button_style='info',
            layout=widgets.Layout(width='200px', height='35px')
        )
        
        def on_click(b):
            with output:
                output.clear_output()
                success, result = self.check_db_connection()
                if success:
                    print("✅ Connexion réussie à la base de données")
                    print(f"📁 Base: {self.db_name}")
                    if result:
                        print(f"📋 Tables: {', '.join(result)}")
                    else:
                        print("📋 Aucune table trouvée")
                else:
                    print(f"❌ Erreur de connexion: {result}")
        
        button.on_click(on_click)
        display(widgets.VBox([button, output]))
    
    def check_table_button(self, table_name):
        """Bouton pour vérifier l'existence d'une table"""
        output = widgets.Output()
        button = widgets.Button(
            description=f"📋 Vérifier {table_name}",
            button_style='warning',
            layout=widgets.Layout(width='200px', height='35px')
        )
        
        def on_click(b):
            with output:
                output.clear_output()
                if self.check_table_exists(table_name):
                    print(f"✅ Table '{table_name}' existe")
                    
                    # Compter les enregistrements
                    try:
                        conn = sqlite3.connect(self.db_name)
                        cursor = conn.cursor()
                        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                        count = cursor.fetchone()[0]
                        print(f"📊 {count} enregistrements")
                        
                        # Montrer la structure
                        cursor.execute(f"PRAGMA table_info({table_name})")
                        columns = cursor.fetchall()
                        print("🏗️ Structure:")
                        for col in columns:
                            print(f"  - {col[1]} ({col[2]})")
                        conn.close()
                    except Exception as e:
                        print(f"⚠️ Erreur lors de la vérification: {e}")
                else:
                    print(f"❌ Table '{table_name}' n'existe pas")
        
        button.on_click(on_click)
        display(widgets.VBox([button, output]))

def load_sqlite_helper():
    """Charge le système d'aide SQLite."""
    if 'sqlite_helper' not in get_ipython().user_ns:
        helper = SQLiteHelper()
        get_ipython().user_ns['sqlite_helper'] = helper
        print("🗄️ Système d'aide SQLite chargé !")
        print("✨ Prêt pour les bases de données relationnelles !")
    else:
        print("✅ Le système d'aide SQLite est déjà chargé.")