from talon import Module, Context, actions

# --- App definition ---
mod = Module()
mod.apps.thorium_reader = """
os: linux
and app.name: EDRLab.ThoriumReader
"""

# Context matching
ctx = Context()
ctx.matches = """
app: thorium_reader
"""


# --- Implement actions ---
@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_next(): actions.key("ctrl-.")
    def page_previous(): actions.key("ctrl-,")
    def page_final(): actions.key("ctrl-end")
    # user.chapters
    def chapter_next(): actions.key("ctrl-pagedown")
    def chapter_previous(): actions.key("ctrl-pageup")
