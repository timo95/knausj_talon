from talon import Module, Context, actions

# --- App definitions ---
mod = Module()
mod.apps.adobe_acrobat_reader = """
os: windows
and app.name: Adobe Acrobat Reader DC 
os: windows
and app.exe: AcroRd32.exe
"""

# Context matching
ctx = Context()
ctx.matches = r"""
app: adobe_acrobat_reader
"""


# --- Implement actions ---
@ctx.action_class('app')
class AppActions:
    # app.tabs
    def tab_next(): actions.key('ctrl-tab')
    def tab_previous(): actions.key('ctrl-shift-tab')


@ctx.action_class('edit')
class EditActions:
    def zoom_in(): actions.key("ctrl-0")
    def zoom_out(): actions.key("ctrl-1")
    def zoom_reset(): actions.key("ctrl-2")


@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current():
        actions.key("ctrl-shift-n")
        page = actions.edit.selected_text()
        actions.key("tab:2 enter")
        return int(page)
    def page_next(): actions.key("right")
    def page_previous(): actions.key("left")
    def page_jump(number: int):
        if number > 0:
            actions.key(f"ctrl-shift-n {number} enter")
    def page_final(): actions.key("end")
