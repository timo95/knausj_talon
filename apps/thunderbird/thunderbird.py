from talon import Module, Context

# App definitions
mod = Module()
mod.apps.thunderbird = """
app.name: Thunderbird
"""

# English
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# German (duplicates removed)
month_names.append(["Januar", "Februar", "März", "Mai", "Juni", "Juli", "Oktober", "Dezember"])
month_titles = "\n".join(map(lambda s: f"title: /{s} /", month_names))
mod.apps.thunderbird_calendar = f"""
app: thunderbird
title: Calendar - Mozilla Thunderbird
title: Kalender - Mozilla Thunderbird
{month_titles}
"""

mod.apps.thunderbird_contacts = """
app: thunderbird
title: Address Book
title: Adressbuch
"""

mod.apps.thunderbird_inbox = """
app: thunderbird
title: /^Inbox -/
title: /^Posteingang -/
title: /^Entwürfe -/
title: /^Papierkorb -/
title: /^Gesendet -/
"""

# Context matching
ctx = Context()
ctx.matches = r"""
app: thunderbird
"""

# Set tags
ctx.tags = ["user.tabs"]


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
