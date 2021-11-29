from talon import Context, actions


# Context matching
ctx = Context()
ctx.matches = r"""
os: windows
app: keepass
"""


@ctx.action_class("user")
class UserActions:
    # user.password_manager
    def password_manager_entry_edit(): actions.key("enter")
    def password_manager_entry_copy(): actions.key("ctrl-shift-c")
    def password_manager_entry_paste(): actions.key("ctrl-shift-v")
    def password_manager_entry_delete(): actions.key("delete")
    def password_manager_password_fill(): actions.key("ctrl-v")
    def password_manager_url_copy(): actions.key("ctrl-shift-u")
    def password_manager_url_open(): actions.key("ctrl-u")

