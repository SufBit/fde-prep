import requests

r = requests.get("https://api.github.com/users/SufBit", timeout=10)
print(r.headers["X-RateLimit-Limit"], r.headers["X-RateLimit-Remaining"])