code.language: latex
-
# Set tags
tag(): user.code_comment
tag(): user.maths
tag(): user.tikz

document class {user.tex_document_classes}: "\\documentclass{{{tex_document_classes}}}"
use package {user.tex_packages}: "\\usepackage{{{tex_packages}}}"
begin {user.tex_environments}:
    user.paste("\\begin{{{tex_environments}}}\n\n\\end{{{tex_environments}}}")
    key(up tab)
insert {user.tex_commands}:
    insert("\\{tex_commands}{{}}")
    key(left)
insert {user.tex_commands_noarg}: "\\{tex_commands_noarg} "

# Magic comments
magic comment: "% !TeX "
magic comment {user.tex_magic_comments}: "% !TeX {tex_magic_comments} = "
magic comment {user.tex_magic_comments_noval}: "% !TeX {tex_magic_comments_noval}"
