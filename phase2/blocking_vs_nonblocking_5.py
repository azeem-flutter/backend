"""
===============================
🧠 BLOCKING vs NON-BLOCKING
===============================

📌 Blocking

👉 Task waits until completion

Example:
time.sleep(3)

----------------------------------

📌 Non-Blocking

👉 Task does NOT wait
👉 Other tasks can run

Example:
await asyncio.sleep(3)

----------------------------------

📌 Real Backend Example

API calling external service

❌ Blocking:
Server waits → no other request handled

✔ Non-blocking:
Server handles multiple users

----------------------------------

📌 Interview Answer

"Blocking code waits for execution, while non-blocking allows other tasks to run concurrently."

----------------------------------
"""

import time
import asyncio

# Blocking example
def blocking():
    print("Blocking start")
    time.sleep(2)
    print("Blocking end")

# Non-blocking example
async def non_blocking():
    print("Non-blocking start")
    await asyncio.sleep(5)
    print("Non-blocking end")
async def non_blocking1():
    print("a")
    await asyncio.sleep(5)
    print('b')

async def main():
    await asyncio.gather(non_blocking,non_blocking1)

asyncio.run(main())