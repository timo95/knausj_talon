from talon import Context, actions

# Context matching
ctx = Context()
ctx.matches = r"""
os: linux
app: thunderbird
"""


# --- Implement actions ---
@ctx.action_class('app')
class AppActions:
    # app.tabs
    def tab_reopen(): actions.key("ctrl-shift-t")  # only works from inbox tab


@ctx.action_class("user")
class UserActions:
    # user.tabs
    def tab_jump(number: int):
        if number <= 9:
            actions.key(f"alt-{number}")

    def tab_final(): actions.key("alt-9")

    # custom actions
    def mod(): return "ctrl"

    def thunderbird_calendar_view(number: int): actions.key(f"ctrl-{number}")
