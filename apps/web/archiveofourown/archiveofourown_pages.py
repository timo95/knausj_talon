from talon import Context, actions

# Stories, search, etc. (query "page")
# /tags/<tag>/works
# /works/search
# /bookmarks/search
# /tags/search
# /people/surge
# /collections
# /users/<user>[/pseuds/<user>]/subscriptions
# /users/<user>[/pseuds/<user>]/readings
# /users/<user>[/pseuds/<user>]/bookmarks
# /users/<user>[/pseuds/<user>]/works
# /users/<user>[/pseuds/<user>]/series
# /users/<user>[/pseuds/<user>]/collections
# /users/<user>[/pseuds/<user>]/gifts
ctx = Context()
ctx.matches = r"""
app: archiveofourown
browser.path: /^\/tags\/[^\/]+\/works\/?$/
browser.path: /^\/(works|bookmarks|tags|people)\/search\/?$/
browser.path: /^\/collections\/?$/
browser.path: /^\/users\/[^\/]+(\/pseuds\/[^\/]+)?\/(subscriptions|readings|bookmarks|works|series|collections|gifts)\/?$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(actions.user.browser_url_query().get("page", "1"))
    def page_jump(number: int): actions.user.browser_set_url_query("page", number)
