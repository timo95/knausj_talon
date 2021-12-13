from talon import Context, actions

# Story, popular, new (query "page")
# /s/<name>
# /top/<category>[/<time_period>/]
ctx = Context()
ctx.matches = r"""
app: literotica
browser.path: /^\/s\/[-\w]+\/?$/
browser.path: /^\/top\/[-\w]+(\/((alltime|last-12-months|last-30-days)\/?)?)?$/
browser.path: /stories/new_submissions.php
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(actions.user.browser_url_query().get("page", "1"))
    def page_jump(number: int): actions.user.browser_set_url_query("page", number)


# Search (query "page")
# search.literotica.com/
ctx = Context()
ctx.matches = r"""
browser.host: search.literotica.com
browser.path: /
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(actions.user.browser_url_query().get("page", "1"))
    def page_jump(number: int): actions.user.browser_set_url_query("page", number)


# Tag (query "page")
# tags.literotica.com/<tag>
ctx = Context()
ctx.matches = r"""
browser.host: tags.literotica.com
browser.path: /^\/[-\w]+\/?$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(actions.user.browser_url_query().get("page", "1"))
    def page_jump(number: int): actions.user.browser_set_url_query("page", number)
