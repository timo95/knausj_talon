from talon import Context, actions


# Context matching
ctx = Context()
ctx.matches = r"""
os: linux
app: keepassx
"""


@ctx.action_class("user")
class UserActions:
    # user.password_manager
    def password_manager_entry_edit(): actions.key("ctrl-e")
    def password_manager_entry_copy(): actions.key("ctrl-shift-c")
    def password_manager_entry_paste(): actions.key("ctrl-shift-v")
    def password_manager_entry_delete(): actions.key("ctrl-d")
    def password_manager_password_fill(): actions.key("ctrl-v")
    def password_manager_url_copy(): actions.key("ctrl-alt-u")
    def password_manager_url_open(): actions.key("ctrl-u")

