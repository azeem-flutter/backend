# ============================================================
# 🚀 PROCESS vs THREAD (Complete Notes + Examples)
# ============================================================

# ------------------------------------------------------------
# 🧠 1. PROCESS
# ------------------------------------------------------------

# Definition:
# A process is a running program with its own separate memory and resources.

# Properties:
# - Independent (does not affect other processes)
# - Has its own memory (RAM)
# - Has its own CPU time
# - Safe (crash in one process does not affect others)
# - Heavy (uses more memory)

# Real-life Example:
# Chrome, VS Code, Spotify → all are separate processes
# If VS Code crashes → Chrome still runs (independent)

# Analogy:
# Process = Separate building


# ------------------------------------------------------------
# 🧠 2. THREAD
# ------------------------------------------------------------

# Definition:
# A thread is a smaller unit inside a process that performs tasks.

# Properties:
# - Shares memory with other threads
# - Lightweight (faster than process)
# - Communication is easy (shared data)
# - Not safe (one thread crash can affect whole process)

# Real-life Example:
# Inside Chrome:
# - One thread loads webpage
# - One thread plays video
# - One thread handles UI

# Analogy:
# Thread = Workers inside a building


# ------------------------------------------------------------
# 🧠 3. SINGLE THREAD vs MULTI THREAD
# ------------------------------------------------------------

# Single Thread:
# - Only one task runs at a time
# - Simple but slow for multiple tasks

# Real-life:
# One worker in a shop → does everything → slow


# Multi Thread:
# - Multiple tasks run together
# - Faster and efficient

# Real-life:
# Restaurant with multiple workers → fast service


# ------------------------------------------------------------
# 🧪 4. PRACTICAL EXAMPLES
# ------------------------------------------------------------

# -------------------------
# Example 1: Single Thread
# -------------------------

import time

def task1():
    print("Task 1 started")
    time.sleep(2)  # simulate waiting
    print("Task 1 finished")

def task2():
    print("Task 2 started")
    time.sleep(2)
    print("Task 2 finished")

# Running tasks one by one (single thread)
task1()
task2()

# Output:
# Task 1 runs first → then Task 2
# Total time ≈ 4 seconds (slow)


# -------------------------
# Example 2: Multi Thread
# -------------------------

import threading

def task():
    print("Task started")
    time.sleep(2)
    print("Task finished")

# Creating threads
t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

# Starting threads
t1.start()
t2.start()

# Waiting for both to finish
t1.join()
t2.join()

# Output:
# Both tasks run "together"
# Total time ≈ 2 seconds (faster)


# ------------------------------------------------------------
# 🧠 5. KEY DIFFERENCE (IMPORTANT)
# ------------------------------------------------------------

# Process:
# - Separate memory
# - Independent
# - Safe but heavy

# Thread:
# - Shared memory
# - Faster
# - Less safe


# ------------------------------------------------------------
# 🎯 FINAL SUMMARY
# ------------------------------------------------------------

# Process = Separate building
# Thread = Workers inside building

# Single thread = One worker → slow
# Multi thread = Multiple workers → fast

# Backend Insight:
# If many users hit API:
# - Single thread → slow
# - Multi thread / async → fast


# ============================================================
# END OF NOTES
# ============================================================