"""
============================================================
🔷 HTTP (DEEP DIVE)
============================================================

This file explains:
- HTTP structure
- Methods (deep)
- Headers, Cookies, Tokens
- Query params, Path params, Body
- Idempotency
- Caching
"""

# ============================================================
# 💡 WHAT IS HTTP?
# ============================================================

"""
HTTP = Communication protocol

Client ↔ Server communication rules

------------------------------------------------------------
REQUEST STRUCTURE:

1. Request Line
2. Headers
3. Body
"""

# ============================================================
# 🔑 HTTP METHODS (DEEP UNDERSTANDING)
# ============================================================

"""
GET:
- Fetch data
- No body

POST:
- Create new resource
- Not idempotent

PUT:
- Full update
- Idempotent

PATCH:
- Partial update

DELETE:
- Remove resource
- Idempotent
"""

# ============================================================
# 🔥 URL STRUCTURE (IMPORTANT)
# ============================================================

"""
Example:
https://api.com/users/123?active=true

Breakdown:

/users/123 → PATH PARAM
?active=true → QUERY PARAM
"""

# ============================================================
# 🔹 PATH PARAMS vs QUERY PARAMS
# ============================================================

"""
PATH PARAM:
- Identifies resource

Example:
GET /users/123

------------------------------------------------------------

QUERY PARAM:
- Filters/modifies result

Example:
GET /users?age=25

------------------------------------------------------------

🔥 DIFFERENCE:

Path:
- Required
- Identifies resource

Query:
- Optional
- Filters data
"""

# ============================================================
# 🔹 REQUEST BODY
# ============================================================

"""
Used in POST/PUT/PATCH

Contains actual data

Example:
{
  "name": "Azeem"
}
"""

# ============================================================
# 🔹 HEADERS (DEEP)
# ============================================================

"""
Headers = Metadata

Examples:

Authorization → security
Content-Type → format
Cache-Control → caching
Accept → response type

------------------------------------------------------------
WHY IMPORTANT?

- Security
- Performance
- Data handling
"""

# ============================================================
# 🔹 COOKIES vs TOKENS
# ============================================================

"""
COOKIES:
- Stored in browser
- Automatic sending

TOKENS:
- Stored in frontend
- Sent manually

------------------------------------------------------------
MODERN SYSTEMS → TOKENS (JWT)
"""

# ============================================================
# 🔥 IDEMPOTENCY (VERY IMPORTANT)
# ============================================================

"""
Definition:
Same request → same result

GET → Yes
PUT → Yes
DELETE → Yes
POST → No

------------------------------------------------------------
WHY IMPORTANT?

- Prevent duplicate actions
- Safe retries
"""

# ============================================================
# 🔥 CACHING
# ============================================================

"""
Purpose:
Reduce server load

Example:
Cache-Control: max-age=3600

------------------------------------------------------------
HOW IT WORKS?

- Response stored in browser
- Next request served from cache
"""

# ============================================================
# 🧠 INTERVIEW QUESTIONS
# ============================================================

"""
Q: Difference between GET and POST?
Q: What are headers?
Q: Path vs Query params?
Q: What is idempotency?
Q: What is caching?
"""