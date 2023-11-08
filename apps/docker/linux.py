from talon import Context, Module, actions

mod = Module()
mod.tag("docker", desc="tag for enabling docker commands in your terminal")

ctx = Context()
ctx.matches = r"""
os: linux
and tag: terminal
and tag: user.docker
"""


@ctx.action_class("user")
class UserActions:
    def docker(command: str = ""):
        actions.insert("sudo docker " + command)
    def docker_compose(command: str = ""):
        actions.insert("sudo docker compose " + command)
