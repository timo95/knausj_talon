from talon import Module, Context

# --- App definition ---
mod = Module()
mod.tag("docker", desc="tag for enabling docker commands in your terminal")
docker = "docker"

# Context matching
ctx = Context()
ctx.matches = r"""
tag: terminal
and tag: user.docker
"""


# --- Define actions ---
@mod.action_class
class Actions:
    def docker():
        """Command to run docker"""
    def docker_compose():
        """Command to run docker compose"""
