##


```bash
#mount disk:
sudo fdisk -l
sudo mkfs.ext4 /dev/vdb
sudo mkdir /data
sudo mount /dev/vdb /data
df -h

sudo vi /etc/fstab
/dev/vdb /data ext4 defaults 0 1

```

```bash
sudo apt-get update
sudo apt-get install docker.io
```
```bash
sudo docker pull couchdb:latest
```

```bash
sudo docker run -d \
  --name my-couchdb \
  -p 5984:5984 \
  -v /data:/opt/couchdb/data \
  -e COUCHDB_USER=admin \
  -e COUCHDB_PASSWORD=password \
  couchdb:latest
```
```bash
sudo docker ps
```


##Dont use docker swarm for creating cluster couchdb!!!below!!!
```bash
sudo docker swarm init --advertise-addr 172.26.136.136
```

```bash
sudo docker swarm join --token SWMTKN-1-2an433ynq9jr8tjco94c32awokjcspzym9w58co3gl0v6oq7rw-4hthfue5qvfwc9myry0xu2o4t 172.26.136.136:2377
```

```bash
sudo docker stack deploy -c docker-compose.yaml couchdb
```

```bash
sudo docker service ps couchdb_couchdb
```