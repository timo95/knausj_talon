from talon import Module, Context

# --- App definitions ---
# Main app
mod = Module()
mod.apps.thunderbird = """
app.name: Thunderbird
"""

# Inbox tab
mod.apps.thunderbird_inbox = """
app: thunderbird
title: /@/
"""

month_names = [
    "January", "February", "March", "April", "May", "June",  # English
    "July", "August", "September", "October", "November", "December",
    "Januar", "Februar", "März", "Mai", "Juni", "Juli", "Oktober", "Dezember"  # German
]
month_titles = "\n".join(map(lambda s: f"title: /{s} /", month_names))
# Calendar tab (lightning)
mod.apps.thunderbird_calendar = f"""
app: thunderbird
title: Calendar - Mozilla Thunderbird
title: Kalender - Mozilla Thunderbird
{month_titles}
"""

# Tasks tab TODO: implement
mod.apps.thunderbird_tasks = """
app: thunderbird
title: Tasks - Mozilla Thunderbird
title: Aufgaben - Mozilla Thunderbird
"""

# Mail composer window TODO: implement
mod.apps.thunderbird_composer = """
app: thunderbird
title: /Write: /
title: /Verfassen: /
"""

# Address book window
mod.apps.thunderbird_contacts = """
app: thunderbird
title: Address Book
title: Adressbuch
"""

# Context matching
ctx = Context()
ctx.matches = r"""
app: thunderbird
"""


# --- Define actions ---
@mod.action_class
class UserActions:
    def mod():
        """ctrl or cmd"""
    def thunderbird_calendar_view(number: int):
        """Select between calendar view tabs"""


# --- Implement actions ---
@ctx.action_class('app')
class AppActions:
    # app.tabs
    # not possible in thunderbird
    def tab_open(): pass
