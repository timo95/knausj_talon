from talon import Module, Context, scope, actions

# --- App definition ---
mod = Module()
mod.apps.fanfictionnet = """
tag: browser
browser.host: www.fanfiction.net
browser.host: m.fanfiction.net
browser.host: www.fictionpress.com
browser.host: m.fictionpress.com
"""

# Context matching
ctx = Context()
ctx.matches = r"""
app: fanfictionnet
"""


# --- Implement actions ---
@ctx.action_class("user")
class UserActions:
    # user.chapters
    def chapter_current(): return int(scope.get("browser.path").split("/")[3])
    def chapter_jump(number: int):
        tokens = scope.get("browser.path").split("/")
        tokens[3] = str(number)
        actions.browser.go(scope.get("browser.host") + "/".join(tokens))
