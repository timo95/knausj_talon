from talon import ui, clip, Context, Module, actions

ctx = Context()
mod = Module()
apps = mod.apps
apps.nautilus = "app.name: Nautilus"
mod.apps.nautilus = """
os: linux
and app.exe: nautilus
os: linux
and app.name: Org.gnome.Nautilus
"""
ctx.matches = r"""
app: nautilus
"""

ctx.tags = ["user.file_manager", "user.tabs"]


@ctx.action_class("user")
class UserActions:
    def tab_jump(number: int): actions.key(f"ctrl-{number}")

    def file_manager_go_back(): actions.key("alt-left")

    def file_manager_go_forward(): actions.key("alt-right")

    def file_manager_open_parent(): actions.key("alt-up")

    def file_manager_show_properties(): actions.key("ctrl-enter")

    def file_manager_open_directory(path: str):
        actions.key("ctrl-l")
        actions.insert(path)
        actions.key("enter")

    def file_manager_new_folder(name: str = None):
        actions.key("ctrl-shift-n")
        if name:
            actions.insert(name)

    def file_manager_terminal_here():
        actions.key("ctrl-l")
        actions.key("ctrl-c")
        ui.launch(path="gnome-terminal", args=["--working-directory={}".format(clip.get())])
