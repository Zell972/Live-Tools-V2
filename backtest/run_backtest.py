import pandas as pd
from strategy_envelope import generate_signals
from backtest_engine import backtest_strategy

# Charger les données
df = pd.read_csv("data/BTCUSDT_1h.csv", parse_dates=["timestamp"])

# Générer les signaux
df = generate_signals(df, ma_length=20, envelope_pct=0.01, ma_type="ema")

# Lancer le backtest
results = backtest_strategy(df)

# Afficher les stats
for key, value in results.items():
    if key != "Trades":
        print(f"{key}: {value}")

# Sauvegarder les trades
results["Trades"].to_csv("trades_output.csv", index=False)
