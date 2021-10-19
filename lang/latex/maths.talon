tag: user.maths
-
# Basic symbols
greek {user.greek_letters}: insert("\\{greek_letters} ")
symbol {user.tex_symbols}: insert("\\{tex_symbols} ")

# Sub/Superscript
(super script | to the power [of]): user.maths_superscript()
(super script | to the power [of]) <user.word>: user.maths_superscript(user.word)
inverse: user.maths_superscript("-1")
squared: user.maths_superscript("2")
cubed: user.maths_superscript("3")
sub script: user.maths_subscript()
sub script <user.word>: user.maths_subscript(user.word)
