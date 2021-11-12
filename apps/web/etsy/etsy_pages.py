from talon import Context, actions

# Search, category, shop, listing, people (query "page")
# [/<language>]/search(/<category>)*
# [/<language>]/c(/<category>)+
# [/<language>]/shop/<shop>
# [/<language>]/shop/<shop>/sold
# [/<language>]/shop/<shop>/favoriters
# [/<language>]/listing/<number>/<name>/favoriters
# [/<language>]/people/<username>/favorites/recent-listings
# [/<language>]/people/<username>/circle
ctx = Context()
ctx.matches = r"""
app: etsy
browser.path: /^(\/\w+)?\/search(\/[-\w]+)*\/?$/
browser.path: /^(\/\w+)?\/c(\/[-\w]+)+\/?$/
browser.path: /^(\/\w+)?\/shop\/[^\/]+(|\/sold|\/favoriters)\/?$/
browser.path: /^(\/\w+)?\/listing\/\d+\/[-\w]+\/favoriters\/?$/
browser.path: /^(\/\w+)?\/people\/[^\/]+\/(favorites\/recent-listings|circle)\/?$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(actions.user.browser_url_query().get("page", "1"))
    def page_jump(number: int):
        if number > 0:
            actions.user.browser_set_url_query("page", number)
