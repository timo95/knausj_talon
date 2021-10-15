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
    def tab_reopen(): actions.key("cmd-shift-t")  # doesn't work?
