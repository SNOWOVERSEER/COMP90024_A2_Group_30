### using ansible ###
```bash
sudo apt-get update
sudo apt-get install ansible
```

```bash
cd Mastodon
ansible-playbook Mastodon.yaml --extra-vars "token=eb7wHIIKQDNDY4iJqpbuXlnOmoAlKE0Wzyqy5_tb3xU url=mastodon.au"
ansible-playbook Mastodon.yaml --extra-vars "token=E0a8BaMkJlCGssCFPby8gLkGYdY0UqKKqj26zTCqLkY url=aus.social"
```


```bash
docker service logs -f
docker service logs -f -n 0 

docker service ls
```
