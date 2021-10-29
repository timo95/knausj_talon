from talon import Module, Context, actions

# --- App definition ---
mod = Module()
mod.apps.fanfictionnet_search = r"""
app: fanfictionnet
app: fictionpress
browser.path: /^\/search\/$/
"""

# Context matching
ctx = Context()
ctx.matches = r"""
app: fanfictionnet_search
"""


# --- Implement actions ---
@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(actions.user.browser_url_parameters().get("ppage", "1"))
    def page_jump(number: int):
        if number > 0:
            actions.user.browser_set_url_parameter("ppage", number)
