from talon import Module, Context, actions

# App definition
mod = Module()
mod.apps.thunderbird = """
app.name: Thunderbird
"""

# Context matching
ctx = Context()
ctx.matches = r"""
app: thunderbird
"""

# Set tags
ctx.tags = ["user.tabs"]


# --- Define actions ---
@mod.action_class
class UserActions:
    def thunderbird_calendar_view(number: int):
        """Select between calendar view tabs"""


# --- Implement actions ---
@ctx.action_class('app')
class AppActions:
    # app.tabs
    # not possible in thunderbird
    def tab_open(): pass
