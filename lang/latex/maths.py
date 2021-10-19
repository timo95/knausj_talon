from talon import Context, Module, actions

# --- Tag definition ---
mod = Module()
mod.tag("maths")

# Context matching
ctx = Context()
ctx.matches = r"""
tag: user.maths
"""


# --- Define and implement lists ---
mod.list("greek_letters", desc="TeX greek letters")
ctx.lists["user.greek_letters"] = {
    # Lowercase
    "alpha": "alpha",
    "beater": "beta",
    "gamma": "gamma",
    "delta": "delta",
    "epsilon": "varepsilon",
    "zita": "zeta",
    "eater": "eta",
    "theta": "theta",
    "iota": "iota",
    "kappa": "kappa",
    "lambda": "lambda",
    "mu": "mu",
    "new": "nu",
    "zee": "xi",
    "pie": "pi",
    "row": "rho",
    "sigma": "sigma",
    "tau": "tau",
    "upsilon": "upsilon",
    "phi": "phi",
    "chi": "chi",
    "sigh": "psi",
    "omega": "omega",
    # Capitals
    "big gamma": "Gamma",
    "big delta": "Delta",
    "big theta": "Theta",
    "big lambda": "Lambda",
    "big zee": "Xi",
    "big pie": "Pi",
    "big sigma": "Sigma",
    "big upsilon": "Upsilon",
    "big phi": "Phi",
    "big sigh": "Psi",
    "big omega": "Omega",
}


mod.list("tex_symbols", desc="TeX mathematical symbols")
ctx.lists["user.tex_symbols"] = {
    # operators
    "product": "prod",
    "integral": "int",
    "double integral": "iint",
    "triple integral": "iiint",
    "times": "times",
    "divide": "div",
    "C dot": "cdot",
    "plus or minus": "pm",
    "partial": "partial",
    "infinity": "infty",
    "vector nabla": "nabla",
    # accents
    "accent hat": "hat",
    "accent tilde": "tilde",
    "accent dot": "dot",
    "accent double dot": "ddot",
    "accent bar": "bar",
    "accent vector": "vec",
    # trig
    "sine": "sin",
    "cosine": "cos",
    "tangent": "tan",
    "secant": "sec",
    "cosecant": "csc",
    "cotangent": "cot",
    "arc sine": "arcsin",
    "arc cosine": "arccos",
    "arc tan": "arctan",
    "hyperbolic sine": "sinh",
    "hyperbolic cosine": "cosh",
    "hyperbolic cotangent": "coth",
    "hyperbolic tangent": "tanh",
    # functions
    "argument": "arg",
    "degree": "deg",
    "determinant": "det",
    "dimension": "dim",
    "natural log": "ln",
    "logarithm": "log",
    "maximum": "max",
    "minimum": "min",
    "modulus": "bmod",
    "infimum": "inf",
    "supremum": "sup",
    "probability": "Pr",
    # relations
    "not equal to": "neq",
    "greater than or equal to": "geq",
    "less than or equal to": "leq",
    "approximately equal to": "approx",
    "proportional to": "propto",
    "preference less than": "prec",
    "preference less equals": "preceq",
    "preference greater than": "succ",
    "preference greater equal": "succeq",
    # logic
    "logic and": "land",
    "logic or": "lor",
    "logic not": "lnot",
    "logic exists": "exists",
    "logic member": "in",
    "logic for all": "forall",
    # arrow
    "left arrow": "leftarrow",
    "right arrow": "rightarrow",
    "up arrow": "uparrow",
    "down arrow": "downarrow",
    "left right arrow": "leftrightarrow",
    "maps to": "mapsto",
    "oh plus": "oplus",
    "oh times": "otimes",
    "big oh plus": "bigoplus",
    "big oh times": "bigotimes",
    # dots
    "dot dot dot": "dots",
    "diagonal dots": "ddots",
    "horizontal dots": "cdots",
    "vertical dots": "vdots",
    # sets
    "empty set": "emptyset",
    "subset": "subset",
    "superset": "supset",
    "strict subset": "subsetneq",
    "strict superset": "supsetneq",
    "intersection": "cap",
    "union": "cup",
}


# --- Define actions ---
@mod.action_class
class Actions:
    def maths_superscript(text: str = None):
        """Superscript"""
    def maths_subscript(text: str = None):
        """Subscript"""


# --- Implement actions ---
@ctx.action_class("user")
class UserActions:
    def maths_superscript(text: str = None):
        actions.insert("^{}")
        actions.key("left")
        if text:
            actions.insert(text)
            actions.key("right")
    def maths_subscript(text: str = None):
        actions.insert("_{}")
        actions.key("left")
        if text:
            actions.insert(text)
            actions.key("right")
