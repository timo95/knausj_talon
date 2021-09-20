from talon import Context, Module, actions

ctx = Context()
mod = Module()
apps = mod.apps
apps.slack = "app.name: Element"
mod.apps.slack = """
and app.name: Element
os: windows
and app.exe: Element.exe
"""
ctx.matches = r"""
app: element
"""


@ctx.action_class("edit")
class EditActions:
    def line_insert_down():
        actions.edit.line_end()
        actions.key("shift-enter")


@ctx.action_class("user")
class UserActions:
    def messaging_workspace_previous():
        pass

    def messaging_workspace_next():
        pass

    def messaging_open_channel_picker():
        actions.key("ctrl-k")

    def messaging_channel_previous():
        actions.key("alt-up")

    def messaging_channel_next():
        actions.key("alt-down")

    def messaging_unread_previous():
        actions.key("alt-shift-up")

    def messaging_unread_next():
        actions.key("alt-shift-down")

    def messaging_open_search():
        actions.key("ctrl-f")

    def messaging_mark_workspace_read():
        pass

    def messaging_mark_channel_read():
        actions.key("esc")

    # Files and Snippets
    def messaging_upload_file():
        pass
