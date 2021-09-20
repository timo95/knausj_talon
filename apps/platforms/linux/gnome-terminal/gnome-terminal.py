from talon import Context, actions

ctx = Context()
ctx.matches = r"""
app.name: Gnome-terminal
"""

@ctx.action_class("user")
class user_actions:
    # tabs-tag functions implementations
    def tab_jump(number):
        actions.key("alt-{}".format(number))

@ctx.action_class("app")
class app_actions:
    # tabs-tag functions implementations
    def tab_open():
        actions.key("ctrl-shift-t")

    def tab_previous():
        actions.key("ctrl-pageup")

    def tab_next():
        actions.key("ctrl-pagedown")

    def tab_close():
        actions.key("ctrl-shift-w")

    def window_open():
        actions.key('ctrl-shift-n')

# this overwrites the unfitting parts of linux/edit.py
@ctx.action_class('edit')
class EditActions:
    def page_down():
        actions.key('shift-pagedown')
    def page_up():
        actions.key('shift-pageup')
    def paste():
        actions.key('ctrl-shift-v')
    def copy():
        actions.key('ctrl-shift-c')
    def find(text: str):
        actions.key('ctrl-shift-f')
        if str:
            actions.insert(text)
