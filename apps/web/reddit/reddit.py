from talon import Context, Module

# App definition
mod = Module()
mod.apps.reddit = r"""
tag: browser
browser.host: www.reddit.com
"""

# Context matching
ctx = Context()
ctx.matches = r"""
app: reddit
"""

# --- Define and implement lists ---
mod.list("subreddit", desc="Subreddits")
ctx.lists["user.subreddit"] = {
    "all": "all",
    "popular": "popular",
}
