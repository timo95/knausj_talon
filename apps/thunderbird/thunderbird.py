from talon import Context, Module, actions

ctx = Context()
mod = Module()
apps = mod.apps
apps.thunderbird = "app.name: Thunderbird"
mod.apps.thunderbird = """
app.name: Thunderbird
"""
ctx.matches = r"""
app: thunderbird
"""


@ctx.action_class('app')
class AppActions:
    def tab_open(): pass  # doesn't exist

    def tab_reopen(): actions.key("ctrl-shift-t")  # doesn't work?


@ctx.action_class("user")
class UserActions:
    def tab_jump(number: int):
        if number <= 9:
            actions.key("alt-{}".format(number))

    def tab_final(): actions.key("alt-9")
