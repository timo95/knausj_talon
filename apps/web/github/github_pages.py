from talon import Context, actions

# Issues, pull requests (query "page")
ctx = Context()
ctx.matches = r"""
app: github
browser.path: /^\/[-\w]+\/[-\w]+\/(issues|pulls)\/?/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(actions.user.browser_url_query().get("page", "1"))
    def page_jump(number: int):
        if number > 0:
            actions.user.browser_set_url_query("page", number)
