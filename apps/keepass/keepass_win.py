from talon import Context, actions


# Context matching
ctx = Context()
ctx.matches = r"""
os: windows
app: keepass
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
    def password_manager_entry_edit(): actions.key("enter")
    def password_manager_entry_clone(): actions.key("ctrl-k")
    def password_manager_entry_copy(): actions.key("ctrl-shift-c")
    def password_manager_entry_paste(): actions.key("ctrl-shift-v")
    def password_manager_entry_delete(): actions.key("delete")
    def password_manager_copy_password(): actions.key("ctrl-c")
    def password_manager_copy_user(): actions.key("ctrl-b")
    def password_manager_copy_url(): actions.key("ctrl-shift-u")
    def password_manager_open_url(): actions.key("ctrl-u")
    def password_manager_fill(): actions.key("ctrl-v")
    # keepass
    def keepass_database_open(): actions.key("ctrl-o")
    def keepass_database_close(): actions.key("ctrl-w")
    def keepass_database_new(): actions.key("ctrl-n")
    def keepass_database_save(): actions.key("ctrl-s")
    def keepass_database_lock(): actions.key("ctrl-l")

