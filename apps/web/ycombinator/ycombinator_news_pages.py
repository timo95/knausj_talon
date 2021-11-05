from talon import Context, actions

# Article lists, comments, etc. (query "p")
ctx = Context()
ctx.matches = r"""
app: ycombinator_news
browser.path: /^\/(|item|news|newest|front|newcomments|ask|show|best|active|bestcomments)$/
"""
ctx.tags = ["user.pages"]

# --- Implement actions ---
@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(actions.user.browser_url_query().get("p", "1"))
    def page_jump(number: int):
        if number > 0:
            actions.user.browser_set_url_query("p", number)
