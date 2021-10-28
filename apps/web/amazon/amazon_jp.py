from talon import Context

# Context matching
ctx = Context()
ctx.matches = r"""
app: amazon
browser.host: www.amazon.co.jp
"""

# --- Implement lists ---
ctx.lists["user.amazon_page"] = {
    "front": "",
    "cart": "gp/cart/view.html",
    "wishlist": "wishlist",
    "deals": "goldbox",
    "orders": "gp/css/order-history",
    "history": "gp/history",
}
