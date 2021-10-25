from urllib.parse import urlparse

from talon import Module, Context, actions, ui

ctx = Context()
mod = Module()
apps = mod.apps
apps.firefox = "app.name: Firefox"
apps.firefox = "app.name: firefox"
apps.firefox = """
os: windows
and app.name: Firefox
os: windows
and app.exe: firefox.exe
"""
apps.firefox = """
os: mac
and app.bundle: org.mozilla.firefox
"""

ctx.matches = r"""
app: firefox
"""


def is_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


@ctx.action_class('browser')
class BrowserActions:
    def address():
        # Addon adds url tab title
        url = actions.win.title().split(" ")[-4]
        if not is_url(url):
            # it might be inside brackets
            url = url[1: -1]
        if not is_url(url):
            url = ""
        return url
    # TODO
    # action(browser.address):
    # action(browser.title):
    def go(url: str):
        actions.browser.focus_address()
        actions.sleep("50ms")
        actions.insert(url)
        actions.key("enter")
    def focus_search():
        actions.browser.focus_address()
    def submit_form():
        actions.key('enter')
