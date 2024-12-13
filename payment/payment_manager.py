import asyncio
import random

class Payment:

    def __init__(self):
        pass

    async def process_payment(self, amount):
        print(f"Processing payment ${amount}...")
        await asyncio.sleep(random.randint(1, 3))  # Simula una operación de pago
        print(f"Payment complete ${amount} ✔")
        return True