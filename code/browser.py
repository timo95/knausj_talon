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
    def browser_url_parameters() -> dict[str]:
        """Return address parameters"""
        parameters = scope.get("browser.url").partition(scope.get("browser.host") + scope.get("browser.path"))[2]
        if not parameters.startswith("?"):
            return {}
        else:
            return {k: v for k, _, v in (p.partition("=") for p in parameters[1:].split("&"))}

    def browser_set_url_parameter(key: str, value: str):
        """Set parameter to current address"""
        parameters = actions.user.browser_url_parameters()
        parameters[key] = value
        path = scope.get('browser.path') + "?" + '&'.join(k if v == "" else f'{k}={v}' for k, v in parameters.items())
        actions.user.browser_go_path(path)

    def browser_go_path(path: str, keep_parameters: bool = False):
        """Go to path of current address"""
        address = scope.get('browser.scheme') + "://" + scope.get('browser.host')
        if len(path) > 0 and not path.startswith("/"):
            address += "/"
        address += path
        if keep_parameters:
            address += scope.get("browser.url").partition(scope.get("browser.host") + scope.get("browser.path"))[2]
        actions.browser.go(address)

    def browser_go_subpath(subpath: str, keep_parameters: bool = False):
        """Go to subpath of current address"""
        path = scope.get('browser.path')
        if not path.endswith("/") and len(subpath) > 0:
            path += "/"
        actions.user.browser_go_path(path + subpath, keep_parameters=keep_parameters)


# --- Implement actions ---
@ctx.action_class('browser')
class BrowserActions:
    def address():
        # Split title by space, check each token and token[1: -1] (it might be in brackets) for valid url.
        # Prioritize last one if multiple are valid, return empty string if none is valid.
        tokens = (url[1: -1] if not is_url(url) else url for url in reversed(actions.win.title().split(" ")))
        return next((url for url in tokens if is_url(url)), "")
