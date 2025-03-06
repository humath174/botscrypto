import logging

def setup_logger():
    """
    Configure le logger pour enregistrer les logs dans un fichier.
    """
    logging.basicConfig(
        filename="logs/market_analysis.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger()