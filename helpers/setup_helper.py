
import subprocess
import sys
import ipywidgets as widgets
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from IPython.display import HTML, display
from IPython import get_ipython

def install_packages():
    """Installe les packages nécessaires pour le notebook."""
    packages = [
        "pandas>=1.5.0",
        "numpy>=1.20.0", 
        "ipywidgets>=7.6.0",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.0"
    ]
    
    print("🚀 Démarrage de l'installation des packages...")
    print("Cette opération peut prendre quelques instants.")
    
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
            print(f"✅ {package} installé.")
        except subprocess.CalledProcessError:
            print(f"❌ Erreur lors de l'installation de {package}.")
            
    print("\\n✨ Installation terminée !")
    print("Si vous rencontrez des problèmes, essayez de redémarrer le noyau (Kernel).")

class PandasHelper:
    def __init__(self):
        self.success_style = """
        <div style="background: linear-gradient(90deg, #4CAF50, #45a049); color: white; padding: 15px; border-radius: 10px; margin: 10px 0; text-align: center; font-weight: bold; font-size: 16px;">
            🎉 {message} 🎉
        </div>
        """
        # Base de données des aides cachées
        self.helps = {
            "2.1.1": {
                "hint": "Utilisez des list comprehensions pour les valeurs aléatoires : [random.randint(min, max) for _ in range(10)]",
                "solution": """noms = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry', 'Iris', 'Jack']
departements = ['IT', 'RH', 'Finance', 'Marketing', 'Ventes'] * 2
salaires = [random.randint(30000, 80000) for _ in range(10)]
ages = [random.randint(22, 60) for _ in range(10)]""",
                "explanation": "Les départements sont multipliés par 2 pour avoir 10 éléments. Les list comprehensions génèrent des valeurs aléatoires."
            },
            "2.1.2": {
                "hint": "Syntaxe : df_employes = pd.DataFrame({'colonne1': liste1, 'colonne2': liste2, ...})",
                "solution": """df_employes = pd.DataFrame({
    'nom': noms,
    'departement': departements,
    'salaire': salaires,
    'age': ages
})""",
                "explanation": "pd.DataFrame() crée un tableau 2D. Chaque clé du dictionnaire devient une colonne."
            },
            "2.1.3": {
                "hint": "Utilisez .head(), .info(), .describe(), .shape sur votre DataFrame",
                "solution": """# Explorer le DataFrame
print("🔍 Premières lignes:")
print(df_employes.head())

print("\\n📊 Informations générales:")
print(df_employes.info())

print("\\n📈 Statistiques descriptives:")
print(df_employes.describe())

print("\\n📏 Dimensions:")
print(f"Forme: {df_employes.shape}")""",
                "explanation": ".head() montre les premières lignes, .info() les types, .describe() les statistiques, .shape la taille."
            },
            "2.2.1": {
                "hint": "Pour une colonne: df['nom_colonne']. Pour plusieurs: df[['col1', 'col2']]",
                "solution": """# Sélection d'une seule colonne (Series)
noms_seuls = df_employes['nom']

# Sélection d'une colonne avec DataFrame
salaires_seuls = df_employes[['salaire']]

# Sélection de plusieurs colonnes
nom_salaire = df_employes[['nom', 'salaire']]""",
                "explanation": "Une colonne retourne une Series, plusieurs colonnes retournent un DataFrame."
            },
            "2.2.2": {
                "hint": "Utilisez les opérateurs de comparaison : >, <, ==, !=. Combinez avec & (et) et | (ou)",
                "solution": """# Filtres simples
employes_bien_payes = df_employes[df_employes['salaire'] > 45000]
employes_jeunes = df_employes[df_employes['age'] < 30]

# Filtres par catégorie
employes_it = df_employes[df_employes['departement'] == 'IT']

# Filtres combinés (attention aux parenthèses !)
seniors_it = df_employes[(df_employes['age'] > 35) & (df_employes['departement'] == 'IT')]""",
                "explanation": "Les filtres pandas utilisent des conditions booléennes. Utilisez & pour 'et', | pour 'ou'."
            },
            "2.3.1": {
                "hint": "Utilisez .groupby('colonne').agg({'autre_colonne': ['mean', 'sum', 'count']})",
                "solution": """# Analyse par département
stats_par_dept = df_employes.groupby('departement').agg({
    'salaire': ['mean', 'min', 'max', 'count'],
    'age': ['mean', 'min', 'max']
}).round(2)

# Salaire moyen par département (Series)
salaire_moyen_dept = df_employes.groupby('departement')['salaire'].mean()""",
                "explanation": "groupby() groupe les données. agg() applique des fonctions d'agrégation à chaque groupe."
            }
        }
        
        # Templates vierges pour le reset
        self.templates = {
            "2.1.1": """# 📝 ÉTAPE 2.1.1 : Données d'employés
# Créez ces 4 listes avec 10 éléments chacune :
# 1. noms : liste de prénoms
# 2. departements : 5 départements répétés (IT, RH, Finance, Marketing, Ventes)
# 3. salaires : salaires aléatoires entre 30000 et 80000
# 4. ages : âges aléatoires entre 22 et 60

# Exemple pour salaires aléatoires :
# salaires = [random.randint(30000, 80000) for _ in range(10)]

# 👇 Créez vos 4 listes ici :""",
            
            "2.1.2": """# 📝 ÉTAPE 2.1.2 : DataFrame principal
# Créez un DataFrame 'df_employes' avec pd.DataFrame()
# Utilisez un dictionnaire pour associer noms de colonnes et listes :
# {
#     'nom': noms,
#     'departement': departements,
#     'salaire': salaires,
#     'age': ages
# }

# 👇 Créez votre DataFrame ici :""",
            
            "2.1.3": """# 📝 ÉTAPE 2.1.3 : Exploration
# Utilisez ces méthodes sur df_employes :
# 1. .head() - premières lignes
# 2. .info() - informations générales
# 3. .describe() - statistiques
# 4. .shape - forme (pas de parenthèses)

print("🔍 EXPLORATION DU DATAFRAME")
print("="*35)

# 👇 Ajoutez vos explorations ici :""",
            
            "2.2.1": """# 📝 ÉTAPE 2.2.1 : Sélections de colonnes
# Créez ces 3 variables :
# 1. noms_seuls = sélection de la colonne 'nom' uniquement
# 2. salaires_seuls = sélection de la colonne 'salaire' uniquement  
# 3. nom_salaire = sélection des colonnes 'nom' ET 'salaire'

# Syntaxe :
# Une colonne : df['colonne']
# Plusieurs colonnes : df[['col1', 'col2']]

# 👇 Créez vos sélections ici :""",
            
            "2.2.2": """# 📝 ÉTAPE 2.2.2 : Filtres conditionnels
# Créez ces 4 DataFrames filtrés :
# 1. employes_bien_payes = salaire > 50000
# 2. employes_jeunes = age < 30
# 3. employes_it = departement == 'IT'
# 4. seniors_it = (age > 40) ET (departement == 'IT')

# Syntaxe :
# df[df['colonne'] > valeur]
# df[(condition1) & (condition2)]  # ET
# df[(condition1) | (condition2)]  # OU

# 👇 Créez vos filtres ici :""",
            
            "2.3.1": """# 📝 ÉTAPE 2.3.1 : Groupement par département
# Créez ces analyses :
# 1. stats_par_dept = df_employes.groupby('departement').agg({
#        'salaire': ['mean', 'min', 'max', 'count'],
#        'age': 'mean'
#    })
# 
# 2. salaire_moyen_dept = df_employes.groupby('departement')['salaire'].mean()

# 👇 Créez vos analyses ici :"""
        }

    def _get_namespace(self):
        """Retourne le namespace utilisateur de Jupyter pour accéder aux variables du notebook."""
        try:
            ip = get_ipython()
            if ip is not None and hasattr(ip, 'user_ns'):
                return ip.user_ns
        except Exception:
            pass
        # Fallback minimal
        return globals()

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
                💡 Conseil (cliquer pour dérouler)
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
                🔍 Solution (cliquer pour dérouler)
            </summary>
            <div style="padding: 15px; margin-top: 10px; background: white; border-radius: 3px;">
                <p><strong>💡 Explication :</strong> {help_data['explanation']}</p>
                <pre style="background: #f5f5f5; padding: 10px; border-radius: 3px; overflow-x: auto; border-left: 3px solid #4caf50;"><code>{help_data['solution']}</code></pre>
            </div>
        </details>
        """
        
        display(HTML(html_hint))
        display(HTML(html_solution))

    def auto_reset_toolbar(self):
        """Affiche une barre d'outils avec tous les resets disponibles"""
        print("🔧 BARRE D'OUTILS DE RESET AUTOMATIQUE")
        print("="*50)
        
        # Créer une grille de boutons
        buttons = []
        outputs = []
        
        for step in sorted(self.templates.keys()):
            output = widgets.Output()
            button = widgets.Button(
                description=f"🔄 {step}",
                button_style='danger',
                layout=widgets.Layout(width='120px', height='30px', margin='2px')
            )
            
            def make_click_handler(step_id, template, out):
                def on_click(b):
                    with out:
                        out.clear_output()
                        print(f"📋 Code vierge pour l'étape {step_id} :")
                        print("="*40)
                        print(template)
                        print("="*40)
                        print("💡 Copiez-collez ce code dans la cellule d'exercice !")
                return on_click
            
            button.on_click(make_click_handler(step, self.templates[step], output))
            buttons.append(button)
            outputs.append(output)
        
        # Afficher en grille 3x2
        row1 = widgets.HBox(buttons[:3])
        row2 = widgets.HBox(buttons[3:])
        grid = widgets.VBox([row1, row2])
        
        # Zone d'affichage commune
        main_output = widgets.Output()
        
        # Interface complète
        ui = widgets.VBox([
            widgets.HTML("<h4>🎯 Cliquez sur une étape pour obtenir son code vierge :</h4>"),
            grid,
            widgets.HTML("<hr>"),
            *outputs
        ])
        
        display(ui)

    def reset_button(self, step):
        """Affiche un bouton pour remettre l'exercice à l'état vierge"""
        if step not in self.templates:
            print(f"❌ Template non trouvé pour l'étape {step}")
            return
        
        output = widgets.Output()
        button = widgets.Button(
            description=f"🔄 Reset {step}",
            button_style='danger',
            layout=widgets.Layout(width='150px', height='35px')
        )
        
        def on_click(b):
            with output:
                output.clear_output()
                print(f"📋 Code vierge pour l'étape {step} :")
                print("="*50)
                print(self.templates[step])
                print("="*50)
                print("💡 Copiez-collez ce code dans la cellule d'exercice pour recommencer à zéro !")
        
        button.on_click(on_click)
        display(widgets.VBox([button, output]))
    
    def solution(self, code, explanation=""):
        html = f"""
        <details style="margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; padding: 5px;">
            <summary style="cursor: pointer; background: #f0f8ff; padding: 10px; border-radius: 3px; font-weight: bold;">
                🔍 Solution (cliquer pour révéler)
            </summary>
            <div style="background: #fafafa; padding: 15px; margin-top: 10px; border-radius: 3px;">
                {f'<p><strong>💡 Explication:</strong> {explanation}</p>' if explanation else ''}
                <pre style="background: #f8f8f8; padding: 10px; border-radius: 3px; overflow-x: auto;"><code>{code}</code></pre>
            </div>
        </details>
        """
        display(HTML(html))
    
    def hint(self, text):
        html = f"""
        <details style="margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; padding: 5px;">
            <summary style="cursor: pointer; background: #fff3e0; padding: 10px; border-radius: 3px; font-weight: bold;">
                💡 Conseil (cliquer pour révéler)
            </summary>
            <div style="background: #fffdf7; padding: 15px; margin-top: 10px; border-radius: 3px;">
                {text}
            </div>
        </details>
        """
        display(HTML(html))
    
    def _check_dataframe(self, df_name, min_rows=None, required_columns=None):
        try:
            ns = self._get_namespace()
            df = ns.get(df_name)
            
            if df is None:
                return False, f"❌ DataFrame '{df_name}' non trouvé (exécutez d'abord la cellule qui le crée)"
            
            if not isinstance(df, pd.DataFrame):
                return False, f"❌ '{df_name}' n'est pas un DataFrame pandas"
            
            if min_rows and len(df) < min_rows:
                return False, f"❌ DataFrame trop petit: {len(df)} lignes (minimum: {min_rows})"
            
            if required_columns:
                missing = [col for col in required_columns if col not in df.columns]
                if missing:
                    return False, f"❌ Colonnes manquantes: {missing}"
            
            info = f"✅ DataFrame '{df_name}': {df.shape[0]} lignes × {df.shape[1]} colonnes"
            if required_columns:
                info += f"\\n✅ Colonnes: {list(df.columns)}"
            
            return True, info
            
        except Exception as e:
            return False, f"❌ Erreur: {e}"
    
    def _check_variable(self, var_name, expected_type=None, min_length=None):
        try:
            ns = self._get_namespace()
            var = ns.get(var_name)
            
            if var is None:
                return False, f"❌ Variable '{var_name}' non trouvée (exécutez d'abord la cellule qui la crée)"
            
            if expected_type and not isinstance(var, expected_type):
                return False, f"❌ Type incorrect: attendu {expected_type.__name__}, reçu {type(var).__name__}"
            
            if min_length and hasattr(var, '__len__') and len(var) < min_length:
                return False, f"❌ Trop petit: {len(var)} éléments (minimum: {min_length})"
            
            return True, f"✅ Variable '{var_name}' correcte ! Type: {type(var).__name__}, Taille: {len(var) if hasattr(var, '__len__') else 'N/A'}"
            
        except Exception as e:
            return False, f"❌ Erreur: {e}"
    
    def check_df_button(self, df_name, min_rows=None, required_columns=None):
        output = widgets.Output()
        button = widgets.Button(
            description=f"📊 Vérifier {df_name}",
            button_style='primary',
            layout=widgets.Layout(width='220px', height='35px')
        )
        
        def on_click(b):
            with output:
                output.clear_output()
                success, message = self._check_dataframe(df_name, min_rows, required_columns)
                if success:
                    print(f"🎉 {message}")
                else:
                    print(message)
        
        button.on_click(on_click)
        display(widgets.VBox([button, output]))
    
    def check_var_button(self, var_name, expected_type=None, min_length=None):
        output = widgets.Output()
        button = widgets.Button(
            description=f"🔍 Vérifier {var_name}",
            button_style='info',
            layout=widgets.Layout(width='200px', height='35px')
        )
        
        def on_click(b):
            with output:
                output.clear_output()
                success, message = self._check_variable(var_name, expected_type, min_length)
                if success:
                    print(f"🎉 {message}")
                else:
                    print(message)
        
        button.on_click(on_click)
        display(widgets.VBox([button, output]))
    
    def success(self, message):
        html = self.success_style.format(message=message)
        display(HTML(html))
    
    def demo_button(self, demo_func, button_text="🎬 Voir la démonstration"):
        output = widgets.Output()
        button = widgets.Button(
            description=button_text,
            button_style='warning',
            layout=widgets.Layout(width='250px', height='35px')
        )
        
        def on_click(b):
            with output:
                output.clear_output()
                demo_func()
        
        button.on_click(on_click)
        display(widgets.VBox([button, output]))

def load_helper():
    """Charge le système d'aide et l'assigne à une variable globale."""
    if 'pandas_helper' not in get_ipython().user_ns:
        helper = PandasHelper()
        get_ipython().user_ns['pandas_helper'] = helper
        print("📊 Système d'aide Pandas chargé !")
        print("✨ L'objet `pandas_helper` est maintenant disponible.")
    else:
        print("✅ Le système d'aide est déjà chargé.")

