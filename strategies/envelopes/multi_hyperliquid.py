import datetime
import sys
import asyncio
import ta

sys.path.append("./Live-Tools-V2")

from utilities.hyperliquid_perp import PerpHyperliquid
from secret import ACCOUNTS

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def main():
    account = ACCOUNTS["hyperliquid1"]

    leverage = 3
    tf = "1h"
    sl = 0.3

    params = {
      "BTC/USDT": {
            "src": "close",
            "ma_base_window": 7,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "ETH/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "ADA/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.09, 0.12, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "AVAX/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.09, 0.12, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "EGLD/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15, 0.2],
            "size": 0.05,
            "sides": ["long", "short"],
        },
        "KSM/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15, 0.2],
            "size": 0.05,
            "sides": ["long", "short"],
        },
        "OCEAN/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15, 0.2],
            "size": 0.05,
            "sides": ["long", "short"],
        },
        "REN/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15, 0.2],
            "size": 0.05,
            "sides": ["long", "short"],
        },
        "ACH/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15, 0.2],
            "size": 0.05,
            "sides": ["long", "short"],
        },
        "APE/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15, 0.2],
            "size": 0.05,
            "sides": ["long", "short"],
        },
        "CRV/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15, 0.2],
            "size": 0.05,
            "sides": ["long", "short"],
        },
        "DOGE/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15, 0.2],
            "size": 0.05,
            "sides": ["long", "short"],
        },
        "ENJ/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15, 0.2],
            "size": 0.05,
            "sides": ["long", "short"],
        },
        "FET/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15, 0.2],
            "size": 0.05,
            "sides": ["long", "short"],
        },
        "ICP/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15, 0.2],
            "size": 0.05,
            "sides": ["long", "short"],
        },
        "IMX/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15, 0.2],
            "size": 0.05,
            "sides": ["long", "short"],
        },
        "LDO/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15, 0.2],
            "size": 0.05,
            "sides": ["long", "short"],
        },
        "MAGIC/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15, 0.2],
            "size": 0.05,
            "sides": ["long", "short"],
        },
        "REEF/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15, 0.2],
            "size": 0.05,
            "sides": ["long", "short"],
        },
        "SAND/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15, 0.2],
            "size": 0.05,
            "sides": ["long", "short"],
        },
        "TRX/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15, 0.2],
            "size": 0.05,
            "sides": ["long", "short"],
        },
        "XTZ/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15, 0.2],
            "size": 0.05,
            "sides": ["long", "short"],
        },
    }


    exchange = PerpHyperliquid(
        api_key=account["api_key"],
        api_secret=account["api_secret"],
    )
    invert_side = {"long": "sell", "short": "buy"}

    print(f"--- Execution started at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")
    try:
        await exchange.load_markets()

        # Vérifie la disponibilité des paires
        for pair in list(params.keys()):
            info = exchange.get_pair_info(pair)
            if info is None:
                print(f"Pair {pair} not found, removing from params...")
                del params[pair]

        pairs = list(params.keys())

        # Récupère les OHLCV et calcule indicateurs
        print(f"Getting data and indicators on {len(pairs)} pairs...")
        tasks = [exchange.get_last_ohlcv(pair, tf, 50) for pair in pairs]
        dfs = await asyncio.gather(*tasks)
        df_list = dict(zip(pairs, dfs))

        for pair in df_list:
            current_params = params[pair]
            df = df_list[pair]
            if current_params["src"] == "close":
                src = df["close"]
            elif current_params["src"] == "ohlc4":
                src = (df["close"] + df["high"] + df["low"] + df["open"]) / 4

            df["ma_base"] = ta.trend.sma_indicator(close=src, window=current_params["ma_base_window"])
            high_envelopes = [round(1 / (1 - e) - 1, 3) for e in current_params["envelopes"]]

            for i in range(1, len(current_params["envelopes"]) + 1):
                df[f"ma_high_{i}"] = df["ma_base"] * (1 + high_envelopes[i - 1])
                df[f"ma_low_{i}"] = df["ma_base"] * (1 - current_params["envelopes"][i - 1])

            df_list[pair] = df

        usdt_balance = await exchange.get_balance()
        usdt_balance = usdt_balance.total
        print(f"Balance: {round(usdt_balance, 2)} USDT")

        # Récupère les positions ouvertes
        print(f"Getting live positions...")
        positions = await exchange.get_open_positions(pairs)

        tasks_close = []
        tasks_open = []

        for position in positions:
            print(f"Current position on {position.pair} {position.side} - {position.size} ~ {position.usd_size} $")
            row = df_list[position.pair].iloc[-2]

            # Placer ordre limite pour fermer position au prix MA base
            tasks_close.append(
                exchange.place_order(
                    pair=position.pair,
                    side=invert_side[position.side],
                    price=row["ma_base"],
                    size=exchange.amount_to_precision(position.pair, position.size),
                    type="limit",
                    reduce=True,
                    leverage=leverage,
                    error=False,
                )
            )

            # Placer stop loss market order
            if position.side == "long":
                sl_side = "sell"
                sl_price = position.entry_price * (1 - sl)
            elif position.side == "short":
                sl_side = "buy"
                sl_price = position.entry_price * (1 + sl)

            sl_price = exchange.price_to_precision(position.pair, sl_price)

            tasks_close.append(
                exchange.place_trigger_order(
                    pair=position.pair,
                    side=sl_side,
                    trigger_price=sl_price,
                    price=None,
                    size=exchange.amount_to_precision(position.pair, position.size),
                    type="market",
                    reduce=True,
                    leverage=leverage,
                    error=False,
                )
            )

            # Place trigger orders d'entrée (long/short) selon enveloppes non encore couvertes
            canceled_buy = 0  # Pas de gestion ici des orders annulés (à adapter si besoin)
            canceled_sell = 0

            for i in range(len(params[position.pair]["envelopes"]) - canceled_buy, len(params[position.pair]["envelopes"])):
                tasks_open.append(
                    exchange.place_trigger_order(
                        pair=position.pair,
                        side="buy",
                        price=exchange.price_to_precision(position.pair, row[f"ma_low_{i+1}"]),
                        trigger_price=exchange.price_to_precision(position.pair, row[f"ma_low_{i+1}"] * 1.005),
                        size=exchange.amount_to_precision(
                            position.pair,
                            ((params[position.pair]["size"] * usdt_balance) / len(params[position.pair]["envelopes"]) * leverage)
                            / row[f"ma_low_{i+1}"],
                        ),
                        type="limit",
                        reduce=False,
                        leverage=leverage,
                        error=False,
                    )
                )

            for i in range(len(params[position.pair]["envelopes"]) - canceled_sell, len(params[position.pair]["envelopes"])):
                tasks_open.append(
                    exchange.place_trigger_order(
                        pair=position.pair,
                        side="sell",
                        trigger_price=exchange.price_to_precision(position.pair, row[f"ma_high_{i+1}"] * 0.995),
                        price=exchange.price_to_precision(position.pair, row[f"ma_high_{i+1}"]),
                        size=exchange.amount_to_precision(
                            position.pair,
                            ((params[position.pair]["size"] * usdt_balance) / len(params[position.pair]["envelopes"]) * leverage)
                            / row[f"ma_high_{i+1}"],
                        ),
                        type="limit",
                        reduce=False,
                        leverage=leverage,
                        error=False,
                    )
                )

        print(f"Placing {len(tasks_close)} close SL / limit orders...")
        await asyncio.gather(*tasks_close)

        pairs_not_in_position = [pair for pair in pairs if pair not in [pos.pair for pos in positions]]
        for pair in pairs_not_in_position:
            row = df_list[pair].iloc[-2]

            for i in range(len(params[pair]["envelopes"])):
                if "long" in params[pair]["sides"]:
                    tasks_open.append(
                        exchange.place_trigger_order(
                            pair=pair,
                            side="buy",
                            price=exchange.price_to_precision(pair, row[f"ma_low_{i+1}"]),
                            trigger_price=exchange.price_to_precision(pair, row[f"ma_low_{i+1}"] * 1.005),
                            size=exchange.amount_to_precision(
                                pair,
                                ((params[pair]["size"] * usdt_balance) / len(params[pair]["envelopes"]) * leverage)
                                / row[f"ma_low_{i+1}"],
                            ),
                            type="limit",
                            reduce=False,
                            leverage=leverage,
                            error=False,
                        )
                    )
                if "short" in params[pair]["sides"]:
                    tasks_open.append(
                        exchange.place_trigger_order(
                            pair=pair,
                            side="sell",
                            trigger_price=exchange.price_to_precision(pair, row[f"ma_high_{i+1}"] * 0.995),
                            price=exchange.price_to_precision(pair, row[f"ma_high_{i+1}"]),
                            size=exchange.amount_to_precision(
                                pair,
                                ((params[pair]["size"] * usdt_balance) / len(params[pair]["envelopes"]) * leverage)
                                / row[f"ma_high_{i+1}"],
                            ),
                            type="limit",
                            reduce=False,
                            leverage=leverage,
                            error=False,
                        )
                    )

        print(f"Placing {len(tasks_open)} open limit orders...")
        await asyncio.gather(*tasks_open)

        await exchange.close()
        print(f"--- Execution finished at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")

    except Exception as e:
        await exchange.close()
        raise e


if __name__ == "__main__":
    asyncio.run(main())
