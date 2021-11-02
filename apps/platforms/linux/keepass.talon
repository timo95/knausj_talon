os: windows
and app.name: KeePass
os: windows
and app.exe: KeePass.exe
-
# Database
database open: key(ctrl-o)
database save: key(ctrl-s)
database close: key(ctrl-w)
database lock: key(ctrl-l)
quit: key(ctrl-q)

# Entries
entry new: key(ctrl-i)
entry clone: key(ctrl-k)
entry copy: key(ctrl-shift-c)
entry paste: key(ctrl-shift-v)
entry (view|edit): key(enter)
entry delete: key(delete)
copy user [name]: key(ctrl-b)
copy password: key(ctrl-c)
(earl|url|link) open: key(ctrl-u)
(earl|url|link) copy: key(ctrl-shift-u)
find: key(ctrl-f)
find <user.text>:
    key(ctrl-f)
    insert("{text}")
