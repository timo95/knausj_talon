from talon import Context

# Context matching
ctx = Context()
ctx.matches = r"""
app: amazon
title: /www\.amazon\.co\.jp/
"""

# --- Implement lists ---
ctx.lists["user.amazon_pages"] = {
    "front": "www.amazon.co.jp",
    "cart": "www.amazon.co.jp/gp/cart/view.html",
    "wishlist": "www.amazon.co.jp/wishlist",
    "deals": "www.amazon.co.jp/goldbox",
    "orders": "www.amazon.co.jp/gp/css/order-history",
    "history": "www.amazon.co.jp/gp/history",
}
