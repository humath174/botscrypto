import pandas as pd

def calculate_moving_average(data, window=20):
    """
    Calcule la moyenne mobile sur une fenêtre donnée.
    """
    df = pd.DataFrame(data["Time Series (Daily)"]).T
    df['close'] = df['4. close'].astype(float)
    df['moving_average'] = df['close'].rolling(window=window).mean()
    return df[['close', 'moving_average']]