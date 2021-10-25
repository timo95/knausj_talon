tag: user.tikz
-
tikz library {user.tikz_library}: insert("{tikz_library}")
use tikz library {user.tikz_library}: insert("\\usetikzlibrary{{{tikz_library}}}")
tikz {user.tikz_commands}:
    insert("\\{tikz_commands}{{}}")
    key(left)
begin tikz {user.tikz_environments}:
    insert("\\begin")
    sleep(200ms)
    key(enter)
    insert("{tikz_environments}")
    key(enter)
