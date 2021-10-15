from talon import Context, actions

# Context matching
ctx = Context()
ctx.matches = r"""
os: windows
os: linux
app: thunderbird
"""


# --- Implement actions ---
@ctx.action_class('app')
class AppActions:
    def tab_reopen(): actions.key("ctrl-shift-t")  # doesn't work?
