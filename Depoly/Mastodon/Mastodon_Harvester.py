import threading
import couchdb
import argparse
from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener
import csv, os, time, json


def resolve_conflicts(db, doc_id):
    # Get the document with conflicts
    doc = db.get(doc_id, conflicts=True)
    if '_conflicts' in doc:
        conflicts = doc['_conflicts']
        print("get conflicts")

        # Get all conflict revisions
        revisions = [db.get(doc_id, rev=rev) for rev in conflicts]
        print('get revisions')

        # Compare the revisions and choose the maximum by sum of all language counts
        max_revision = max(revisions, key=lambda x: sum(x['language_count'].values()))
        print('get-max')

        # Save the maximum revision as the new revision
        max_revision['_rev'] = doc['_rev']
        print(sum(max_revision['language_count'].values()))
        db.save(max_revision)

        # Delete the other revisions
        for revision in revisions:
            if revision != max_revision:
                db.delete(revision)


class Listener(StreamListener):
    def __init__(self):
        self.language_count = {}
        self.update_interval = 15  # seconds
        # self.update_timer = threading.Timer(self.update_interval, self.update_db)
        # self.update_timer.start()

    def on_update(self, status):
        data = json.loads(json.dumps(status, indent=2, sort_keys=True, default=str))
        print(data)
        language = data['language']
        if language != "en":
            print(self.language_count)
            self.language_count[language] = self.language_count.get(language, 0) + 1

    def update_db(self):
        admin = 'admin'
        password = 'password'
        url = f'http://{admin}:{password}@172.26.132.185:80'

        couch = couchdb.Server(url)

        db_name = 'mastodon'

        if db_name not in couch:
            db = couch.create(db_name)
        else:
            db = couch[db_name]

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
                print("Conflict! waiting of retry...")
                resolve_conflicts(db, 'language_count')
                print("Conflict solved!")
                time.sleep(3)

                continue

        # Clear the memory counter
        self.language_count.clear()

        # Restart the timer
        self.update_timer = threading.Timer(self.update_interval, self.update_db)
        self.update_timer.start()


if __name__ == '__main__':

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
