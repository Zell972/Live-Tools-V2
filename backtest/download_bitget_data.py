import ccxt
import pandas as pd

exchange = ccxt.bitget()

symbol = 'BTC/USDT:USDT'  # ⚠️ Bitget utilise ce format avec ":USDT"
timeframe = '1h'
limit = 1000  # max par requête
since = exchange.parse8601('2024-01-01T00:00:00Z')

# Téléchargement OHLCV
ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, since=since, limit=limit)

# Mise en DataFrame
df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

# Sauvegarde CSV
df.to_csv("backtest/data/BTCUSDT_1h.csv", index=False)
print("✅ Données sauvegardées dans backtest/data/BTCUSDT_1h.csv")
