"""
===============================
🧠 EVENT LOOP
===============================

📌 What is Event Loop?

👉 The engine behind async programming

👉 It:
- Manages tasks
- Schedules execution
- Runs async functions

----------------------------------

📌 Flow

Task → Event Loop → Execute when ready

----------------------------------

📌 Real Backend Example

FastAPI uses event loop internally

👉 When multiple users hit API:
Event loop manages all requests efficiently

----------------------------------

📌 Interview Answer

"Event loop is responsible for scheduling and executing asynchronous tasks."

----------------------------------
"""

import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("Done")

# Event loop starts here
asyncio.run(say_hello())

"""
👉 asyncio.run() creates and runs event loop

----------------------------------

📌 Important

👉 You NEVER manually manage loop in FastAPI
👉 It is handled automatically
"""