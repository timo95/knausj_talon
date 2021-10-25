from urllib.parse import urlparse

from talon import app, Module, Context, actions, ui

mod = Module()

ctx = Context()
ctx.matches = r"""
tag: browser
"""


def is_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


@mod.scope
def url_scope_updater():
    return {
        "url": actions.browser.address(),
        "uri": urlparse(actions.browser.address()).path,
    }


def register_events():
    ui.register("win_title", url_scope_updater.update)
    ui.register("win_focus", url_scope_updater.update)


# prevent scary errors in the log by waiting for talon to be fully loaded
# before registering the events
app.register("ready", register_events)

