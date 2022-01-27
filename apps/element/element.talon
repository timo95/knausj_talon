app: element
-
tag(): user.messaging
tag(): user.emoji

# Spaces
workspace <number_small>: key("ctrl-{number_small}")

# Insert format
insert command:
    insert("``")
    key(left)
insert [code] block:
    insert("``````")
    key(left:3 shift-enter:2 up)
insert bold:
    insert("****")
    key(left:2)
insert (quotation | citation):
    key(shift-enter)
    insert("> ")
insert italic:
    insert("__")
    key(left)

# Format selected word
bold that: key(ctrl-b)
(quote | cite) that: key(ctrl->)
(italic | italicize) that: key(ctrl-i)

# Calls
([toggle] mute | unmute): key(ctrl-d)
[toggle] video: key(ctrl-e)

# Miscellaneous
show shortcuts: key(ctrl-/)
toggle (right | info): key(ctrl-.)
toggle (left | [work] spaces): key(ctrl-shift-d)
