app: keepass
app: keepassx
app: keepassxc
-
tag(): user.tabs
tag(): user.password_manager

# Database
database open: user.keepass_database_open()
database new: user.keepass_database_new()
database save: user.keepass_database_save()
database close: user.keepass_database_close()
database lock: user.keepass_database_lock()
