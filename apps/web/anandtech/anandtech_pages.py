from talon import Context, actions, scope

# Main page (subpath 2)
# /[Page/<page>]
ctx = Context()
ctx.matches = r"""
app: anandtech
browser.path: /^\/(Page\/\d+\/?)?$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current():
        tokens = scope.get("browser.path").rstrip("/").split("/")
        return int(tokens[2]) if len(tokens) > 2 else 1
    def page_jump(number: int):
        if number > 0:
            tokens = scope.get("browser.path").rstrip("/").split("/")[:2]
            tokens += ["Page", str(number)][(len(tokens) - 1):]
            actions.user.browser_go_path("/".join(tokens), keep_query=True)


# Tag pages (subpath 3)
# /tag/<tag>[/<page>]
ctx = Context()
ctx.matches = r"""
app: anandtech
browser.path: /^\/tag\/\w+(\/\d+\/?)?$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current():
        tokens = scope.get("browser.path").rstrip("/").split("/")
        return int(tokens[3]) if len(tokens) > 3 else 1
    def page_jump(number: int):
        if number > 0:
            tokens = scope.get("browser.path").rstrip("/").split("/")[:3]
            tokens.append(str(number))
            actions.user.browser_go_path("/".join(tokens), keep_query=True)
