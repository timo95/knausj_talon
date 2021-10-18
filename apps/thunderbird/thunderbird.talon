app: thunderbird
-
# navigate tabs
go (mails | messages | inbox): user.tab_jump(1)
go (calendar | lightning): key("{user.mod()}-shift-c")
go tasks: key("{user.mod()}-shift-d")
# open windows
(open address [book] | address book | open contacts): key("{user.mod()}-shift-b")
dev tools: key("{user.mod()}-shift-i")
