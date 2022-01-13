from talon import Context, actions

# Issues, pull requests (query "page")
# /<user>/<repository>/issues
# /<user>/<repository>/pulls
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
    def page_jump(number: int): actions.user.browser_set_url_query("page", number)


# Search (query "p")
# [/<user>/<repository>]/search
ctx = Context()
ctx.matches = r"""
app: github
browser.path: /^(\/[-\w]+\/[-\w]+)?\/search\/?/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(actions.user.browser_url_query().get("p", "1"))
    def page_jump(number: int): actions.user.browser_set_url_query("p", number)
