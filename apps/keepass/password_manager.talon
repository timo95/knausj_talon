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
copy user [name]: user.password_manager_copy_user()
copy password: user.password_manager_copy_password()
copy (earl|url|link): user.password_manager_copy_url()
open (earl|url|link): user.password_manager_open_url()
fill password: user.password_manager_fill()
