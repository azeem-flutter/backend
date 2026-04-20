"""
===============================
🧠 CPU vs I/O Bound
===============================

📌 CPU-Bound

👉 Heavy computation

Examples:
- AI models
- Image processing
- Data analysis

👉 Use:
✔ multiprocessing

----------------------------------

📌 I/O-Bound

👉 Waiting for external resources

Examples:
- API calls
- Database queries
- File reading

👉 Use:
✔ async
✔ threading

----------------------------------

📌 Real Backend Example

Passport App:

Upload → AI processing → CPU-bound
Fetch profile → DB call → I/O-bound

----------------------------------

📌 Interview Answer

"I/O-bound tasks wait for external operations, while CPU-bound tasks require heavy computation."

----------------------------------
"""

import time
import asyncio

# CPU-bound example
def cpu_task():
    for _ in range(10_000_000):
        pass

# I/O-bound example
async def io_task():
    await asyncio.sleep(2)
    print("I/O Task Done")

start = time.time()
cpu_task()
print("CPU Task Done:", time.time() - start)

start = time.time()
asyncio.run(io_task())
print("IO Task Done:", time.time() - start)