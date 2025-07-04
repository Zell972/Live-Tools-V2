import pandas as pd

def backtest_strategy(
    df: pd.DataFrame,
    risk_per_trade_pct: float = 0.01,
    initial_balance: float = 10000.0,
    sl_ratio: float = 1.0,
    tp_ratio: float = 2.0
) -> dict:
    """
    Exécute un backtest basé sur les signaux fournis par strategy_envelope.py

    Args:
        df (pd.DataFrame): colonnes = ['timestamp', 'close', 'signal']
        risk_per_trade_pct (float): Pourcentage du capital risqué par trade (ex: 0.01 = 1%)
        initial_balance (float): Capital de départ
        sl_ratio (float): distance au stop-loss en R (1R = 1 * risque)
        tp_ratio (float): distance au take-profit en R

    Returns:
        dict: statistiques de performance + DataFrame des trades
    """
    balance = initial_balance
    position = None
    entry_price = 0.0
    stop_price = 0.0
    target_price = 0.0
    trades = []

    for i in range(1, len(df)):
        row = df.iloc[i]
        prev_row = df.iloc[i - 1]

        # Check for entry
        if position is None and row["signal"] != 0:
            position = "long" if row["signal"] == 1 else "short"
            entry_price = row["close"]

            risk_amount = balance * risk_per_trade_pct
            sl_distance = entry_price * 0.01 * sl_ratio  # ex: 1% SL
            tp_distance = sl_distance * tp_ratio

            if position == "long":
                stop_price = entry_price - sl_distance
                target_price = entry_price + tp_distance
            else:
                stop_price = entry_price + sl_distance
                target_price = entry_price - tp_distance

        elif position is not None:
            price = row["close"]

            # Exit logic
            if position == "long":
                if price <= stop_price or price >= target_price:
                    result = "win" if price >= target_price else "loss"
                    pnl = risk_amount * tp_ratio if result == "win" else -risk_amount
                    balance += pnl

                    trades.append({
                        "timestamp": row["timestamp"],
                        "side": "long",
                        "entry": entry_price,
                        "exit": price,
                        "pnl": pnl,
                        "balance": balance,
                        "result": result
                    })
                    position = None

            elif position == "short":
                if price >= stop_price or price <= target_price:
                    result = "win" if price <= target_price else "loss"
                    pnl = risk_amount * tp_ratio if result == "win" else -risk_amount
                    balance += pnl

                    trades.append({
                        "timestamp": row["timestamp"],
                        "side": "short",
                        "entry": entry_price,
                        "exit": price,
                        "pnl": pnl,
                        "balance": balance,
                        "result": result
                    })
                    position = None

    # Convert to DataFrame and calculate stats
    trades_df = pd.DataFrame(trades)
    total_trades = len(trades_df)
    wins = trades_df[trades_df["pnl"] > 0]
    losses = trades_df[trades_df["pnl"] < 0]
    winrate = len(wins) / total_trades * 100 if total_trades > 0 else 0
    total_pnl = trades_df["pnl"].sum() if total_trades > 0 else 0

    stats = {
        "Initial Balance": initial_balance,
        "Final Balance": balance,
        "Total Trades": total_trades,
        "Wins": len(wins),
        "Losses": len(losses),
        "Winrate (%)": round(winrate, 2),
        "Total PnL": round(total_pnl, 2),
        "Trades": trades_df
    }

    return stats
