from talon import Context

# Context matching
ctx = Context()
ctx.matches = r"""
app: amazon
title: /www\.amazon\.de/
"""

# --- Implement lists ---
ctx.lists["user.amazon_pages"] = {
    "front": "www.amazon.de",
    "cart": "www.amazon.de/gp/cart/view.html",
    "wishlist": "www.amazon.de/wishlist",
    "deals": "www.amazon.de/gp/angebote",
    "orders": "www.amazon.de/gp/css/order-history",
    "history": "www.amazon.de/gp/history",
}
