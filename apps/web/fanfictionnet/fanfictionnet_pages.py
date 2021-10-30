from talon import Context, actions


# Search results (parameter ppage)
ctx = Context()
ctx.matches = r"""
app: fanfictionnet
app: fictionpress
browser.path: /^\/search\/$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(actions.user.browser_url_parameters().get("ppage", "1"))
    def page_jump(number: int):
        if number > 0:
            actions.user.browser_set_url_parameter("ppage", number)


# Story browser (parameter p)
ctx = Context()
ctx.matches = r"""
app: fanfictionnet
app: fictionpress
browser.path: /^\/\w+\/[^\/]+\/$/
and not browser.path: /^\/(forums|crossovers|betareaders|u)\/\w+\/$/
browser.path: /^\/[^\/]+-Crossovers\/\d+\/\d+\/$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(actions.user.browser_url_parameters().get("p", "1"))
    def page_jump(number: int):
        if number > 0:
            actions.user.browser_set_url_parameter("p", number)
