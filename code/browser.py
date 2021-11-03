from urllib.parse import urlparse

from talon import Context, Module, actions, scope

mod = Module()

ctx = Context()
ctx.matches = r"""
tag: browser
"""


def is_url(url):
    try:
        # Valid if url successfully parsed
        result = urlparse(url)
        # and contains both scheme (e.g. http) and netloc (e.g. github.com)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


# --- Define actions ---
@mod.action_class
class Actions:
    def browser_url_query(delimiter: str = "&") -> dict[str]:
        """Return address query"""
        query = scope.get("browser.url").partition("?")[2]
        return {} if query == "" else {k: (None if s == "" else v) for k, s, v in (p.partition("=") for p in query.split(delimiter))}

    def browser_set_url_query(key: str, value: str, delimiter: str = "&"):
        """Set query to current address"""
        query = actions.user.browser_url_query(delimiter=delimiter)
        query[key] = value
        address = scope.get("browser.url").partition("?")[0] + "?"
        actions.browser.go(address + delimiter.join(k if v is None else f"{k}={v}" for k, v in query.items()))

    def browser_go_path(path: str, keep_query: bool = False):
        """Go to path of current address"""
        address = scope.get('browser.scheme') + "://" + scope.get('browser.host')
        if len(path) > 0 and not path.startswith("/"):
            address += "/"
        address += path
        if keep_query:
            tokens = scope.get("browser.url").partition("?")
            address += tokens[1] + tokens[2]
        actions.browser.go(address)

    def browser_go_subpath(subpath: str, keep_query: bool = False):
        """Go to subpath of current address"""
        path = scope.get('browser.path')
        if not path.endswith("/") and len(subpath) > 0:
            path += "/"
        actions.user.browser_go_path(path + subpath, keep_query=keep_query)


# --- Implement actions ---
@ctx.action_class('browser')
class BrowserActions:
    def address():
        # Split title by space, check each token and token[1: -1] (it might be in brackets) for valid url.
        # Prioritize last one if multiple are valid, return empty string if none is valid.
        tokens = (url[1: -1] if not is_url(url) else url for url in reversed(actions.win.title().split(" ")))
        return next((url for url in tokens if is_url(url)), "")
