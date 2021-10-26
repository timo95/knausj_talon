from urllib.parse import urlparse

from talon import app, Module, Context, actions, ui, registry

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


@ctx.action_class('browser')
class BrowserActions:
    def address():
        # Split title by space, check each token and token[1: -1] (it might be in brackets) for valid url.
        # Prioritize last one if multiple are valid, return empty string if none is valid.
        tokens = (url[1: -1] if not is_url(url) else url for url in reversed(actions.win.title().split(" ")))
        return next((url for url in tokens if is_url(url)), "")


@mod.scope
def url_scope_updater():
    # For possible values see: https://docs.python.org/3/library/urllib.parse.html
    return {"url_" + k: v for (k, v) in urlparse(actions.browser.address())._asdict().items()} if "browser" in registry.tags else None


def register_events():
    ui.register("win_title", url_scope_updater.update)
    ui.register("win_focus", url_scope_updater.update)


# prevent scary errors in the log by waiting for talon to be fully loaded
# before registering the events
app.register("ready", register_events)
