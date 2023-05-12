import couchdb
import argparse
from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener
import csv, os, time, json


class Listener(StreamListener):
    def on_update(self, status):
        data = json.dumps(status, indent=2, sort_keys=True, default=str)

        data = json.loads(data)
        languages_dict[data['language']] = languages_dict.get(data['language'], 0) + 1
        print(languages_dict)
        # doc_id,doc_rev = db.save(languages_dict)


if __name__ == '__main__':
    # admin = 'admin'
    # password = 'password'
    # url = f'http://{admin}:{password}@127.0.0.1:5984'
    #
    # couch = couchdb.Server(url)
    #
    #
    # db_name = 'mastodon'
    #
    # if db_name not in couch:
    #     db = couch.create(db_name)
    # else:
    #     db = couch[db_name]
    #

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
