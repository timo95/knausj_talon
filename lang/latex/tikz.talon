tag: user.tikz
-
tikz library {user.tikz_library}: insert("{tikz_library}")
use tikz library {user.tikz_library}: insert("\\usetikzlibrary{{{tikz_library}}}")
tikz {user.tikz_commands}:
    insert("\\{tikz_commands}{{}}")
    key(left)
begin tikz {user.tikz_environments}:
    user.paste("\\begin{{{tex_environments}}}\n\n\\end{{{tex_environments}}}")
    key(up tab)
