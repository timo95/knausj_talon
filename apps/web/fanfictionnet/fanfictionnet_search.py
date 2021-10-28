from talon import Module, Context, scope, actions

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
    def page_current(): return int(actions.user.get_parameters().get("ppage", "1"))
    def page_jump(number: int):
        parameters = actions.user.get_parameters()
        parameters["ppage"] = number
        prefix = scope.get('browser.host') + scope.get('browser.path')
        actions.browser.go(f"{prefix}?{'&'.join(f'{k}={v}' for k, v in parameters.items())}")
