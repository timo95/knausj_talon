tag: terminal
and tag: user.docker
-
# Docker
docker display: "docker ps "
docker logs: "docker logs "
docker logs <user.text>: "docker logs {text}"
# Compose up
[docker] compose up: "docker-compose up -d "
[docker] compose up <user.text>: "docker-compose up -d {text}"
[docker] compose build: "docker-compose up -d --build "
[docker] compose build <user.text>: "docker-compose up -d --build {text}"
[docker] compose recreate: "docker-compose up -d --force-recreate "
[docker] compose recreate <user.text>: "docker-compose up -d --force-recreate {text}"
# Compose down
[docker] compose down: "docker-compose down "
[docker] compose down <user.text>: "docker-compose down {text}"
[docker] compose volume down: "docker-compose down -v "
[docker] compose volume down <user.text>: "docker-compose down -v {text}"
