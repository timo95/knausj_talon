from talon import Module, Context

from .user_settings import get_list_from_csv

mod = Module()
mod.list("file_extension", desc="A file extension, such as .py")

_file_extensions_defaults = {
    "pie": ".py",
    "talon": ".talon",
    "mark down": ".md",
    "shell": ".sh",
    "vim": ".vim",
    "see": ".c",
    "see sharp": ".cs",
    "com": ".com",
    "net": ".net",
    "org": ".org",
    "U S": ".us",
    "exe": ".exe",
    "batch": ".bat",
    "binary": ".bin",
    "jason": ".json",
    "jay son": ".json",
    "J S": ".js",
    "java script": ".js",
    "TS": ".ts",
    "type script": ".ts",
    "csv": ".csv",
    "cassie": ".csv",
    "text": ".txt",
    "pdf": ".pdf",
    "svg": ".svg",
    "savage": ".svg",
    "yaml": ".yaml",
    "yammel": ".yaml",
}

file_extensions = get_list_from_csv(
    "file_extensions.csv",
    headers=("File extension", "Name"),
    default=_file_extensions_defaults,
)

ctx = Context()
ctx.lists["self.file_extension"] = file_extensions
