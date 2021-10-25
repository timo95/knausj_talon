from talon import Context, Module, actions

# --- Tag definition ---
mod = Module()
mod.tag("tikz")

# Context matching
ctx = Context()
ctx.matches = r"""
tag: user.tikz
"""


# --- Define and implement lists ---
mod.list("tikz_commands", desc="TeX tikz commands")
ctx.lists["user.tikz_commands"] = {
    "set": "tikzset",
    "style": "tikzstyle",
    "math": "tikzmath",
}

mod.list("tikz_library", desc="TeX tikz packages")
ctx.lists["user.tikz_library"] = {
    "math": "math",
}

mod.list("tikz_environments", desc="TeX tikz environments")
ctx.lists["user.tikz_environments"] = {
    "picture": "tikzpicture",
}
