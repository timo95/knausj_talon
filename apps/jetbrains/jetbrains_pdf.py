from talon import Context, Module, actions

# --- App definition ---
mod = Module()
mod.apps.jetbrains_pdf = """
app: jetbrains
code.language: pdf
"""

# Context matching
ctx = Context()
ctx.matches = """
app: jetbrains_pdf
"""


# --- Implement actions ---
@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_next(): actions.key("ctrl-right")
    def page_previous(): actions.key("ctrl-left")
    def page_final(): actions.key("end")
