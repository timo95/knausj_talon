os: linux
app.name: /^keepassx(c|2)$/i
-
tag(): user.tabs

# Database
database open: key(ctrl-o)
database save: key(ctrl-s)
database close: key(ctrl-w)
database lock: key(ctrl-l)
quit: key(ctrl-q)

# Entries
entry new: key(ctrl-n)
entry clone: key(ctrl-k)
entry copy: key(ctrl-shift-c)
entry paste: key(ctrl-shift-v)
entry (view|edit): key(ctrl-e)
entry delete: key(ctrl-d)
copy user [name]: key(ctrl-b)
copy password: key(ctrl-c)
(earl|url|link) open: key(ctrl-u)
(earl|url|link) copy: key(ctrl-alt-u)
find: key(ctrl-f)
find <user.text>:
    key(ctrl-f)
    insert("{text}")
