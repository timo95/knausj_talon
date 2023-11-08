from talon import Context, Module, actions

mod = Module()
mod.tag("docker", desc="Enables docker commands")

ctx = Context()
ctx.matches = r"""
os: windows
and tag: terminal
and tag: user.docker
"""


@ctx.action_class("user")
class UserActions:
    def docker(command: str = ""):
        actions.insert("docker " + command)
    def docker_compose(command: str = ""):
        actions.insert("docker compose " + command)
