"""
===============================
🧠 GIL (Global Interpreter Lock)
===============================

📌 What is GIL?

GIL is a lock in Python that ensures:
👉 Only ONE thread executes Python bytecode at a time

Even if you create multiple threads,
👉 Python will NOT run them in parallel (for CPU tasks)

----------------------------------

📌 Why GIL exists?

👉 To make memory management safe
👉 Prevent race conditions (multiple threads modifying same memory)

----------------------------------

📌 Problem with GIL

👉 Threads CANNOT run in true parallel for CPU-bound tasks

Example:
- Calculations
- Image processing
- Machine Learning

👉 Even with 4 threads → only 1 runs at a time ❌

----------------------------------

📌 Real Backend Example

In your FastAPI project:

If you do:
- heavy data processing
- AI computation

👉 Threads will NOT improve performance

Instead → use multiprocessing ✔️

----------------------------------

📌 Interview Answer

"GIL prevents multiple threads from executing Python code at the same time,
which limits performance for CPU-bound tasks."

----------------------------------

📌 Key Insight

👉 GIL DOES NOT affect:
✔ I/O tasks (API, DB)
✔ Async programming

👉 GIL DOES affect:
❌ CPU-heavy tasks

----------------------------------
"""

import threading
import time

# Example to show GIL behavior

def cpu_task():
    """
    This is a CPU-bound task
    Even if we run multiple threads,
    GIL allows only one to execute at a time
    """
    count = 0
    for _ in range(10_000_000):
        count += 1

# Creating multiple threads
t1 = threading.Thread(target=cpu_task)
t2 = threading.Thread(target=cpu_task)

start = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print("Time taken:", end - start)

"""
👉 Observation:

Even with 2 threads,
👉 Execution is NOT significantly faster

WHY?
👉 Because of GIL

----------------------------------

📌 When NOT to use threads?

❌ CPU-heavy tasks

----------------------------------

📌 What to use instead?

👉 multiprocessing (next topic)
"""