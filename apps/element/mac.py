from talon import Context, actions

# Context matching
ctx = Context()
ctx.matches = r"""
os: mac
app: element
"""


# --- Implement actions ---
@ctx.action_class("app")
class AppActions:
    # global (overwrite mac/app.py)
    def window_close(): actions.key("cmd-w")


@ctx.action_class("edit")
class EditActions:
    # edit
    def file_start(): actions.key("cmd-home")
    def file_end(): actions.key("cmd-end")
    def extend_file_start(): actions.key("cmd-shift-home")
    def extend_file_end(): actions.key("cmd-shift-end")


@ctx.action_class("user")
class UserActions:
    # user.messaging
    def messaging_open_channel_picker(): actions.key("cmd-k")
    def messaging_open_search(): actions.key("cmd-f")
    def messaging_upload_file(): actions.key("cmd-shift-u")
