from urllib.parse import urlparse

from talon import Context, Module, actions, app, scope

mod = Module()
ctx = Context()
ctx.matches = r"""
tag: browser
"""


def is_url(url: str) -> bool:
    try:
        # Valid if url successfully parsed
        result = urlparse(url)
        # and contains both scheme (e.g. http) and netloc (e.g. github.com)
        return all((result.scheme, result.netloc))
    except ValueError:
        return False


@mod.action_class
class Actions:
    def browser_open_address_in_new_tab():
        """Open the url in the address bar in a new tab"""
        actions.key("alt-enter")

    def browser_url_query(delimiter: str = "&") -> dict[str]:
        """Return address query"""
        query = scope.get("browser.url").partition("?")[2].partition("#")[0]
        return {} if query == "" else {k: (None if s == "" else v) for k, s, v in (p.partition("=") for p in query.split(delimiter))}

    def browser_set_url_query(key: str, value: str, delimiter: str = "&", keep_fragment: bool = True):
        """Set query to current address"""
        query = actions.user.browser_url_query(delimiter=delimiter)
        query[key] = value
        tokens = scope.get("browser.url").partition("?")
        address = tokens[0]
        address += "?" + delimiter.join(k if v is None else f"{k}={v}" for k, v in query.items())
        if keep_fragment:
            tokens = tokens[2].partition("#")
            address += tokens[1] + tokens[2]
        actions.browser.go(address)

    def browser_go_path(path: str, keep_query: bool = False, keep_fragment: bool = False):
        """Go to path of current address"""
        address = scope.get('browser.scheme') + "://" + scope.get('browser.host')
        if len(path) > 0 and not path.startswith("/"):
            address += "/"
        address += path
        tokens = scope.get("browser.url").partition("?")
        if keep_query:
            address += tokens[1] + tokens[2]
        if keep_fragment:
            tokens = tokens[2].partition("#")
            address += tokens[1] + tokens[2]
        actions.browser.go(address)

    def browser_go_subpath(subpath: str, keep_query: bool = False, keep_fragment: bool = False):
        """Go to subpath of current address"""
        path = scope.get('browser.path')
        if not path.endswith("/") and len(subpath) > 0:
            path += "/"
        actions.user.browser_go_path(path + subpath, keep_query=keep_query, keep_fragment=keep_fragment)


@ctx.action_class("user")
class UserActions:
    def tab_jump(number: int):
        if number < 9:
            if app.platform == "windows":
                actions.key(f"ctrl-{number}")
            else:
                actions.key(f"alt-{number}")

    def tab_final():
        if app.platform == "windows":
            actions.key("ctrl-9")
        else:
            actions.key("alt-9")

    def tab_duplicate():
        actions.browser.focus_address()
        actions.sleep("180ms")
        possibly_edited_url = actions.edit.selected_text()
        actions.key("esc:2")
        actions.browser.focus_address()
        actions.sleep("180ms")
        url_address = actions.edit.selected_text()
        if possibly_edited_url == url_address:
            actions.user.browser_open_address_in_new_tab()
        else:
            actions.user.paste(possibly_edited_url)
            actions.app.tab_open()
            actions.user.paste(url_address)
            actions.key("enter")


@ctx.action_class("browser")
class BrowserActions:
    def address() -> str:
        title: str = actions.win.title()
        if not title:
            return ""

        # We expect the URL to either be prepended or appended to the page title.
        first, *tokens = title.split()
        if is_url(first):
            return first

        # Prioritize last one if multiple are valid.
        for url in reversed(tokens):
            if is_url(url):
                return url
            # The URL may be in [brackets].
            unbracketed = url[1:-1]
            if is_url(unbracketed):
                return unbracketed

        # None were valid.
        return ""

    def bookmark():
        actions.key("ctrl-d")

    def bookmark_tabs():
        actions.key("ctrl-shift-d")

    def bookmarks():
        actions.key("ctrl-shift-o")

    def bookmarks_bar():
        actions.key("ctrl-shift-b")

    def focus_address():
        actions.key("alt-d")

    def focus_page():
        actions.browser.focus_address()
        actions.sleep("180ms")
        actions.key("esc:2")
        actions.sleep("180ms")
        actions.key("esc:2")

    def focus_search():
        actions.browser.focus_address()

    def go_blank():
        actions.key("ctrl-n")

    def go(url: str):
        actions.browser.focus_address()
        actions.sleep("50ms")
        actions.insert(url)
        actions.key("enter")

    def go_home():
        actions.key("alt-home")

    def go_back():
        actions.key("alt-left")

    def go_forward():
        actions.key("alt-right")

    def open_private_window():
        actions.key("ctrl-shift-n")

    def reload():
        actions.key("ctrl-r")

    def reload_hard():
        actions.key("ctrl-shift-r")

    def show_downloads():
        actions.key("ctrl-j")

    def show_clear_cache():
        actions.key("ctrl-shift-delete")

    def show_history():
        actions.key("ctrl-h")

    def submit_form():
        actions.key("enter")

    def toggle_dev_tools():
        actions.key("ctrl-shift-i")
