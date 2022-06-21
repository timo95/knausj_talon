from talon import Context

# Context matching
ctx = Context()
ctx.matches = r"""
app: thunderbird_inbox
"""

# Many single letters are mapped to some action.
# Remove accidental actions by removing single letters.
# But this will also disable it for search.
ctx.lists["self.letter"] = {}
