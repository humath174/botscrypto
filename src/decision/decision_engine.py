def make_decision(analysis):
    """
    Prend une décision d'achat/vente basée sur l'analyse.
    """
    moving_average = analysis.get("moving_average")
    close_price = analysis.get("close")
    if close_price > moving_average:
        return "Acheter"
    else:
        return "Vendre"