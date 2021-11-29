from talon import Context, actions


# Context matching
ctx = Context()
ctx.matches = r"""
os: windows
app: keepassxc
"""


@ctx.action_class("user")
class UserActions:
    # user.password_manager
    def password_manager_entry_edit(): actions.key("ctrl-e")
    def password_manager_entry_delete(): actions.key("delete")
    def password_manager_password_fill(): actions.key("ctrl-shift-v")
    def password_manager_url_copy(): actions.key("ctrl-u")
    def password_manager_url_open(): actions.key("ctrl-shift-u")

