from talon import Context, actions

# Search result (query "page")
# /s
# /-/<lang>/s
ctx = Context()
ctx.matches = r"""
app: amazon
browser.path: /^(\/-\/\w+)?\/s$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(actions.user.browser_url_query().get("page", "1"))
    def page_jump(number: int): actions.user.browser_set_url_query("page", number)
