from talon import Module

# --- App definitions ---
mod = Module()
mod.apps.foobar2000 = """
os: windows
and app.name: foobar2000
os: windows
and app.exe: foobar2000.exe
"""
mod.apps.foobar2000_properties = """
app: foobar2000
title: /^Properties - /
"""

