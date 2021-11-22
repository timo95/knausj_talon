from talon import Module, Context

# --- Tag definition ---
mod = Module()
mod.tag("emoji", desc="Emoji, ascii emoticons and kaomoji")

# Context matching
ctx = Context()
ctx.matches = """
tag: user.emoji
"""


# --- Define and implement lists ---
mod.list("emoticon", desc="Emoticons (ascii)")
ctx.lists["user.emoticon"] = {
    "crying": ":'(",
    "happy": ":)",
    "heart": "<3",
    "laughing": ":D",
    "sad": ":(",
    "surprised": ":o",
    "wink": ";)",
}

mod.list("emoji", desc="Emoji (unicode)")
ctx.lists["user.emoji"] = {
    "blushing": "😳",
    "crying": "😭",
    "happy": "😀",
    "heart": "❤️",
    "sad": "🙁",
    "shrug": "🤷",
}

mod.list("kaomoji", desc="Kaomoji (unicode)")
ctx.lists["user.kaomoji"] = {
    "blushing": "(⁄ ⁄•⁄ω⁄•⁄ ⁄)",
    "crying": "(╥﹏╥)",
    "embarrassed": "(⌒_⌒;)",
    "flower girl": "(◕‿◕✿)",
    "happy": "(* ^ ω ^)",
    "lenny": "( ͡° ͜ʖ ͡°)",
    "sad": "(｡•́︿•̀｡)",
    "shrug": r"¯\_(ツ)_/¯",
    "table flip": "(╯°□°)╯︵ ┻━┻",
    "table return": "┬─┬ ノ( ゜-゜ノ)",
}
