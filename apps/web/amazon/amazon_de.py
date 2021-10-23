from talon import Context

# Context matching
ctx = Context()
ctx.matches = r"""
app: amazon
win.title: /www\.amazon\.de/
"""

# --- Implement lists ---
ctx.lists["user.amazon_pages"] = {
    "front": "www.amazon.de",
    "cart": "www.amazon.de/gp/cart/view.html",
    "wishlist": "www.amazon.de/wishlist",
    "offers": "www.amazon.de/gp/angebote",
}
