from talon import Context, actions

# Context matching
ctx = Context()
ctx.matches = r"""
os: windows
os: linux
app: keepass
app: keepassx
app: keepassxc
"""


# --- Implement actions ---
@ctx.action_class("app")
class AppActions:
    def tab_open(): actions.key("ctrl-o")
    def window_close(): actions.key("ctrl-q")


@ctx.action_class("user")
class UserActions:
    # user.password_manager
    def password_manager_entry_new(): actions.key("ctrl-i")
    def password_manager_entry_clone(): actions.key("ctrl-k")
    def password_manager_password_copy(): actions.key("ctrl-c")
    def password_manager_user_copy(): actions.key("ctrl-b")
    # keepass
    def keepass_database_open(): actions.key("ctrl-o")
    def keepass_database_close(): actions.key("ctrl-w")
    def keepass_database_new(): actions.key("ctrl-n")
    def keepass_database_save(): actions.key("ctrl-s")
    def keepass_database_lock(): actions.key("ctrl-l")

