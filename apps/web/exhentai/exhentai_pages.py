from talon import Context, actions, scope

# Browser (parameter "page")
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
    def page_current(): return int(actions.user.browser_url_parameters().get("page", "0")) + 1
    def page_jump(number: int):
        if number > 0:
            actions.user.browser_set_url_parameter("page", number - 1)


# Story overview (parameter "p")
ctx = Context()
ctx.matches = r"""
app: exhentai
browser.path: /^\/g\/[\d]+\/[\w]+\/$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(actions.user.browser_url_parameters().get("p", "0")) + 1
    def page_jump(number: int):
        if number > 0:
            actions.user.browser_set_url_parameter("p", number - 1)
    def page_final(): actions.user.page_jump(100000)


# Tag search (subpath 3)
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
            tokens += [str(number - 1)][(len(tokens) - 3):]
            actions.user.browser_go_path("/".join(tokens), keep_parameters=True)


# Reader (keys a/d)
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
