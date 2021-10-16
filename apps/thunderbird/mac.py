from talon import Context, actions

# Context matching
ctx = Context()
ctx.matches = r"""
os: mac
app: thunderbird
"""


# --- Implement actions ---
@ctx.action_class('app')
class AppActions:
    def tab_reopen(): actions.key("cmd-shift-t")  # not tested


@ctx.action_class("user")
class UserActions:
    # user.tabs
    def tab_jump(number: int):
        if number <= 9:
            actions.key(f"alt-{number}")  # not tested
    def tab_final(): actions.key("alt-9")  # not tested
    # custom actions
    def thunderbird_calendar_view(number: int): actions.key(f"cmd-{number}")  # not tested
