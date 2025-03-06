from src.api.market_data import get_market_data
from src.api.chatgpt_integration import get_chatgpt_insight
from src.analysis.technical_analysis import calculate_moving_average
from src.database.db_manager import save_analysis_to_db
from src.decision.decision_engine import make_decision
from src.utils.helpers import setup_logger

logger = setup_logger()

def main():
    symbol = "AAPL"
    logger.info(f"Début de l'analyse pour {symbol}")

    # Récupération des données
    market_data = get_market_data(symbol)
    logger.info("Données du marché récupérées")

    # Analyse technique
    technical_analysis = calculate_moving_average(market_data)
    logger.info("Analyse technique terminée")

    # Décision
    decision = make_decision(technical_analysis.iloc[-1].to_dict())
    logger.info(f"Décision: {decision}")

    # Insight ChatGPT
    insight = get_chatgpt_insight(f"Analyse du marché pour {symbol}: {technical_analysis}")
    logger.info(f"Insight ChatGPT: {insight}")

    # Sauvegarde en base de données
    save_analysis_to_db(symbol, {"decision": decision, "insight": insight})
    logger.info("Analyse sauvegardée en base de données")

if __name__ == "__main__":
    main()