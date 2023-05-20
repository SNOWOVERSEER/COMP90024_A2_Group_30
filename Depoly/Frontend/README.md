```bash
sudo apt-get update
sudo apt-get install docker.io

cd Frontend

sudo docker build -t my-vue-app .


#sudo docker service create --name frontend --replicas 1 -p 80:80 my-vue-app


sudo docker run -p 80:80 -d my-vue-app




```