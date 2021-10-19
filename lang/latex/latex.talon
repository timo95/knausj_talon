code.language: latex
-
# Set tags
tag(): user.code_comment
tag(): user.maths

document class {user.tex_document_classes}:
    insert("\\documentclass{{{tex_document_classes}}}")
use package {user.tex_packages}:
    insert("\\usepackage{{{tex_packages}}}")
begin {user.tex_environments}:
    insert("\\begin")
    sleep(100ms)
    key(enter)
    insert("{tex_environments}")
    key(enter)
insert {user.tex_commands}:
    insert("\\{tex_commands}{{}}")
    key(left)
insert {user.tex_commands_noarg}:
    insert("\\{tex_commands_noarg} ")

