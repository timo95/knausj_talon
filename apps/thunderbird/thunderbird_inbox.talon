app: thunderbird
# English
title: /^Inbox -/
# German
title: /^Posteingang -/
title: /^Entwürfe -/
title: /^Papierkorb -/
title: /^Gesendet -/
-
# navigate
(mail | message) open: key(enter)
(mail | message) up: key(b)
(mail | message) down: key(f)
go home: key(alt-home)
toggle (mail | message) [pane]: key(f8)
# mark
(mail | message) (favorite | unfavorite): key(s)
(mail | message) (read | unread): key(m)
(mail | message) (watch | unwatch): key(w)
(mail | message) (ignore | unignore): key(k)
(mail | message) suspend: key(c)
(mail | message) spam: key(j)
# send
(mail | message) new: key("{user.mod()}-n")
(mail | message) edit: key("{user.mod()}-e")
(mail | message) reply sender: key("{user.mod()}")
(mail | message) reply all: key("{user.mod()}-shift-r")
(mail | message) reply list: key("{user.mod()}-shift-l")
(mail | message) forward: key("{user.mod()}-l")
# organize
(mail | message) delete: key(delete)
(mail | message) archive: key(a)
(mail | message) save: key("{user.mod()}-s")
(mail | message) print: key("{user.mod()}-p")
