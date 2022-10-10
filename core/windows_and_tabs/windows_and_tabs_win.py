# defines the default app actions for windows

from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: windows
"""


@ctx.action_class("app")
class AppActions:
    # app.preferences()

    def tab_close():
        actions.key("ctrl-w")
        # action(app.tab_detach):
        #  Move the current tab to a new window

    def tab_next():
        actions.key("ctrl-tab")

    def tab_open():
        actions.key("ctrl-t")

    def tab_previous():
        actions.key("ctrl-shift-tab")

    def tab_reopen():
        actions.key("ctrl-shift-t")

    def window_close():
        actions.key("alt-f4")

    def window_hide():
        actions.key("alt-space n")

    def window_hide_others():
        actions.key("super-home")
        # requires easy window switcher or equivalent (built into most Linux)

    def window_next():
        actions.key("alt-^")

    def window_open():
        actions.key("ctrl-n")
        # requires easy window switcher or equivalent (built into most Linux)

    def window_previous():
        actions.key("alt-shift-^")


@ctx.action_class("user")
class UserActions:
    def window_maximize():
        actions.key("super-up")
    def window_restore():
        actions.key("super-up super-down")
    def window_menu():
        actions.key("alt-space")
    def window_overview():
        actions.key("super-tab")
