app: element
-
tag(): user.messaging

# Spaces
workspace <number_small>: key("ctrl-{number_small}")
# Messaging
grab left: key(shift-up)
grab right: key(shift-down)
# New format
insert command:
    insert("``")
    key(left)
insert [code] block:
    insert("``````")
    key(left left left)
    key(shift-enter)
    key(shift-enter)
    key(up)
insert bold:
    insert("****")
    key(left left)
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
