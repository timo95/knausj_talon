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
    "happy": ":)",
    "laughing": ":D",
    "wink": ";)",
    "crying": ";(",
    "sad": ":(",
    "heart": "<3",
    "surprised": ":o",
}

mod.list("emoji", desc="Emoji (unicode)")
ctx.lists["user.emoji"] = {
    "happy": "😀",
    "crying": "😭",
    "sad": "🙁",
    "shrug": "🤷",
    "heart": "❤️",
    "blushing": "😳",
}

mod.list("kaomoji", desc="Kaomoji (unicode)")
ctx.lists["user.kaomoji"] = {
    "happy": "(* ^ ω ^)",
    "crying": "(╥﹏╥)",
    "sad": "(｡•́︿•̀｡)",
    "shrug": r"¯\_(ツ)_/¯",
    "table flip": "(╯°□°)╯︵ ┻━┻",
    "table return": "┬─┬ ノ( ゜-゜ノ)",
    "flower girl": "(◕‿◕✿)",
    "lenny": "( ͡° ͜ʖ ͡°)",
    "embarrassed": "(⌒_⌒;)",
    "blushing": "(⁄ ⁄•⁄ω⁄•⁄ ⁄)",
}
