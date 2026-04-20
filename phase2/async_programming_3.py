"""
===============================
🧠 ASYNC PROGRAMMING
===============================

📌 What is Async?

👉 A way to write NON-BLOCKING code

Using:
- async
- await

----------------------------------

📌 Key Idea

👉 While waiting → do other work

----------------------------------

📌 Blocking vs Non-Blocking

❌ Blocking:
    time.sleep(5)
    → program waits

✔ Non-blocking:
    await asyncio.sleep(5)
    → program continues

----------------------------------

📌 Real Backend Example (VERY IMPORTANT)

In FastAPI:

User requests profile →
Backend calls database (takes time)

👉 Without async:
    server waits → slow ❌

👉 With async:
    server handles other users ✔️

----------------------------------

📌 Interview Answer

"Async programming allows non-blocking execution using an event loop,
making it efficient for I/O-bound tasks."

----------------------------------

📌 Pros

✔ High performance
✔ Handles many users
✔ Best for APIs

----------------------------------

📌 Cons

❌ Complex debugging
❌ Not for CPU tasks

----------------------------------

📌 When to Use?

👉 API calls
👉 Database queries
👉 File I/O

----------------------------------
"""

import asyncio

async def task1():
    print("Task 1 start")
    await asyncio.sleep(2)  # non-blocking wait
    print("Task 1 end")

async def task2():
    print("Task 2 start")
    await asyncio.sleep(1)
    print("Task 2 end")

async def main():
    """
    Event loop runs this function
    Both tasks run concurrently
    """
    await asyncio.gather(task1(), task2())

asyncio.run(main())

"""
👉 Output:
Tasks overlap instead of waiting one by one

----------------------------------

📌 Real FastAPI Example

@app.get("/data")
async def get_data():
    data = await fetch_from_db()
    return data

👉 This allows handling many users efficiently
"""