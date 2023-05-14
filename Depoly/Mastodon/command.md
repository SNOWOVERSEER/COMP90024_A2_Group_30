
```bash
docker build -t my_python_app:latest .
```

[//]: # (ansible-playbook -vvv Mastodon.yaml -e "token=eb7wHIIKQDNDY4iJqpbuXlnOmoAlKE0Wzyqy5_tb3xU url=mastodon.au")
```bash
ansible-playbook Mastodon.yaml --extra-vars "token=eb7wHIIKQDNDY4iJqpbuXlnOmoAlKE0Wzyqy5_tb3xU url=mastodon.au"
```



_[//]: # (docker service create --name mastodon_harvester_1234567890 --replicas 1 --mount type=bind,source=/home/ubuntu/Mastodon,dst=/app --mount type=bind,source=/home/ubuntu/Mastodon/requirements.txt,dst=/requirements.txt my_python_app:latest python /app/Mastodon_Harvester.py --token eb7wHIIKQDNDY4iJqpbuXlnOmoAlKE0Wzyqy5_tb3xU --url mastodon.au)_

```bash
docker ps
```

docker service logs -f
docker service logs -f -n 0 

docker service ls
docker service rm mastodon_harvester_1234567890