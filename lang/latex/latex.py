from talon import Context, Module, actions

mod = Module()

# Context matching
ctx = Context()
ctx.matches = r"""
code.language: latex
"""


# --- Define and implement lists ---
mod.list("tex_document_classes", desc="TeX document classes")
ctx.lists["user.tex_document_classes"] = {
    "article": "article",
    "beamer": "beamer",
    "book": "book",
    "letter": "letter",
    "proceedings": "proc",
    "report": "report",
}

mod.list("tex_packages", desc="TeX packages")
ctx.lists["user.tex_packages"] = {
    "AMS math": "amsmath",
    # "bib latex"   = ["[style=authoryear]", "biblatex"]
    "bib latex": "biblatex",
    "colour": "color",
    "geometry": "geometry",
    "graphic X": "graphicx",
    "hyper ref": "hyperref",
    "import": "import",
    "math tools": "mathtools",
    "multi col": "multicol",
    "long table": "longtable",
    "tabular X": "tabularx",
    "tikz": "tikz",
    "X color": "xcolor",
    "wrap figure": "wrapfig",
}

mod.list("tex_environments", desc="TeX environments")
ctx.lists["user.tex_environments"] = {
    "abstract": "abstract",
    "add margin": "addmargin",
    "align": "align",
    "center": "center",
    "columns": "columns",
    # "column"                      = ["column", "{0.5\\textwidth}"]
    "column": "column",
    "cases": "cases",
    "display cases": "dcases",
    "definition": "definition",
    "description": "description",
    "document": "document",
    "enumerate": "enumerate",
    "equation": "equation",
    # "figure"                      = ["figure", "[h!]"]
    "figure": "figure",
    "flush left": "flushleft",
    "flush right": "flushright",
    "frame": "frame",
    "itemise": "itemize",
    "mini page": "minipage",
    # "multi (cols | columns)"      = ["multicols", "{2}"]
    "multi line": "multline",
    "proof": "proof",
    "quotation": "quotation",
    "quote": "quote",
    "split": "split",
    "table": "table",#              = ["table", "[h!]\n\\centering"]
    # "long table"                  = ["longtable", "{lll}"]
    "tabular": "tabular",#          = ["tabular", "{llll}"]
    # "tabular X"                   = ["tabular X", "{l X}"]
    "theorem": "theorem",
    "title page": "titlepage",
    "verbatim": "verbatim",
    "verse": "verse",
    "wrap figure": "wrapfigure",
}

mod.list("tex_commands", desc="TeX commands")
ctx.lists["user.tex_commands"] = {
    "author": "author",
    "add bib resource": "addbibresource",
    "caption": "caption",
    "chapter": "chapter",
    "simple citation": "cite",
    "frame title": "frametitle",
    "footnote": "footnote",
    "footnote text": "footnotetext[]",
    "graphics path": "graphicspath",
    "import": "import",
    "include graphics": "includegraphics[width=1\\textwidth]",
    "input": "input",
    "label": "label",
    "new command": "newcommand{}[]",
    "paragraph": "paragraph",
    "paren cite": "parencite",
    "part": "part",
    "reference": "ref",
    "renew command": "renewcommand",
    "sub paragraph": "subparagraph",
    "section": "section",
    "sub import": "subimport",
    "sub section": "subsection",
    "sub sub section": "subsubsection",
    "text cite": "textcite",
    "bold": "textbf",
    "italics": "textit",
    "slanted": "textsl",
    "emphasis": "emph",
    "title": "title",
    "use theme": "usetheme",
    # Accents
    "accent grave": "`",
    "accent acute": "'",
    "accent dot": ".",
    "accent breve": "u",
    "circumflex": "^",
    "umlaut": '"',
    "tilde": "~",
    "macron": "=",
}

mod.list("tex_commands_noarg", desc="TeX commands without arguments")
ctx.lists["user.tex_commands_noarg"] = {
    "centering": "centering",
    "column": "column{0.5\\textwidth}",
    "footnote mark": "footnotemark[]",
    "horizontal line": "hline",
    "lay tech": "LaTeX~ ",
    "line break": "linebreak",
    "item": "item",
    "make title": "maketitle",
    "new page": "newpage",
    "no indent": "noindent",
    "page break": "pagebreak",
    "print bibliography": "printbibliography",
    "table of contents": "tableofcontents",
    "tech": "TeX~ ",
    "text backslash": "textbackslash",
    "text height": "textheight",
    "text width": "textwidth",
    "vertical line": "vline",
}

mod.list("tex_magic_comments", desc="TeX magic comments")
ctx.lists["user.tex_magic_comments"] = {
    "begin preamble": "begin preamble",
    "bibtex compiler": "BibTeX Compiler",
    "compiler": "Compiler",
    "encoding": "encoding",
    "end preamble": "end preamble",
    "language": "language",
    "preview preamble": "preview preamble",
    "program": "Program",
    "root": "root",
    "spell check": "spellcheck",
}

mod.list("tex_magic_comments_noval", desc="TeX magic comments without values")
ctx.lists["user.tex_magic_comments_noval"] = {
    "parser off": "parser off",
    "parser on": "parser on",
}


# --- Implement actions ---
@ctx.action_class("user")
class UserActions:
    def code_comment(): actions.auto_insert('% ')
