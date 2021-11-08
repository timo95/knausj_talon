from talon import Module, Context, actions

# --- App definition ---
mod = Module()
mod.apps.okular = """
os: linux
and app.name: okular
"""

# Context matching
ctx = Context()
ctx.matches = """
app: okular
"""


# --- Implement actions ---
@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current():
        actions.key("ctrl-g")
        page = actions.edit.selected_text()
        actions.key("escape")
        return int(page)
    def page_next(): actions.key("l")
    def page_previous(): actions.key("h")
    def page_jump(number: int):
        if number > 0:
            actions.key("ctrl-g")
            actions.sleep("100ms")
            actions.insert(str(number))
            actions.key("enter")
    def page_final(): actions.key("ctrl-end")
