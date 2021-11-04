from talon import Context, actions, scope

# Browser (query "page")
ctx = Context()
ctx.matches = r"""
app: exhentai
browser.path: /
browser.path: /torrents.php
browser.path: /favorites.php
browser.path: /watched
browser.path: /bounty.php
browser.path: /toplist.php
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(actions.user.browser_url_query().get("page", "0")) + 1
    def page_jump(number: int):
        if number > 0:
            actions.user.browser_set_url_query("page", number - 1)


# Story overview (query "p")
# /g/<number>/<code>/
ctx = Context()
ctx.matches = r"""
app: exhentai
browser.path: /^\/g\/[\d]+\/[\w]+\/$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(actions.user.browser_url_query().get("p", "0")) + 1
    def page_jump(number: int):
        if number > 0:
            actions.user.browser_set_url_query("p", number - 1)
    def page_final(): actions.user.page_jump(100000)


# Tag search (subpath 3)
# /tag/<tag>[/<page>]
ctx = Context()
ctx.matches = r"""
app: exhentai
browser.path: /^\/tag\/[\w:+]+(\/\d*)?$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current():
        tokens = scope.get("browser.path").rstrip("/").split("/")
        return int(tokens[3]) + 1 if len(tokens) > 3 else 1
    def page_jump(number: int):
        if number > 0:
            tokens = scope.get("browser.path").rstrip("/").split("/")[:3]
            tokens.append(str(number - 1))
            actions.user.browser_go_path("/".join(tokens), keep_query=True)


# Reader (keys a/d)
# /s/<string>/<number>-<page>
ctx = Context()
ctx.matches = r"""
app: exhentai
browser.path: /^\/s\/[\w:]+\/\d+-\d+/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(scope.get("browser.path").split("/")[3].partition("-")[2])
    def page_next(): actions.key("d")
    def page_previous(): actions.key("a")
