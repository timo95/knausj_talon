from talon import Module, Context, scope, actions

# --- App definitions ---
mod = Module()
mod.apps.fanfictionnet = """
tag: browser
browser.host: www.fanfiction.net
browser.host: m.fanfiction.net
"""
mod.apps.fictionpress = """
tag: browser
browser.host: www.fictionpress.com
browser.host: m.fictionpress.com
"""

# Context matching
ctx = Context()
ctx.matches = r"""
app: fanfictionnet
app: fictionpress
"""


# --- Define lists ---
# TODO: add more, split between categories
mod.list("fanfictionnet_fandom", desc="Fandoms to browse")
ctx.lists["user.fanfictionnet_fandom"] = {
    "harry potter": "book/Harry-Potter/",
    "naruto": "anime/Naruto/",
    "bleach": "anime/Bleach/",
    "ruby": "anime/RWBY/",
    "my hero academia": "anime/My-Hero-Academia-僕のヒーローアカデミア/",
    "madoka magica": "anime/Puella-Magi-Madoka-Magica-魔法少女まどか-マギカ/",
}

# TODO: add all categories
mod.list("fanfictionnet_category", desc="Categories of fandoms")
ctx.lists["user.fanfictionnet_category"] = {
    "anime": "anime/",
    "books": "book/",
}

# TODO: add poetry genres
mod.list("fictionpress_genre_fiction", desc="Fiction genre to browse")
ctx.lists["user.fictionpress_genre_fiction"] = {
    "general": "General/",
    "romance": "Romance/",
    "fantasy": "Fantasy/",
    "young adult": "Young-Adult/",
    "adult": "Adult/",
    "horror": "Horror/",
    "supernatural": "Supernatural/",
    "humor": "Humor/",
    "sci-fi": "Sci-Fi/",
    "action": "Action/",
    "essay": "Essay/",
    "manga": "Manga/",
    "historical": "Historical/",
    "mystery": "Mystery/",
    "biography": "Biography/",
    "thriller": "Thriller/",
    "spiritual": "Spiritual/",
    "mythology": "Mythology/",
    "play": "Play/",
    "fable": "Fable/",
    "kids": "Kids/",
    "western": "Western/",
}


# --- Implement actions ---
@ctx.action_class("user")
class UserActions:
    # user.chapters
    def chapter_current(): return int(scope.get("browser.path").split("/")[3])
    def chapter_jump(number: int):
        tokens = scope.get("browser.path").split("/")
        tokens[3] = str(number)
        actions.user.browser_go_path("/".join(tokens), keep_parameters=True)
