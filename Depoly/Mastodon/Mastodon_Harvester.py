import threading
import couchdb
import argparse
from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener
import csv, os, time, json

class Listener(StreamListener):
    def __init__(self):
        self.language_count = {}
        self.update_interval = 20  # seconds
        self.update_timer = threading.Timer(self.update_interval, self.update_db)
        self.update_timer.start()

    def on_update(self, status):
        data = json.loads(json.dumps(status, indent=2, sort_keys=True, default=str))
        language = data['language']
        if language != "en":
            self.language_count[language] = self.language_count.get(language, 0) + 1

    def update_db(self):
        while True:
            try:
                # Fetch the document
                doc = db.get('language_count')
                if doc is None:
                    # Create a new document if it doesn't exist
                    doc = {"_id": 'language_count'}

                # Add the counts from memory to the document
                for language, count in self.language_count.items():
                    doc[language] = doc.get(language, 0) + count

                print(doc)
                # Save the document and break the loop if successful
                db.save(doc)
                print('success')
                break
            except couchdb.http.ResourceConflict:
                # Retry the operation if there was a conflict
                continue

        # Clear the memory counter
        self.language_count.clear()

        # Restart the timer
        self.update_timer = threading.Timer(self.update_interval, self.update_db)
        self.update_timer.start()


if __name__ == '__main__':
    admin = 'admin'
    password = 'password'
    url = f'http://{admin}:{password}@172.26.132.185:80'

    couch = couchdb.Server(url)

    db_name = 'mastodon'

    if db_name not in couch:
        db = couch.create(db_name)
    else:
        db = couch[db_name]

    parser = argparse.ArgumentParser(description='mastodon token and url')

    parser.add_argument('--token', type=str, required=True, help='token')
    parser.add_argument('--url', type=str, required=True, help='url')

    args = parser.parse_args()

    # token = 'eb7wHIIKQDNDY4iJqpbuXlnOmoAlKE0Wzyqy5_tb3xU'
    token = args.token
    m = Mastodon(
        api_base_url=f'{args.url}',
        access_token=token
    )

    languages_dict = {}

    m.stream_public(Listener())
    while True:
        time.sleep(1)
