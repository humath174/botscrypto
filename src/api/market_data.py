import requests
from src.config import ALPHA_VANTAGE_API_KEY

def get_market_data(symbol):
    """
    Récupère les données du marché pour un symbole donné.
    """
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erreur lors de la récupération des données: {response.status_code}")