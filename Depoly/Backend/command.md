```bash
sudo apt-get update
sudo apt-get install docker.io
sudo docker build -t my-django-app .
```

```bash
docker swarm init
```

```bash
sudo docker service create --name my_django_service --publish published=8000,target=8000 --replicas 2 my-django-app
```
### If want to update this service to 4 replicas ###
```bash
sudo docker service update --replicas 4 my_django_service
```

## if use ansible: ##

```bash
sudo apt-get update
sudo apt-get install ansible
ansible-playbook backend.yaml
```

```bash
### if want to leave the swarm ###
docker swarm leave --force
```


### If want to update this service to 4 replicas ###
```bash
sudo docker service update --replicas 4 my_django_service
```
