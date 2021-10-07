from talon import Module, Context, actions, app

mod = Module()
mod.tag("docker", desc="tag for enabling docker commands in your terminal")
docker = "docker"

ctx = Context()
ctx.matches = r"""
tag: terminal
and tag: user.docker
"""


@mod.action_class
class Actions:
    def docker():
        """Command to run docker"""
    def docker_compose():
        """Command to run docker compose"""
