from talon import Context

# Context matching
ctx = Context()
ctx.matches = r"""
app: amazon
title: /www\.amazon\.com/
"""

# --- Implement lists ---
ctx.lists["user.amazon_pages"] = {
    "front": "www.amazon.com",
    "cart": "www.amazon.com/gp/cart/view.html",
    "wishlist": "www.amazon.com/wishlist",
    "deals": "www.amazon.com/events/epicdeals",
    "orders": "www.amazon.com/gp/css/order-history",
    "history": "www.amazon.com/gp/history",
}
