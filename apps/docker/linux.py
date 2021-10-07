from talon import Context, Module, actions

mod = Module()
mod.tag("docker", desc="tag for enabling docker commands in your terminal")
docker = "docker"

ctx = Context()
ctx.matches = r"""
os: linux
and tag: terminal
and tag: user.docker
"""


@ctx.action_class("user")
class UserActions:
    def docker():
        actions.insert("sudo docker")
    def docker_compose():
        actions.insert("sudo docker-compose")
