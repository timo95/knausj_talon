tag: terminal
and tag: user.docker
-
# Docker
docker display:
    user.docker()
    " ps "
docker display all:
    user.docker()
    " ps -a "
docker logs:
    user.docker()
    " logs "
docker logs <user.text>:
    user.docker()
    " logs {text}"
# Compose up
[docker] compose up:
    user.docker_compose()
    " up -d "
[docker] compose up <user.text>:
    user.docker_compose()
    " up -d {text}"
[docker] compose build:
    user.docker_compose()
    " up -d --build "
[docker] compose build <user.text>:
    user.docker_compose()
    " up -d --build {text}"
[docker] compose recreate:
    user.docker_compose()
    " up -d --force-recreate "
[docker] compose recreate <user.text>:
    user.docker_compose()
    " up -d --force-recreate {text}"
# Compose down
[docker] compose down:
    user.docker_compose()
    " down "
[docker] compose down <user.text>:
    user.docker_compose()
    " down {text}"
[docker] compose volume down:
    user.docker_compose()
    " down -v "
[docker] compose volume down <user.text>:
    user.docker_compose()
    " down -v {text}"
