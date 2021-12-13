tag: terminal
and tag: user.docker
-
# Docker
docker display: user.docker("ps ")
docker display all: user.docker("ps -a ")
docker login: user.docker("login ")
docker logout: user.docker("logout ")
docker image push: user.docker("image push ")
docker image pull: user.docker("image pull ")
docker search [<user.text>]: user.docker("search {text or ''}")
docker logs [<user.text>]: user.docker("logs {text or ''}")
# Compose up
[docker] compose up [<user.text>]: user.docker_compose("up -d {text or ''}")
[docker] compose build [<user.text>]: user.docker_compose("up -d --build {text or ''}")
[docker] compose recreate [<user.text>]: user.docker_compose("up -d --force-recreate {text or ''}")
# Compose down
[docker] compose down [<user.text>]: user.docker_compose("down {text or ''}")
[docker] compose volume down [<user.text>]: user.docker_compose("down -v {text or ''}")
