# Configuration du projet
import os

# Clés API
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY", "votre_clé_api")
CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY", "votre_clé_api_chatgpt")

# Configuration de la base de données
DATABASE_CONFIG = {
    "dbname": "market_analysis.db",
    "user": "admin",
    "password": "password",
    "host": "localhost",
    "port": 5432,
}