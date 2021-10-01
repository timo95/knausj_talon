from talon import Module, Context

mod = Module()
mod.tag("docker", desc="tag for enabling docker commands in your terminal")
docker_compose = "docker"

ctx = Context()
ctx.matches = r"""
tag: user.docker_|
"""
