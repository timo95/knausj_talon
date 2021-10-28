from talon import Context, Module, actions

# --- App definition ---
mod = Module()
mod.apps.element = """
app.name: Element
os: windows
and app.exe: Element.exe
"""

# Context matching
ctx = Context()
ctx.matches = r"""
app: element
"""


# --- Implement actions ---
@ctx.action_class("edit")
class EditActions:
    # edit
    def line_insert_down():
        actions.edit.line_end()
        actions.key("shift-enter")
    def file_start():
        actions.key("ctrl-home")
    def file_end():
        actions.key("ctrl-end")
    def extend_file_start():
        actions.key("ctrl-shift-home")
    def extend_file_end():
        actions.key("ctrl-shift-end")


@ctx.action_class("user")
class UserActions:
    # user.messaging
    def messaging_workspace_previous(): pass
    def messaging_workspace_next(): pass
    def messaging_open_channel_picker(): actions.key("ctrl-k")
    def messaging_channel_previous(): actions.key("alt:down up alt:up")
    def messaging_channel_next(): actions.key("alt:down down alt:up")
    def messaging_unread_previous(): actions.key("alt-shift-up")
    def messaging_unread_next(): actions.key("alt-shift-down")
    def messaging_open_search(): actions.key("ctrl-f")
    def messaging_mark_workspace_read(): pass
    def messaging_mark_channel_read(): actions.key("esc")
    def messaging_upload_file(): actions.key("ctrl-shift-u")
