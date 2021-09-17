app: element
-
tag(): user.messaging

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
