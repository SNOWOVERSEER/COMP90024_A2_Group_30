
```bash
sudo apt-get update
sudo apt-get install docker.io
sudo apt-get install ansible

cd Mastodon
docker build -t my_python_app:latest .
```

```bash
ansible-playbook Mastodon.yaml --extra-vars "token=eb7wHIIKQDNDY4iJqpbuXlnOmoAlKE0Wzyqy5_tb3xU url=mastodon.au"
ansible-playbook Mastodon.yaml --extra-vars "token=E0a8BaMkJlCGssCFPby8gLkGYdY0UqKKqj26zTCqLkY url=aus.social"
```


```bash
docker ps

docker stop 6e8cabd0dc67

docker rm 6e8cabd0dc67
```

