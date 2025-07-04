import pandas as pd

def generate_signals(
    df: pd.DataFrame,
    ma_length: int = 20,
    envelope_pct: float = 0.01,
    ma_type: str = "ema"
) -> pd.DataFrame:
    """
    Applique la stratégie Envelope fidèle à celle de multi_bitget.py
    
    Args:
        df (pd.DataFrame): colonnes nécessaires = ['close']
        ma_length (int): période de la moyenne mobile
        envelope_pct (float): pourcentage de l'enveloppe (ex: 0.01 = 1%)
        ma_type (str): "ema" ou "sma"
    
    Returns:
        pd.DataFrame: avec colonnes ajoutées ['ma', 'upper', 'lower', 'signal']
    """
    df = df.copy()

    if ma_type == "ema":
        df["ma"] = df["close"].ewm(span=ma_length, adjust=False).mean()
    else:
        df["ma"] = df["close"].rolling(ma_length).mean()

    df["upper"] = df["ma"] * (1 + envelope_pct)
    df["lower"] = df["ma"] * (1 - envelope_pct)

    df["signal"] = 0
    df.loc[df["close"] > df["upper"], "signal"] = -1  # Short
    df.loc[df["close"] < df["lower"], "signal"] = 1   # Long

    return df

