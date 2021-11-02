from talon import Context, actions, scope


# Search results, betareader browser (parameter "ppage")
ctx = Context()
ctx.matches = r"""
app: fanfictionnet
app: fictionpress
browser.path: /^\/search\/$/
browser.path: /^\/betareaders/\w+\/[^\/]+\/?$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(actions.user.browser_url_parameters().get("ppage", "1"))
    def page_jump(number: int):
        if number > 0:
            actions.user.browser_set_url_parameter("ppage", number)


# Story browser (parameter "p")
ctx = Context()
ctx.matches = r"""
app: fanfictionnet
app: fictionpress
browser.path: /^\/\w+\/[^\/]+\/$/
and not browser.path: /^\/(communities|forums|crossovers|betareaders|u)\/[^\/]+\/$/
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


# Community general browser (subpath 5)
ctx = Context()
ctx.matches = r"""
app: fanfictionnet
app: fictionpress
browser.path: /^\/communities\/general\/0\/(\d\/)?(\d\/?)?$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current():
        tokens = scope.get("browser.path").rstrip("/").split("/")
        return int(tokens[5]) if len(tokens) > 5 else 1
    def page_jump(number: int):
        if number > 0:
            tokens = scope.get("browser.path").rstrip("/").split("/")[:4]
            tokens += ["3", str(number), ""][(len(tokens) - 4):]
            actions.user.browser_go_path("/".join(tokens), keep_parameters=True)


# Community browser, forum general browser (subpath 6)
ctx = Context()
ctx.matches = r"""
app: fanfictionnet
app: fictionpress
browser.path: /^\/(communities\/(?!general)\w+|forums\/general)\/[^\/]+\/(\d\/){0,2}(\d\/?)?$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current():
        tokens = scope.get("browser.path").rstrip("/").split("/")
        return int(tokens[6]) if len(tokens) > 6 else 1
    def page_jump(number: int):
        if number > 0:
            tokens = scope.get("browser.path").rstrip("/").split("/")[:6]
            tokens += ["0", "3", str(number), ""][(len(tokens) - 4):]
            actions.user.browser_go_path("/".join(tokens), keep_parameters=True)


# Forum browser (subpath 7)
ctx = Context()
ctx.matches = r"""
app: fanfictionnet
app: fictionpress
browser.path: /^\/forums\/(?!general)\w+\/[^\/]+\/(\d\/){0,3}(\d\/?)?$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current():
        tokens = scope.get("browser.path").rstrip("/").split("/")
        return int(tokens[7]) if len(tokens) > 7 else 1
    def page_jump(number: int):
        if number > 0:
            tokens = scope.get("browser.path").rstrip("/").split("/")[:7]
            tokens += ["0", "3", "0", str(number), ""][(len(tokens) - 4):]
            actions.user.browser_go_path("/".join(tokens), keep_parameters=True)
