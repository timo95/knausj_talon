from talon import Context, actions, scope


# Search result (query "page")
# /search/<number>/
ctx = Context()
ctx.matches = r"""
app: sufficientvelocity
browser.path: /^\/search\/\d+\/?$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(actions.user.browser_url_query().get("page", "1"))
    def page_jump(number: int): actions.user.browser_set_url_query("page", number)


# Thread, forums, tags (subpath 3)
# /threads/<thread>.<number>/[page-<page>]
# /forums/<forum>.<number>/[page-<page>]
# /tags/<tag>/[page-<page>]
ctx = Context()
ctx.matches = r"""
app: sufficientvelocity
browser.path: /^\/(threads|forums)\/[-\w]+\.\d+\/(page-\d+)?$/
browser.path: /^\/tags\/[-\w]+\/(page-\d+)?$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current():
        tokens = scope.get("browser.path").rstrip("/").split("/")
        return int(tokens[3].partition("-")[2]) if len(tokens) > 3 else 1
    def page_jump(number: int):
        tokens = scope.get("browser.path").rstrip("/").split("/")[:3]
        tokens.append(f"page-{str(number)}")
        actions.user.browser_go_path("/".join(tokens), keep_query=True)
    def page_final(): actions.user.page_jump(1000000)


# Reader mode, new stuff (subpath 4)
# /threads/<name>.<number>/reader/[page-<page>]
# /whats-new/<category>/<number>[/page-<page>]
ctx = Context()
ctx.matches = r"""
app: sufficientvelocity
browser.path: /^\/threads\/[-\w]+\.\d+\/reader\/(page-\d+)?$/
browser.path: /^\/whats-new\/(posts|threadmarks|profile-posts)\/\d+(\/(page-\d+)?)?$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current():
        tokens = scope.get("browser.path").rstrip("/").split("/")
        return int(tokens[4].partition("-")[2]) if len(tokens) > 4 else 1
    def page_jump(number: int):
        tokens = scope.get("browser.path").rstrip("/").split("/")[:4]
        tokens.append(f"page-{str(number)}")
        actions.user.browser_go_path("/".join(tokens), keep_query=True)
    def page_final(): actions.user.page_jump(1000000)


# Other reader modes (subpath 5)
# /threads/<name>.<number>/<number_type>/reader/[page-<page>]
ctx = Context()
ctx.matches = r"""
app: sufficientvelocity
browser.path: /^\/threads\/[-\w]+\.\d+\/\d+\/reader\/(page-\d+)?$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current():
        tokens = scope.get("browser.path").rstrip("/").split("/")
        return int(tokens[5].partition("-")[2]) if len(tokens) > 5 else 1
    def page_jump(number: int):
        tokens = scope.get("browser.path").rstrip("/").split("/")[:5]
        tokens.append(f"page-{str(number)}")
        actions.user.browser_go_path("/".join(tokens), keep_query=True)
    def page_final(): actions.user.page_jump(1000000)
