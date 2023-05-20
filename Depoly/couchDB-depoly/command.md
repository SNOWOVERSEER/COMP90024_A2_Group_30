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
