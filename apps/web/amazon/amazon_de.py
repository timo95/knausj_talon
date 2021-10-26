from talon import Context

# Context matching
ctx = Context()
ctx.matches = r"""
app: amazon
user.url_netloc: www.amazon.de
"""

# --- Implement lists ---
domain = "www.amazon.de"
ctx.lists["user.amazon_pages"] = {k: domain + v for k, v in {
    "front": "",
    "cart": "/gp/cart/view.html",
    "wishlist": "/wishlist",
    "deals": "/gp/angebote",
    "orders": "/gp/css/order-history",
    "history": "/gp/history",
}.items()}
