from talon import Context, Module, actions

# --- App definition ---
mod = Module()
mod.apps.firefox_pdf = r"""
app: firefox
tag: browser
title: /\.pdf(\s|$)/
"""
# TODO: Does not work: browser.path: /\.pdf$/

# Context matching
ctx = Context()
ctx.matches = """
os: windows
os: linux
app: firefox_pdf
"""

# --- Implement actions ---
@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current():
        actions.key("ctrl-alt-g")
        page = actions.edit.selected_text()
        actions.key("tab")
        return int(page)
    def page_next(): actions.key("n")
    def page_previous(): actions.key("p")
    def page_jump(number: int):
        if number > 0:
            actions.key("ctrl-alt-g")
            actions.insert(str(number))
            actions.key("enter tab")
    def page_final(): actions.key("end")
