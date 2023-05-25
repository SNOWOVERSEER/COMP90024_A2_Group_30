```bash
sudo apt-get update
sudo apt-get install docker.io

cd Frontend

sudo docker build -t my-vue-app .


sudo docker run -p 80:80 -d my-vue-app




```
## if use ansible: ##

```bash
sudo apt-get update
sudo apt-get install ansible
ansible-playbook frontend.yaml
```
