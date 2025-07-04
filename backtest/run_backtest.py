from strategy_envelope import generate_signals
import pandas as pd

df = pd.read_csv("data/BTCUSDT_1h.csv", parse_dates=["timestamp"])
df = generate_signals(df, ma_length=20, envelope_pct=0.01, ma_type="ema")

print(df[["timestamp", "close", "ma", "upper", "lower", "signal"]].tail(10))
