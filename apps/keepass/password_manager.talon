tag: user.password_manager
-
# Entry management
entry new: user.password_manager_entry_new()
entry clone: user.password_manager_entry_clone()
entry copy: user.password_manager_entry_copy()
entry paste: user.password_manager_entry_paste()
entry edit: user.password_manager_entry_edit()
entry delete: user.password_manager_entry_delete()

# Entry data
password copy: user.password_manager_password_copy()
password fill: user.password_manager_password_fill()
user [name] copy: user.password_manager_user_copy()
(earl|url|link) copy: user.password_manager_url_copy()
(earl|url|link) open: user.password_manager_url_open()
