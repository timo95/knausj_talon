from talon import ui, clip, Context, Module, actions

# App definition
mod = Module()
mod.apps.amazon = """
tag: browser
win.title: /www\.amazon\./
"""

# --- Define lists ---
mod.list("amazon_pages", desc="Pages on Amazon")
