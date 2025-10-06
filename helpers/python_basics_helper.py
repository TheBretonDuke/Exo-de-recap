#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Système d'aide pour les exercices Python de base
Version simplifiée sans boucles infinies
"""

import subprocess
import sys

# Imports conditionnels pour Jupyter
try:
    import ipywidgets as widgets
    from IPython.display import HTML, display
    JUPYTER_AVAILABLE = True
except ImportError:
    JUPYTER_AVAILABLE = False
    # Fonctions de remplacement pour le mode console
    def display(content):
        print(content)
    
    class HTML:
        def __init__(self, content):
            self.content = content

def install_python_basics_packages():
    """Installe les packages nécessaires pour le notebook Python basique."""
    packages = ["ipywidgets>=7.6.0"]
    
    print("🚀 Installation des packages pour Python...")
    print("📝 Note: Les modules de base Python ne nécessitent pas d'installation")
    
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✅ {package} installé avec succès")
        except subprocess.CalledProcessError:
            print(f"❌ Erreur lors de l'installation de {package}")
    
    print("\n✨ Installation terminée ! Vous pouvez maintenant continuer les exercices.")

class PythonBasicsHelper:
    """Système d'aide pour les exercices Python de base"""
    
    def __init__(self):
        self.helps = {
            "1.1.1": {
                "hint": "Une chaîne de caractères utilise des guillemets : nom = 'Pierre' ou nom = \"Pierre\"",
                "solution": "nom = 'Pierre'  # Une chaîne de caractères (string)",
                "explanation": "En Python, on peut utiliser des guillemets simples ' ou doubles \" pour créer une chaîne."
            },
            "1.1.2": {
                "hint": "Un nombre entier s'écrit sans guillemets : age = 25",
                "solution": "age = 25  # Un nombre entier (int)",
                "explanation": "Les nombres entiers (int) s'écrivent directement sans guillemets. Python les reconnaît automatiquement."
            },
            "1.1.3": {
                "hint": "Un nombre décimal utilise un point : salaire = 45000.50",
                "solution": "salaire = 45000.50  # Un nombre décimal (float)",
                "explanation": "En Python, on utilise le point (.) pour séparer les décimales, jamais la virgule."
            },
            "1.1.4": {
                "hint": "Une liste se crée avec des crochets : competences = ['Python', 'SQL', 'Docker', 'MongoDB', 'Git']",
                "solution": "competences = ['Python', 'SQL', 'Docker', 'MongoDB', 'Git']",
                "explanation": "Une liste (list) contient plusieurs éléments entre crochets, séparés par des virgules."
            },
            "1.1.5": {
                "hint": "Un dictionnaire utilise des accolades et des clés : profil = {'nom': nom, 'age': age, ...}",
                "solution": """profil = {
    "nom": nom,
    "age": age,
    "salaire": salaire,
    "competences": competences
}""",
                "explanation": "Un dictionnaire (dict) associe des clés à des valeurs. On peut utiliser nos variables comme valeurs."
            },
            "1.2.1": {
                "hint": "Utilisez if/elif/else avec les comparaisons < et >=. Python teste les conditions dans l'ordre.",
                "solution": """def categoriser_age(age):
    if age < 13:
        return "Enfant"
    elif age < 18:
        return "Adolescent"
    elif age < 65:
        return "Adulte"
    else:
        return "Senior""",
                "explanation": "'elif' (else if) permet de tester plusieurs conditions. Python teste dans l'ordre et s'arrête à la première vraie."
            },
            "1.2.2": {
                "hint": "Créez d'abord la liste : ages_test = [10, 15, 25, 45, 70], puis utilisez : for age in ages_test:",
                "solution": """ages_test = [10, 15, 25, 45, 70]

for age in ages_test:
    categorie = categoriser_age(age)
    print(f"Age {age} est un(e) {categorie}")""",
                "explanation": "Une boucle 'for' itère sur chaque élément d'une liste. On peut utiliser le résultat de la fonction dans la boucle."
            },
            "1.3.1": {
                "hint": "Utilisez append() pour ajouter, insert(position, élément) pour insérer, remove() pour supprimer, sort() pour trier.",
                "solution": """# 1. Ajouter à la fin
competences.append("Machine Learning")

# 2. Insérer à la position 2
competences.insert(2, "React")

# 3. Supprimer un élément
competences.remove("Git")  # ou competences.pop()

# 4. Trier alphabétiquement
competences.sort()

# 5. Liste avec compétences de plus de 5 caractères
competences_longues = [comp for comp in competences if len(comp) > 5]

print("🔧 Liste modifiée :", competences)
print("📏 Compétences longues :", competences_longues)""",
                "explanation": "Les listes ont des méthodes pour les modifier. List comprehension : [expression for item in liste if condition]."
            },
            "1.3.2": {
                "hint": "Utilisez dict[clé] = valeur pour ajouter, dict.update() pour fusionner, dict.items() pour parcourir.",
                "solution": """# 1. Ajouter expérience
profil["experience"] = 3

# 2. Ajouter langues
profil["langues"] = ["Français", "Anglais", "Espagnol"]

# 3. Augmenter salaire de 10%
profil["salaire"] = profil["salaire"] * 1.10

# 4. Créer dictionnaire contact
contact = {
    "email": "contact@example.com",
    "telephone": "06.12.34.56.78",
    "ville": "Paris"
}

# 5. Fusionner dans profil
profil.update(contact)

print("📋 Profil enrichi :")
for cle, valeur in profil.items():
    print(f"  {cle}: {valeur}")""",
                "explanation": "update() fusionne deux dictionnaires. items() retourne les paires clé-valeur pour l'itération."
            },
            "1.4.1": {
                "hint": "Utilisez isinstance(variable, (int, float)) pour vérifier le type. Gérez ZeroDivisionError pour la division par zéro.",
                "solution": """def division_securisee(a, b):
    try:
        # Vérification des types
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return "❌ Erreur : Les arguments doivent être des nombres"
        
        # Division
        resultat = a / b
        return f"✅ Résultat : {resultat}"
        
    except ZeroDivisionError:
        return "❌ Erreur : Division par zéro impossible"
    except Exception as e:
        return f"❌ Erreur inattendue : {e}"

# Tests
print(division_securisee(10, 2))      # ✅ Résultat : 5.0
print(division_securisee(10, 0))      # ❌ Erreur : Division par zéro
print(division_securisee("10", 2))    # ❌ Erreur : Types incorrects""",
                "explanation": "try/except capture les erreurs. isinstance() vérifie le type. Gérez spécifiquement chaque type d'erreur."
            },
            "1.5.1": {
                "hint": "Importez avec import, from...import, ou import...as. Utilisez datetime.now(), random.randint(), math.sqrt().",
                "solution": """# 1. datetime - Date et heure
import datetime
maintenant = datetime.datetime.now()
print(f"📅 Date/heure actuelles : {maintenant.strftime('%d/%m/%Y %H:%M:%S')}")

# 2. random - Nombres aléatoires
from random import randint
nombres_aleatoires = [randint(1, 100) for _ in range(5)]
print(f"🎲 5 nombres aléatoires : {nombres_aleatoires}")

# 3. math - Fonctions mathématiques
import math as m
racine = m.sqrt(16)
logarithme = m.log(16)
print(f"🔢 √16 = {racine}, ln(16) = {logarithme:.2f}")

# 4. os - Système d'exploitation
from os import getcwd
repertoire = getcwd()
print(f"📁 Répertoire actuel : {repertoire}")""",
                "explanation": "Chaque module offre des fonctionnalités spécialisées. Différentes syntaxes d'import pour différents besoins."
            },
            "1.6.1": {
                "hint": "Une classe définit un modèle. __init__ est le constructeur. self fait référence à l'instance courante.",
                "solution": """class Employe:
    def __init__(self, nom, prenom, salaire, departement):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.departement = departement
    
    def se_presenter(self):
        print(f"👋 Je suis {self.prenom} {self.nom}")
        print(f"💼 Département : {self.departement}")
        print(f"💰 Salaire : {self.salaire}€")
    
    def augmentation(self, pourcentage):
        ancien_salaire = self.salaire
        self.salaire = self.salaire * (1 + pourcentage/100)
        print(f"📈 Augmentation de {pourcentage}% : {ancien_salaire}€ → {self.salaire}€")
    
    def changer_departement(self, nouveau_dept):
        ancien_dept = self.departement
        self.departement = nouveau_dept
        print(f"🔄 Changement : {ancien_dept} → {nouveau_dept}")

# Test de la classe
emp1 = Employe("Dupont", "Marie", 45000, "IT")
emp1.se_presenter()
emp1.augmentation(10)
emp1.changer_departement("DevOps")""",
                "explanation": "class définit une classe. __init__ initialise les attributs. self représente l'instance. Les méthodes agissent sur l'objet."
            }
        }
    
    def help(self, step):
        """Affiche l'aide pour une étape donnée"""
        if step not in self.helps:
            print(f"❌ Aide non trouvée pour l'étape {step}")
            return
            
        help_data = self.helps[step]
        
        if JUPYTER_AVAILABLE:
            # Version Jupyter avec HTML
            html_hint = f"""
            <details style="margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; padding: 5px; background: #f9f9f9;">
                <summary style="cursor: pointer; background: #fff3e0; padding: 10px; border-radius: 3px; font-weight: bold; color: #f57c00;">
                    💡 Conseil Python (cliquer pour dérouler)
                </summary>
                <div style="padding: 15px; margin-top: 10px; background: white; border-radius: 3px;">
                    <p style="margin: 0; color: #333;">{help_data['hint']}</p>
                </div>
            </details>
            """
            
            html_solution = f"""
            <details style="margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; padding: 5px; background: #f9f9f9;">
                <summary style="cursor: pointer; background: #e8f5e8; padding: 10px; border-radius: 3px; font-weight: bold; color: #2e7d32;">
                    🔍 Solution Python (cliquer pour dérouler)
                </summary>
                <div style="padding: 15px; margin-top: 10px; background: white; border-radius: 3px;">
                    <p><strong>🐍 Explication :</strong> {help_data['explanation']}</p>
                    <pre style="background: #f5f5f5; padding: 10px; border-radius: 3px; overflow-x: auto; border-left: 3px solid #ff9800;"><code>{help_data['solution']}</code></pre>
                </div>
            </details>
            """
            
            display(HTML(html_hint))
            display(HTML(html_solution))
        else:
            # Version console
            print("💡 Conseil:", help_data['hint'])
            print("🔍 Solution:")
            print(help_data['solution'])
            print("📝 Explication:", help_data['explanation'])
    
    def solution(self, code, explanation=""):
        """Affiche une solution"""
        if JUPYTER_AVAILABLE:
            html = f"""
            <details style="margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; padding: 5px;">
                <summary style="cursor: pointer; background: #fff3e0; padding: 10px; border-radius: 3px; font-weight: bold;">
                    🔍 Solution Python (cliquer pour révéler)
                </summary>
                <div style="background: #fafafa; padding: 15px; margin-top: 10px; border-radius: 3px;">
                    {f'<p><strong>🐍 Explication Python:</strong> {explanation}</p>' if explanation else ''}
                    <pre style="background: #f8f8f8; padding: 10px; border-radius: 3px; overflow-x: auto;"><code>{code}</code></pre>
                </div>
            </details>
            """
            display(HTML(html))
        else:
            print("🔍 Solution Python:")
            if explanation:
                print(f"🐍 Explication: {explanation}")
            print(code)
    
    def hint(self, text):
        """Affiche un conseil"""
        if JUPYTER_AVAILABLE:
            html = f"""
            <details style="margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; padding: 5px;">
                <summary style="cursor: pointer; background: #fff3e0; padding: 10px; border-radius: 3px; font-weight: bold;">
                    💡 Conseil Python (cliquer pour révéler)
                </summary>
                <div style="background: #fffef7; padding: 15px; margin-top: 10px; border-radius: 3px;">
                    {text}
                </div>
            </details>
            """
            display(HTML(html))
        else:
            print(f"💡 Conseil: {text}")
    
    def success(self, message):
        """Affiche un message de succès"""
        if JUPYTER_AVAILABLE:
            html = f"""
            <div style="background: linear-gradient(90deg, #FF9800, #F57C00); color: white; padding: 15px; border-radius: 10px; margin: 10px 0; text-align: center; font-weight: bold; font-size: 16px;">
                🐍 {message} 🐍
            </div>
            """
            display(HTML(html))
        else:
            print(f"🎉 {message} 🎉")

# Chargement automatique
print("🚀 Chargement du système d'aide Python...")
helper = PythonBasicsHelper()

# Création des boutons seulement dans Jupyter
if JUPYTER_AVAILABLE:
    # Bouton d'installation
    install_output = widgets.Output()
    install_button = widgets.Button(
        description="📦 Installer packages",
        button_style='info',
        tooltip="Installe les dépendances nécessaires",
        icon='download',
        layout=widgets.Layout(width='250px', height='40px')
    )

    def on_install_click(b):
        with install_output:
            install_output.clear_output()
            install_python_basics_packages()

    install_button.on_click(on_install_click)

    print("🎯 Système d'aide Python chargé avec succès !")
    print("📚 Fonctions disponibles:")
    print("  • helper.help('1.1.1') - Aide pour une étape spécifique")
    print("  • helper.solution('code') - Afficher une solution")
    print("  • helper.hint('conseil') - Afficher un conseil")

    display(widgets.VBox([install_button, install_output]))
else:
    print("📚 Système d'aide Python chargé (mode console)")
    print("✨ Utilisez helper.help('1.1.1') pour obtenir de l'aide")