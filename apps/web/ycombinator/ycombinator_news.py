from talon import Module, Context, actions

# --- App definitions ---
mod = Module()
mod.apps.ycombinator_news = """
tag: browser
browser.host: news.ycombinator.com
"""

# Context matching
ctx = Context()
ctx.matches = r"""
app: ycombinator_news
"""


# --- Implement actions ---
@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(actions.user.browser_url_parameters().get("p", "1"))
    def page_jump(number: int):
        if number > 0:
            actions.user.browser_set_url_parameter("p", number)
