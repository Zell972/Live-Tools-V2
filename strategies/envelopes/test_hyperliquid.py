import asyncio
from utilities.hyperliquid_perp import PerpHyperliquid
from secret import ACCOUNTS

async def main():
    account = ACCOUNTS["hyperliquid1"]
    bot = PerpHyperliquid(account["public_api"], account["secret_api"])
    
    await bot.connect()
    
    # Voir ton solde
    await bot.get_balance()
    
    # Envoyer un ordre TEST (en commentaire pour éviter erreur, active quand prêt)
    # await bot.place_order("BTC-USDT", "buy", size=0.001, price=30000)
    
    await bot.close()

if __name__ == "__main__":
    asyncio.run(main())
