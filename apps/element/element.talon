app: element
-
tag(): user.messaging

# Spaces
workspace <number_small>: key("ctrl-{number}")
# Messaging
grab left: key(shift-up)
grab right: key(shift-down)
(insert command | commandify):
    insert("``")
    key(left)
insert code:
    insert("``````")
    key(left left left)
    key(shift-enter)
    key(shift-enter)
    key(up)
element (quotes | quotation): key(ctrl->)
bold: key(ctrl-b)
(italic | italicize): key(ctrl-i)
