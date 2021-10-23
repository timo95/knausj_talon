from talon import Context

# Context matching
ctx = Context()
ctx.matches = r"""
app: amazon
win.title: /www\.amazon\.com/
"""

# --- Implement lists ---
ctx.lists["user.amazon_pages"] = {
    "front": "www.amazon.com",
    "cart": "www.amazon.com/gp/cart/view.html",
    "wishlist": "www.amazon.com/wishlist",
    "offers": "www.amazon.com/events/epicdeals",
}
