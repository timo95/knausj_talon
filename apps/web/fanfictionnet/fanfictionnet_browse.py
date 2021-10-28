from talon import Module, Context, scope, actions

# --- App definition ---
mod = Module()
mod.apps.fanfictionnet_browse = r"""
app: fanfictionnet
app: fictionpress
browser.path: /^\/\w+\/[^\/]+\/$/
and not browser.path: /^\/(forums|crossovers|betareaders|u)\/\w+\/$/
browser.path: /^\/[^\/]+-Crossovers\/\d+\/\d+\/$/
"""

# Context matching
ctx = Context()
ctx.matches = r"""
app: fanfictionnet_browse
"""


# --- Implement actions ---
@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(actions.user.get_parameters().get("p", "1"))
    def page_jump(number: int):
        parameters = actions.user.get_parameters()
        parameters["p"] = number
        prefix = scope.get('browser.host') + scope.get('browser.path')
        actions.browser.go(f"{prefix}?{'&'.join(f'{k}={v}' for k, v in parameters.items())}")
