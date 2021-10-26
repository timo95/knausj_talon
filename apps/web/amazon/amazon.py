from talon import Module

# App definition
mod = Module()
mod.apps.amazon = r"""
tag: browser
browser.host: /www\.amazon\./
"""

# --- Define lists ---
mod.list("amazon_pages", desc="Pages on Amazon")
