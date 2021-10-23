from talon import Context, Module

# App definition
mod = Module()
mod.apps.reddit = r"""
tag: browser
title: /www\.reddit\.com/
"""

# Context matching
ctx = Context()
ctx.matches = r"""
app: reddit
"""

# --- Define and implement lists ---
mod.list("subreddits", desc="Subreddits")
ctx.lists["user.subreddits"] = {
    "all": "all",
    "popular": "popular",
}
