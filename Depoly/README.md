```bash
sudo apt-get update
sudo apt-get install nginx

sudo nano /etc/nginx/conf.d/couchdb.conf

sudo nginx -t

sudo systemctl reload nginx


```

### If use ansible ###
```bash
sudo apt-get update
sudo apt-get install ansible
ansible-playbook nginx.yaml


```

