1. Heberger gitlab en local

```bash
docker run -d --hostname gitlab.local -p 8080:80 -p 443:443 -p 2222:22 --name gitlab --restart always -v gitlab_config:/etc/gitlab -v gitlab_logs:/var/log/gitlab -v gitlab_data:/var/opt/gitlab gitlab/gitlab-ce:latest
```

- Accès web : http://localhost:8080
- login : utilisateur `root`
- Pour trouver le MDP :

```bash
docker exec -it gitlab grep 'Password:' /etc/gitlab/initial_root_password
```

2. Runner docker pour exécuter les pipelines

```bash
docker run -d --name gitlab-runner --restart always -v /var/run/docker.sock:/var/run/docker.sock  -v gitlab-runner-config:/etc/gitlab-runner gitlab/gitlab-runner:latest
```

- Enregistrer le runner

```bash
docker exec -it gitlab-runner gitlab-runner register

URL: http://gitlab:80
Token: <token du projet>
Description: runner-docker
Tags: docker
Executor: docker
Default image: python:3.11.9-slim
```

- pour trouver le token : ton projet => Settings > CI/CD > Runners

- vérifier :

```bash
docker exec -it gitlab-runner gitlab-runner list
```

3. Configuration du runner :

- dans le fichier /etc/gitlab-runner/config.toml :

```toml
[[runners]]
  name = "test"
  url = "http://gitlab/"
  token = "xxxxx"
  executor = "docker"
  [runners.docker]
    tls_verify = false
    image = "python:3.12-slim"
    privileged = false
    disable_entrypoint_overwrite = false
    oom_kill_disable = false
    disable_cache = false
    volumes = ["/cache"]
    shm_size = 0
```

dans `[runners.docker]` ajouter : network_mode = "gitlab-net"
