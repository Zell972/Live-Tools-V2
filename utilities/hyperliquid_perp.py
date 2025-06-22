import asyncio
import json
import websockets
import hmac
import hashlib
import time


class PerpHyperliquid:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.ws_url = "wss://api.hyperliquid.xyz/ws"
        self.ws = None

    async def connect(self):
        print("Connecting to Hyperliquid WebSocket...")
        self.ws = await websockets.connect(self.ws_url)
        await self.authenticate()

    async def authenticate(self):
        ts = str(int(time.time() * 1000))
        msg = ts + self.api_key
        sig = hmac.new(self.api_secret.encode(), msg.encode(), hashlib.sha256).hexdigest()
        auth_msg = {
            "method": "auth",
            "params": {
                "apiKey": self.api_key,
                "ts": ts,
                "sig": sig
            }
        }
        await self.ws.send(json.dumps(auth_msg))
        resp = await self.ws.recv()
        print("Auth response:", resp)

    async def close(self):
        if self.ws:
            await self.ws.close()
            print("WebSocket closed.")

    async def get_balance(self):
        req = {
            "method": "walletStatus",
            "params": {}
        }
        await self.ws.send(json.dumps(req))
        resp = await self.ws.recv()
        data = json.loads(resp)
        balance = data.get("result", {}).get("marginSummary", {}).get("accountValue", 0)
        print(f"USDT Balance: {balance}")
        return balance

    async def place_order(self, pair, side, size, price=None, reduce=False):
        order = {
            "method": "order",
            "params": {
                "symbol": pair,
                "side": side.upper(),  # "BUY" or "SELL"
                "size": size,
                "reduceOnly": reduce,
                "price": price if price else 0,
                "type": "limit" if price else "market",
                "postOnly": False
            }
        }
        await self.ws.send(json.dumps(order))
        resp = await self.ws.recv()
        print("Order Response:", resp)
        return json.loads(resp)
