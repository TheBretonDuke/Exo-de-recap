"""
🌐 API Helper - Module d'aide pour l'exercice 7 (APIs et Services Web)
Fournit des aides contextuelles pour l'apprentissage des APIs REST avec FastAPI.
"""

from IPython.display import HTML, display
import pandas as pd

class APIHelper:
    def __init__(self):
        self.name = "API Helper"
        self.version = "1.0.0"
        print(f"🌐 {self.name} v{self.version} chargé avec succès!")
        print("💡 Tapez api_helper.help('section') pour obtenir de l'aide")
        print("📚 Sections disponibles: 7.1.1, 7.1.2, 7.2.1, 7.2.2, 7.3.1, 7.3.2, 7.4.1, 7.4.2")
    
    def help(self, section=None):
        """Affiche l'aide pour une section spécifique avec masquage interactif"""
        if section is None:
            self._show_main_help()
            return
        
        sections = {
            "7.1.1": self._help_7_1_1,
            "7.1.2": self._help_7_1_2,
            "7.2.1": self._help_7_2_1,
            "7.2.2": self._help_7_2_2,
            "7.3.1": self._help_7_3_1,
            "7.3.2": self._help_7_3_2,
            "7.4.1": self._help_7_4_1,
            "7.4.2": self._help_7_4_2
        }
        
        if section in sections:
            sections[section]()
        else:
            self._show_error(section, list(sections.keys()))

    def _show_main_help(self):
        display(HTML("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 20px; border-radius: 10px; color: white; margin: 10px 0;'>
            <h2>🌐 Guide API et Services Web</h2>
            <p><strong>Sections disponibles :</strong></p>
            <ul>
                <li><code>7.1.1</code> - Comparaison SOAP vs REST vs GraphQL</li>
                <li><code>7.1.2</code> - Principes et contraintes REST</li>
                <li><code>7.2.1</code> - Première API FastAPI</li>
                <li><code>7.2.2</code> - Validation Pydantic avancée</li>
                <li><code>7.3.1</code> - Authentification JWT</li>
                <li><code>7.3.2</code> - Middleware et CORS</li>
                <li><code>7.4.1</code> - Tests automatisés</li>
                <li><code>7.4.2</code> - Déploiement production</li>
            </ul>
            <p>💡 <strong>Usage:</strong> <code>api_helper.help("7.1.1")</code></p>
        </div>
        """))
    
    def _show_error(self, section, available_sections):
        display(HTML(f"""
        <div style='background: #ff6b6b; padding: 15px; border-radius: 8px; color: white; margin: 10px 0;'>
            <h3>❌ Section introuvable</h3>
            <p>La section <strong>{section}</strong> n'existe pas.</p>
            <p>Sections disponibles: {', '.join(available_sections)}</p>
        </div>
        """))
    
    def _help_7_3_2(self):
        """Aide pour la section 7.3.2 - Middleware et CORS"""
        html_content = """
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 20px; border-radius: 10px; color: white; margin: 10px 0;'>
            <h2>🛡️ Section 7.3.2 : Middleware et CORS</h2>
            
            <details style='margin: 15px 0; cursor: pointer;'>
                <summary style='font-size: 18px; font-weight: bold; padding: 10px; 
                               background: rgba(255,255,255,0.1); border-radius: 5px;'>
                    🔧 Concepts Middleware
                </summary>
                <div style='padding: 15px; background: rgba(255,255,255,0.05); margin-top: 10px; border-radius: 5px;'>
                    <ul>
                        <li><strong>CORS:</strong> Cross-Origin Resource Sharing - permet les requêtes cross-domain</li>
                        <li><strong>GZip:</strong> Compression automatique des réponses</li>
                        <li><strong>Middleware personnalisé:</strong> Traitement avant/après chaque requête</li>
                        <li><strong>Logging:</strong> Enregistrement des requêtes pour monitoring</li>
                    </ul>
                    <h4>⚠️ Sécurité CORS :</h4>
                    <p>En production, spécifiez des domaines précis au lieu de "*"</p>
                </div>
            </details>
            
            <details style='margin: 15px 0; cursor: pointer;'>
                <summary style='font-size: 18px; font-weight: bold; padding: 10px; 
                               background: rgba(255,255,255,0.1); border-radius: 5px;'>
                    🔧 Middlewares de sécurité
                </summary>
                <div style='padding: 15px; background: rgba(255,255,255,0.05); margin-top: 10px; border-radius: 5px;'>
                    <p>Ajoutez ces middlewares :</p>
                    <pre style='background: #2d3748; padding: 15px; border-radius: 5px; color: #e2e8f0;'>
# Middleware de sécurité
@app.middleware("http")
async def security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response

# Rate limiting  
from collections import defaultdict
request_counts = defaultdict(list)

@app.middleware("http")
async def rate_limit(request: Request, call_next):
    client_ip = request.client.host
    current_time = time.time()
    
    # Nettoyer les anciens timestamps
    request_counts[client_ip] = [
        t for t in request_counts[client_ip] 
        if current_time - t < 60
    ]
    
    # Vérifier limite (100 req/min)
    if len(request_counts[client_ip]) >= 100:
        raise HTTPException(429, "Trop de requêtes")
    
    request_counts[client_ip].append(current_time)
    return await call_next(request)</pre>
                </div>
            </details>
            
            <details style='margin: 15px 0; cursor: pointer;'>
                <summary style='font-size: 18px; font-weight: bold; padding: 10px; 
                               background: rgba(255,255,255,0.1); border-radius: 5px;'>
                    🧪 Tests des middlewares
                </summary>
                <div style='padding: 15px; background: rgba(255,255,255,0.05); margin-top: 10px; border-radius: 5px;'>
                    <h4>Comment tester :</h4>
                    <ol>
                        <li><strong>CORS:</strong> Requête depuis un autre domaine</li>
                        <li><strong>Compression:</strong> Header "Content-Encoding: gzip"</li>
                        <li><strong>Logging:</strong> Observer les logs console</li>
                        <li><strong>Sécurité:</strong> Inspecter headers HTTP</li>
                    </ol>
                    
                    <h4>🧪 Commandes de test :</h4>
                    <pre style='background: #2d3748; padding: 10px; border-radius: 5px; color: #e2e8f0;'>
# Test CORS
curl -H "Origin: http://example.com" -X OPTIONS http://localhost:8000/users

# Test headers sécurité  
curl -I http://localhost:8000/</pre>
                    
                    <h4>⚡ Endpoint de test :</h4>
                    <pre style='background: #2d3748; padding: 10px; border-radius: 5px; color: #e2e8f0;'>
@app.get("/test-middleware")
async def test_middleware():
    return {
        "message": "Middleware actifs",
        "timestamp": datetime.now(),
        "size": "A" * 2000  # Pour tester compression
    }</pre>
                </div>
            </details>
        </div>
        """
        display(HTML(html_content))

    def _help_7_1_1(self):
        """Aide pour la comparaison des protocoles"""
        html_content = """
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 20px; border-radius: 10px; color: white; margin: 10px 0;'>
            <h2>🌐 Section 7.1.1 : Comparaison SOAP vs REST vs GraphQL</h2>
            <p>Utilisez la méthode <code>api_helper.compare_protocols()</code> pour voir un tableau détaillé des différences.</p>
            <p><strong>Points clés :</strong></p>
            <ul>
                <li><strong>SOAP :</strong> Protocol complexe, XML, sécurité robuste</li>
                <li><strong>REST :</strong> Simple, léger, JSON, caches HTTP</li>
                <li><strong>GraphQL :</strong> Flexible, query précise, single endpoint</li>
            </ul>
        </div>
        """
        display(HTML(html_content))

    def _help_7_1_2(self):
        """Aide pour les principes REST"""
        html_content = """
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 20px; border-radius: 10px; color: white; margin: 10px 0;'>
            <h2>🌐 Section 7.1.2 : Principes REST</h2>
            <p><strong>Les 6 contraintes REST :</strong></p>
            <ol>
                <li><strong>Client-Server :</strong> Séparation des responsabilités</li>
                <li><strong>Stateless :</strong> Chaque requête est indépendante</li>
                <li><strong>Cacheable :</strong> Les réponses peuvent être mises en cache</li>
                <li><strong>Uniform Interface :</strong> Interface uniforme (HTTP verbs, URIs)</li>
                <li><strong>Layered System :</strong> Architecture en couches</li>
                <li><strong>Code on Demand :</strong> (Optionnel) Serveur peut envoyer du code</li>
            </ol>
            <p><strong>💡 Bonnes pratiques :</strong> Utilisez les noms de ressources au pluriel, verbes HTTP appropriés, codes de statut corrects.</p>
        </div>
        """
        display(HTML(html_content))

    def _help_7_2_1(self):
        """Aide pour FastAPI basics"""
        html_content = """
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 20px; border-radius: 10px; color: white; margin: 10px 0;'>
            <h2>🚀 Section 7.2.1 : FastAPI Basics</h2>
            <p><strong>Endpoints à implémenter :</strong></p>
            <ul>
                <li><code>@app.get("/")</code> - Page d'accueil</li>
                <li><code>@app.get("/users")</code> - Lister utilisateurs</li>
                <li><code>@app.get("/users/{user_id}")</code> - Obtenir un utilisateur</li>
                <li><code>@app.post("/users", status_code=201)</code> - Créer utilisateur</li>
                <li><code>@app.put("/users/{user_id}")</code> - Modifier utilisateur</li>
                <li><code>@app.delete("/users/{user_id}")</code> - Supprimer utilisateur</li>
            </ul>
            <p><strong>💡 Astuce :</strong> Utilisez <code>HTTPException(404, "Message")</code> pour les erreurs.</p>
        </div>
        """
        display(HTML(html_content))

    def _help_7_2_2(self):
        """Aide pour Pydantic"""
        html_content = """
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 20px; border-radius: 10px; color: white; margin: 10px 0;'>
            <h2>✅ Section 7.2.2 : Validation Pydantic</h2>
            <p><strong>Modifiez votre API :</strong></p>
            <ul>
                <li>Utilisez <code>UserCreate</code> pour les entrées (POST, PUT)</li>
                <li>Utilisez <code>UserResponse</code> pour les sorties</li>
                <li><code>Field(..., min_length=2)</code> pour la validation</li>
                <li><code>@validator('name')</code> pour validation personnalisée</li>
                <li><code>response_model=UserResponse</code> dans les décorateurs</li>
            </ul>
            <p><strong>💡 Installation :</strong> <code>pip install email-validator</code> pour EmailStr</p>
        </div>
        """
        display(HTML(html_content))

    def _help_7_3_1(self):
        """Aide pour JWT"""
        html_content = """
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 20px; border-radius: 10px; color: white; margin: 10px 0;'>
            <h2>🔒 Section 7.3.1 : JWT</h2>
            <p><strong>Fonctions à implémenter :</strong></p>
            <ul>
                <li><code>verify_password()</code> - Vérifier mot de passe hashé</li>
                <li><code>create_access_token()</code> - Créer JWT avec expiration</li>
                <li><code>verify_token()</code> - Décoder et vérifier JWT</li>
                <li><code>get_current_user()</code> - Middleware authentification</li>
            </ul>
            <p><strong>Endpoints :</strong></p>
            <ul>
                <li><code>POST /login</code> - Authentification</li>
                <li><code>GET /protected</code> - Route protégée</li>
            </ul>
            <p><strong>💡 Installation :</strong> <code>pip install python-jose[cryptography] passlib[bcrypt]</code></p>
        </div>
        """
        display(HTML(html_content))

    def _help_7_4_1(self):
        """Aide pour les tests"""
        html_content = """
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 20px; border-radius: 10px; color: white; margin: 10px 0;'>
            <h2>🧪 Section 7.4.1 : Tests</h2>
            <p><strong>Types de tests :</strong></p>
            <ul>
                <li><strong>Tests endpoints :</strong> TestClient(app)</li>
                <li><strong>Tests validation :</strong> Données invalides → 422</li>
                <li><strong>Tests auth :</strong> Avec/sans token</li>
                <li><strong>Tests erreurs :</strong> 404, 401, etc.</li>
            </ul>
            <p><strong>💡 Commande :</strong> <code>pytest -v</code> pour exécuter les tests</p>
            <p><strong>📊 Couverture :</strong> <code>pytest --cov=main</code></p>
        </div>
        """
        display(HTML(html_content))

    def _help_7_4_2(self):
        """Aide pour le déploiement"""
        html_content = """
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 20px; border-radius: 10px; color: white; margin: 10px 0;'>
            <h2>🚀 Section 7.4.2 : Déploiement</h2>
            <p><strong>Configuration production :</strong></p>
            <ul>
                <li><strong>Logging :</strong> Configuration structurée</li>
                <li><strong>Variables d'env :</strong> Secrets sécurisés</li>
                <li><strong>Health checks :</strong> Endpoint /health</li>
                <li><strong>Gestionnaire d'erreurs :</strong> Exception handler global</li>
            </ul>
            <p><strong>🐳 Docker :</strong> Dockerfile + docker-compose</p>
            <p><strong>🚀 Commande :</strong> <code>uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4</code></p>
        </div>
        """
        display(HTML(html_content))

    def compare_protocols(self):
        """Fonction de démonstration pour comparer les protocoles API"""
        comparison = pd.DataFrame({
            'Aspect': ['Format', 'Transport', 'Verbes', 'Structure', 'Performance', 
                       'Sécurité', 'Cache', 'Complexité', 'Usage'],
            'SOAP': ['XML', 'HTTP/HTTPS/SMTP', 'Actions', 'Envelope/Body', 'Lent', 
                     'WS-Security', 'Difficile', 'Élevée', 'Enterprise'],
            'REST': ['JSON/XML', 'HTTP', 'GET/POST/PUT/DELETE', 'Resources', 'Rapide', 
                     'HTTPS/OAuth', 'Excellent', 'Faible', 'Web/Mobile'],
            'GraphQL': ['JSON', 'HTTP', 'Query/Mutation', 'Schema', 'Variable', 
                        'HTTPS/JWT', 'Complexe', 'Moyenne', 'Frontend']
        })
        
        print("🌐 Comparaison des protocoles API :")
        print("=" * 60)
        display(comparison)
        print("✅ Recommandation : REST pour APIs publiques, GraphQL pour frontends complexes")

# Créer l'instance globale
api_helper = APIHelper()