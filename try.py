 
import jwt
import time

# 🔐 Replace with your real LiveKit Cloud credentials
api_key = "APImu6rzA24doaG"
api_secret = "faaqNcAWks1aEF12Q2DYdHAmqlhCt8ccJueVmO1EfptA"

# 👤 Identity & Room Info
identity = "priya-agent"
room_name = "test-room"
ttl = 3600  # Token time-to-live in seconds

# 🧾 JWT Payload
now = int(time.time())
payload = {
    "iss": api_key,
    "sub": identity,
    "nbf": now,
    "exp": now + ttl,
    "video": {
        "room": room_name,
        "join": True
    }
}

# 🔑 Generate the JWT token
token = jwt.encode(payload, api_secret, algorithm="HS256")

print("🔐 LiveKit Room Token:\n", token)
