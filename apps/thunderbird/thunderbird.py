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


# --- Implement actions ---
@ctx.action_class('app')
class AppActions:
    # app.tabs
    # doesn't exist
    def tab_open(): pass


@ctx.action_class("user")
class UserActions:
    # user.tabs
    def tab_jump(number: int):
        if number <= 9:
            actions.key("alt-{}".format(number))
    def tab_final(): actions.key("alt-9")
