from talon import Context

# Context matching
ctx = Context()
ctx.matches = r"""
app: thunderbird_inbox
"""

# Many single letters are mapped to some action. Remove accidental actions.
ctx.lists["self.letter"] = {}
