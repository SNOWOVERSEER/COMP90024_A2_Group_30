```bash
docker build -t my-django-app .
```

```bash
docker swarm init
```

```bash
docker service create --name my_django_service --publish published=8000,target=8000 --replicas 2 my-django-app
```

if use ansible:
```bash
docker swarm init
ansible-playbook backend.yaml
```