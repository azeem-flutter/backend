"""
============================================================
🔷 CLIENT-SERVER ARCHITECTURE (DEEP DIVE)
============================================================

This file explains:
- What is Client-Server Architecture
- Internal flow (step-by-step)
- Layers of backend
- Stateless vs Stateful (deep understanding)
- Real-world system behavior
- Differences & trade-offs
"""

# ============================================================
# 💡 WHAT IS CLIENT-SERVER ARCHITECTURE?
# ============================================================

"""
A system where:

CLIENT → Sends request
SERVER → Processes request
DATABASE → Stores data

------------------------------------------------------------

🧠 REAL EXAMPLE:

You open a website and click "View Profile"

Client sends:
GET /profile

Server:
- Checks authentication
- Fetches data from database

Database:
- Returns user data

Server:
- Sends response

Client:
- Shows profile UI

------------------------------------------------------------
IMPORTANT:
Client NEVER talks directly to database
Server acts as MIDDLEMAN
"""

# ============================================================
# 🔄 HOW IT WORKS INTERNALLY (ADVANCED FLOW)
# ============================================================

"""
1. Client sends HTTP request

2. DNS resolves domain → IP

3. Request goes through Internet

4. Load Balancer (in big systems)
   - Distributes traffic

5. API Gateway (optional)
   - Central entry point

6. Backend Server receives request

7. Middleware runs:
   - Authentication
   - Logging
   - Validation

8. Router:
   - Matches endpoint

9. Controller:
   - Handles request

10. Service Layer:
    - Business logic

11. Repository:
    - DB query execution

12. Database:
    - Returns data

13. Response goes back same path

------------------------------------------------------------
🔥 THIS FLOW IS VERY IMPORTANT FOR INTERVIEW
"""

# ============================================================
# 🔷 BACKEND LAYERS (VERY IMPORTANT)
# ============================================================

"""
1. ROUTER
   - Defines endpoints

2. CONTROLLER
   - Handles request/response
   - Validates input

3. SERVICE (CORE LOGIC 🔥)
   - Business rules
   Example:
   "User can only book one token per day"

4. REPOSITORY
   - Database interaction

------------------------------------------------------------
WHY LAYERS?

- Clean code
- Easy testing
- Scalable system
"""

# ============================================================
# ⚖️ STATELESS vs STATEFUL (DEEP)
# ============================================================

"""
🔹 STATELESS SYSTEM

Definition:
Server does NOT store client state

Each request contains everything needed

Example:
GET /profile
Authorization: Bearer token

------------------------------------------------------------
HOW IT WORKS?

- Token contains user info
- Server verifies token each time
- No memory used on server

------------------------------------------------------------
ADVANTAGES:

- Highly scalable
- Easy to distribute requests
- No session storage needed

------------------------------------------------------------
DISADVANTAGES:

- Slightly more processing per request

------------------------------------------------------------

🔹 STATEFUL SYSTEM

Definition:
Server stores client session

Example:
User logs in → server stores session in memory

Next request:
GET /profile
Session ID sent

------------------------------------------------------------
HOW IT WORKS?

- Server remembers user
- Uses session storage

------------------------------------------------------------
ADVANTAGES:

- Faster repeated requests
- Easier logic sometimes

------------------------------------------------------------
DISADVANTAGES:

- Hard to scale
- Requires session storage
- Server memory usage

------------------------------------------------------------

🧠 DIFFERENCE (IMPORTANT)

Stateless:
- Used in REST APIs
- JWT-based auth

Stateful:
- Used in traditional apps
- Session-based auth

------------------------------------------------------------
🔥 MODERN BACKENDS → STATELESS
"""

# ============================================================
# 🔥 REAL PROJECT EXAMPLE
# ============================================================

"""
Passport Token App:

Client:
- User selects date

Server:
- Checks if slot available

Database:
- Stores booking

Server:
- Returns confirmation

------------------------------------------------------------
Key Learning:
Always separate:
Client → Server → Database
"""

# ============================================================
# 🧠 INTERVIEW QUESTIONS
# ============================================================

"""
Q: Explain client-server architecture?
Q: What is request lifecycle?
Q: Stateless vs Stateful?
Q: Why layered architecture?

👉 Practice explaining without notes
"""
