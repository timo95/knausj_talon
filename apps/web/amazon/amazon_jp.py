from talon import Context

# Context matching
ctx = Context()
ctx.matchces = r"""
app: amazon
browser.host: www.amazon.co.jp
"""

# --- Implement lists ---
domain = "www.amazon.co.jp"
ctx.lists["user.amazon_pages"] = {k: domain + v for k, v in {
    "front": "",
    "cart": "/gp/cart/view.html",
    "wishlist": "/wishlist",
    "deals": "/goldbox",
    "orders": "/gp/css/order-history",
    "history": "/gp/history",
}.items()}
