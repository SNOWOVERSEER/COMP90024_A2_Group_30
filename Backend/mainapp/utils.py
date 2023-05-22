import json
import random
from couchdb import Server
from django.conf import settings


def get_random_database():
    databases = list(settings.COUCHDB_DATABASES.keys())
    return random.choice(databases)

def get_state_database():
    databases = settings.COUCHDB_DATABASES["state"]
    return databases

def get_mastodon_database():
    databases = settings.COUCHDB_DATABASES["mastodon"]
    return databases


def get_state_immigration_database():
    databases = settings.COUCHDB_DATABASES["immigration"]
    return databases


def check_couchdb_status():
    server_url = settings.COUCHDB_DATABASES["URL"]
    try:
        server = Server(server_url)
        server.version()  # Perform a simple operation to check the server's availability
        print(f"CouchDB server is running: False")
    except Exception:
        print(f"CouchDB server is running: True")
