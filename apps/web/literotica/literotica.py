from talon import Module

# --- App definition ---
mod = Module()
# not including shop and forum, since those are arguably different websites
mod.apps.literotica = r"""
tag: browser
browser.host: /^((www|tags|search|chat)\.)?literotica.com$/
"""
