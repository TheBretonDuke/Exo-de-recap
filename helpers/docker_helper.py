import subprocess
import os

# Détection sécurisée de Jupyter (si disponible)
try:
    from IPython.display import HTML, display
    from IPython import get_ipython
    JUPYTER_AVAILABLE = get_ipython() is not None
except Exception:
    JUPYTER_AVAILABLE = False

    # Fallback minimal pour l'affichage en mode console
    class HTML:
        def __init__(self, data):
            self.data = data

    def display(html_obj):
        # En mode console, on n'affiche pas le HTML
        print()  # noop placeholder


def install_docker_packages():
    """Informer sur les dépendances nécessaires (ne pas forcer d'installations)."""
    print("📝 Vérifiez que 'ipywidgets' et 'requests' sont installés dans votre environnement Jupyter si vous utilisez l'interface HTML.")
    print("� Note: Docker lui-même doit être installé séparément (Docker Desktop).")

class DockerHelper:
    def __init__(self):
        self.success_style = """
        <div style="background: linear-gradient(90deg, #0db7ed, #003d6b); color: white; padding: 15px; border-radius: 10px; margin: 10px 0; text-align: center; font-weight: bold; font-size: 16px;">
            🐳 {message} 🐳
        </div>
        """
        
        # Base de données des aides cachées pour Docker
        self.helps = {
            "5.1.1": {
                "hint": "Vérifiez l'installation avec `docker --version` et testez avec `docker run hello-world`.",
                "solution": """# Vérifier l'installation Docker
import subprocess

try:
    result = subprocess.run(['docker', '--version'], capture_output=True, text=True)
    print(f"✅ Docker installé: {result.stdout.strip()}")
    print("\n🚀 Test avec hello-world...")
    result = subprocess.run(['docker', 'run', 'hello-world'], capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ Docker fonctionne correctement!")
    else:
        print(f"❌ Erreur: {result.stderr}")
except FileNotFoundError:
    print("❌ Docker n'est pas installé ou pas dans le PATH")
    print("💡 Installez Docker Desktop depuis https://docker.com")
""",
                "explanation": "`docker --version` vérifie l'installation. `docker run hello-world` teste le fonctionnement de base."
            },
            "5.1.2": {
                "hint": "Utilisez `docker ps` pour les conteneurs actifs, `docker ps -a` pour tous les conteneurs.",
                "solution": """# Explorer les conteneurs Docker
import subprocess

try:
    print("🔍 Conteneurs actifs:")
    result = subprocess.run(['docker', 'ps'], capture_output=True, text=True)
    print(result.stdout or "ℹ️ Aucun conteneur actif")

    print("\n📦 Tous les conteneurs:")
    result = subprocess.run(['docker', 'ps', '-a'], capture_output=True, text=True)
    print(result.stdout)

    print("\n🖼️ Images Docker disponibles:")
    result = subprocess.run(['docker', 'images'], capture_output=True, text=True)
    print(result.stdout)
except Exception as e:
    print(f"❌ Erreur: {e}")
""",
                "explanation": "`docker ps` affiche les conteneurs actifs, `docker ps -a` affiche tous les conteneurs, `docker images` liste les images."
            },
            "5.2.1": {
                "hint": "Créez un Dockerfile (FROM, COPY, RUN, CMD) et utilisez une image de base comme `python:3.9`.",
                "solution": """# Exemple de Dockerfile pour une app Python
dockerfile = '''FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "app.py"]
'''
print(dockerfile)
""",
                "explanation": "Un Dockerfile définit comment construire une image ; FROM, COPY, RUN et CMD sont les instructions de base."
            },
            "5.2.2": {
                "hint": "Construisez l'image avec `docker build -t nom_image .` puis listez les images avec `docker images`.",
                "solution": """# Construire une image Docker (exemple)
import subprocess

try:
    print('🔨 Construction de l\'image...')
    subprocess.run(['docker', 'build', '-t', 'mon-app-python', '.'], check=False)
    print('\n� Images disponibles:')
    subprocess.run(['docker', 'images'], check=False)
except Exception as e:
    print('❌ Erreur:', e)
""",
                "explanation": "`docker build` crée une image à partir d'un Dockerfile ; `-t` spécifie le tag (nom)."
            },
            "5.3.1": {
                "hint": "Démarrez un conteneur en arrière-plan avec `docker run -d -p host:container --name nom image`.",
                "solution": """# Lancer un conteneur en arrière-plan
import subprocess

try:
    subprocess.run(['docker', 'run', '-d', '-p', '8000:8000', '--name', 'mon-conteneur', 'mon-app-python'], check=False)
    subprocess.run(['docker', 'ps'], check=False)
except Exception as e:
    print('❌ Erreur:', e)
""",
                "explanation": "`-d` détache le conteneur, `-p` mappe les ports, `--name` donne un nom utile pour l'administration."
            },
            "5.4.1": {
                "hint": "Créez un volume avec `docker volume create <name>` puis montez-le via `docker run -v <name>:<path>` pour tester la persistance.",
                "solution": """# Exemple simple pour tester la persistance avec un volume
import subprocess

try:
    print('🔧 Création du volume (si nécessaire)')
    subprocess.run(['docker', 'volume', 'create', 'exercice_vol'], check=False)
    print('🚀 Lancement d\'un conteneur qui écrit dans le volume')
    subprocess.run(['docker', 'run', '--rm', '-v', 'exercice_vol:/data', 'busybox', 'sh', '-c', "echo hello > /data/hello.txt"], check=False)
    print('\n📄 Contenu du volume:')
    subprocess.run(['docker', 'run', '--rm', '-v', 'exercice_vol:/data', 'busybox', 'ls', '-la', '/data'], check=False)
except Exception as e:
    print('❌ Erreur:', e)
""",
                "explanation": "Les fichiers écrits dans un volume persistent après l'arrêt du conteneur ; utilisez `docker run -v` pour monter."
            }
        }
    
    def help(self, step):
        """Affiche l'aide pour une étape donnée"""
        if step not in self.helps:
            print(f"❌ Aide non trouvée pour l'étape {step}")
            return
            
        help_data = self.helps[step]
        
        if JUPYTER_AVAILABLE:
            # Mode Jupyter avec HTML
            # Conseil caché
            html_hint = f"""
            <details style="margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; padding: 5px; background: #f9f9f9;">
                <summary style="cursor: pointer; background: #e3f2fd; padding: 10px; border-radius: 3px; font-weight: bold; color: #0277bd;">
                    💡 Conseil Docker (cliquer pour dérouler)
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
                    🔍 Solution Docker (cliquer pour dérouler)
                </summary>
                <div style="padding: 15px; margin-top: 10px; background: white; border-radius: 3px;">
                    <p><strong>🐳 Explication :</strong> {help_data['explanation']}</p>
                    <pre style="background: #f5f5f5; padding: 10px; border-radius: 3px; overflow-x: auto; border-left: 3px solid #0db7ed;"><code>{help_data['solution']}</code></pre>
                </div>
            </details>
            """
            
            display(HTML(html_hint))
            display(HTML(html_solution))
        else:
            # Mode console
            print(f"\n🐳 AIDE {step} - DOCKER")
            print("=" * 50)
            print(f"💡 CONSEIL: {help_data['hint']}")
            print(f"\n📖 EXPLICATION: {help_data['explanation']}")
            print(f"\n🔍 SOLUTION:")
            print("-" * 30)
            print(help_data['solution'])
            print("=" * 50)
    
    def success(self, message):
        if JUPYTER_AVAILABLE:
            html = self.success_style.format(message=message)
            display(HTML(html))
        else:
            print(f"✅ 🐳 {message} 🐳")
    
    def check_docker_status(self):
        """Vérifie si Docker est installé et fonctionne"""
        try:
            result = subprocess.run(['docker', '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                return True, result.stdout.strip()
            else:
                return False, "Docker installé mais erreur"
        except FileNotFoundError:
            return False, "Docker non installé"
        except Exception as e:
            return False, str(e)

# Initialisation automatique
install_docker_packages()

if JUPYTER_AVAILABLE:
    # Mode Jupyter: forcer le rechargement de l'instance helper dans user_ns
    def load_docker_helper(force_reload=True):
        """Charge le système d'aide Docker. Si force_reload=True, remplace l'instance existante."""
        try:
            if force_reload or 'helper' not in get_ipython().user_ns:
                get_ipython().user_ns['helper'] = DockerHelper()
                print("🐳 Système d'aide Docker chargé (Jupyter) !")
                print("✨ Prêt pour la conteneurisation !")
            else:
                print("✅ Le système d'aide Docker est déjà chargé.")
        except Exception as e:
            print(f"❌ Erreur lors du chargement: {e}")

    # Charger en écrasant l'ancienne instance si nécessaire
    load_docker_helper(force_reload=True)
else:
    # Mode console - créer directement l'instance helper
    helper = DockerHelper()
    print("🐳 Système d'aide Docker chargé (mode console)")
    print("✨ Utilisez helper.help('5.1.1') pour obtenir de l'aide")