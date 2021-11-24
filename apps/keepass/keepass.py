from talon import Module

# --- App definitions ---
mod = Module()
mod.apps.keepass = """
os: windows
and app.name: KeePass
os: windows
and app.exe: KeePass.exe
"""
mod.apps.keepassx = """
os: linux
app.name: /^keepassx(c|2)$/i
"""


# --- Define actions ---
@mod.action_class
class Actions:
    def keepass_database_open():
        """Open password database"""
    def keepass_database_close():
        """Close password database"""
    def keepass_database_new():
        """Create new password database"""
    def keepass_database_save():
        """Save password database"""
    def keepass_database_lock():
        """Lock password database"""

