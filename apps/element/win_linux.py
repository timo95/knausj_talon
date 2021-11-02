from talon import Context, actions

# Context matching
ctx = Context()
ctx.matches = r"""
os: windows
os: linux
app: element
"""


# --- Implement actions ---
@ctx.action_class("app")
class AppActions:
    # global (overwrite win/app.py and linux/app.py)
    def window_close(): actions.key("ctrl-w")


@ctx.action_class("edit")
class EditActions:
    # edit
    def file_start(): actions.key("ctrl-home")
    def file_end(): actions.key("ctrl-end")
    def extend_file_start(): actions.key("ctrl-shift-home")
    def extend_file_end(): actions.key("ctrl-shift-end")


@ctx.action_class("user")
class UserActions:
    # user.messaging
    def messaging_open_channel_picker(): actions.key("ctrl-k")
    def messaging_open_search(): actions.key("ctrl-f")
    def messaging_upload_file(): actions.key("ctrl-shift-u")
