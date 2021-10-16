app: thunderbird
title: /^Inbox -/
# German
title: /^Posteingang -/
title: /^Entwürfe -/
title: /^Papierkorb -/
title: /^Gesendet -/
-
(mail | message) open: key(enter)
(mail | message) (favorite | unfavorite): key(s)
(mail | message) (read | unread): key(m)
(mail | message) (watch | unwatch): key(w)
(mail | message) (ignore | unignore): key(k)
(mail | message) suspend: key(c)
(mail | message) archive: key(a)
(mail | message) spam: key(j)
(mail | message) up: key(b)
(mail | message) down: key(f)
(mail | message) new: key(ctrl-n)
(mail | message) reply sender: key(ctrl-r)
(mail | message) reply all: key(ctrl-shift-r)
(mail | message) reply list: key(ctrl-shift-l)
(mail | message) forward: key(ctrl-l)
(mail | message) save: key(ctrl-s)
(mail | message) print: key(ctrl-p)
(mail | message) edit: key(ctrl-e)

go home: key(alt-home)
toggle (mail | message) [pane]: key(f8)
