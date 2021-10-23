from talon import Module

# App definition
mod = Module()
mod.apps.amazon = r"""
tag: browser
title: /www\.amazon\./
"""

# --- Define lists ---
mod.list("amazon_pages", desc="Pages on Amazon")
