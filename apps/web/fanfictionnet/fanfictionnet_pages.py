from talon import Context, actions, scope


# Search results, betareader browser (query "ppage")
# /search/
# /betareaders/all/<category>
# /betareaders/<category>/<fandom>
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
    def page_current(): return int(actions.user.browser_url_query().get("ppage", "1"))
    def page_jump(number: int): actions.user.browser_set_url_query("ppage", number)


# Story browser (query "p")
# /<category>/<fandom>/
# /<crossover_fandom>/<number>/<number>/
ctx = Context()
ctx.matches = r"""
app: fanfictionnet
app: fictionpress
browser.path: /^\/(?!(communities|forums|crossovers|betareaders|u)\/)\w+\/[^\/]+\/$/
browser.path: /^\/[^\/]+-Crossovers\/\d+\/\d+\/$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current(): return int(actions.user.browser_url_query().get("p", "1"))
    def page_jump(number: int): actions.user.browser_set_url_query("p", number)


# Community general browser (subpath 5)
# /communities/general/<number_lang>/[<number_sort>/<page>]
ctx = Context()
ctx.matches = r"""
app: fanfictionnet
app: fictionpress
browser.path: /^\/communities\/general\/\d\/(\d\/)?(\d+\/?)?$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current():
        tokens = scope.get("browser.path").rstrip("/").split("/")
        return int(tokens[5]) if len(tokens) > 5 else 1
    def page_jump(number: int):
        tokens = scope.get("browser.path").rstrip("/").split("/")[:4]
        tokens += ["3", str(number), ""][(len(tokens) - 4):]
        actions.user.browser_go_path("/".join(tokens), keep_query=True)


# Community browser (subpath 6)
# /communities/<category>/<fandom>/[<number_lang>/<number_sort>/<page>]
ctx = Context()
ctx.matches = r"""
app: fanfictionnet
app: fictionpress
browser.path: /^\/communities\/(?!general)\w+\/[^\/]+\/(\d\/){0,2}(\d+\/?)?$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current():
        tokens = scope.get("browser.path").rstrip("/").split("/")
        return int(tokens[6]) if len(tokens) > 6 else 1
    def page_jump(number: int):
        tokens = scope.get("browser.path").rstrip("/").split("/")[:6]
        tokens += ["0", "3", str(number), ""][(len(tokens) - 4):]
        actions.user.browser_go_path("/".join(tokens), keep_query=True)


# Forum general browser (subpath 6)
# /forums/general/<number_lang>/[<number_sort>/<number_type>/<page>]
ctx = Context()
ctx.matches = r"""
app: fanfictionnet
app: fictionpress
browser.path: /^\/forums\/general\/[^\/]+\/(\d\/){0,2}(\d+\/?)?$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current():
        tokens = scope.get("browser.path").rstrip("/").split("/")
        return int(tokens[6]) if len(tokens) > 6 else 1
    def page_jump(number: int):
        tokens = scope.get("browser.path").rstrip("/").split("/")[:6]
        tokens += ["3", "0", str(number), ""][(len(tokens) - 4):]
        actions.user.browser_go_path("/".join(tokens), keep_query=True)


# Community story browser (subpath 6)
# /community/<community>/<number_community>/[<number_rating>/<number_sort>/<page>/<number_type>/<number_genre>/<number_words>/<number_status>/<number_update_time>]
ctx = Context()
ctx.matches = r"""
app: fanfictionnet
app: fictionpress
browser.path: /^\/community\/[^\/]+\/\d+\/(\d+\/){0,6}(\d+\/?)?$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current():
        tokens = scope.get("browser.path").rstrip("/").split("/")
        return int(tokens[6]) if len(tokens) > 6 else 1
    def page_jump(number: int):
        tokens = scope.get("browser.path").rstrip("/").split("/")
        if len(tokens) > 6:
            tokens[6] = str(number)
        else:
            tokens += ["3", "0", str(number), "0", "0", "0", "0", ""][(len(tokens) - 4):]
        actions.user.browser_go_path("/".join(tokens), keep_query=True)


# Forum browser (subpath 7)
# /forums/<category>/<fandom>/[<number_lang>/<number_sort>/<number_type>/<page>]
ctx = Context()
ctx.matches = r"""
app: fanfictionnet
app: fictionpress
browser.path: /^\/forums\/(?!general)\w+\/[^\/]+\/(\d\/){0,3}(\d+\/?)?$/
"""
ctx.tags = ["user.pages"]

@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current():
        tokens = scope.get("browser.path").rstrip("/").split("/")
        return int(tokens[7]) if len(tokens) > 7 else 1
    def page_jump(number: int):
        tokens = scope.get("browser.path").rstrip("/").split("/")[:7]
        tokens += ["0", "3", "0", str(number), ""][(len(tokens) - 4):]
        actions.user.browser_go_path("/".join(tokens), keep_query=True)


# --- Chapters ---
# Reader (subpath 3)
# /s/<story_number>[/<chapter>/<story_name>]
ctx = Context()
ctx.matches = r"""
app: fanfictionnet
app: fictionpress
browser.path: /^\/s\/\d+(\/(\d+(\/([^\/]+\/?)?)?)?)?$/
"""
ctx.tags = ["user.chapters"]

@ctx.action_class("user")
class UserActions:
    # user.chapters
    def chapter_current():
        tokens = scope.get("browser.path").rstrip("/").split("/")
        return int(tokens[3]) if len(tokens) > 3 else 1
    def chapter_jump(number: int):
        tokens = scope.get("browser.path").rstrip("/").split("/")
        # story name can be after chapter number -> replace number, keep name
        if len(tokens) > 3:
            tokens[3] = str(number)
        else:
            tokens.append(str(number))
        actions.user.browser_go_path("/".join(tokens), keep_query=True)
