from couchdb import Server
from django.http import JsonResponse

from mainapp.utils import get_amin_database, get_state_database, get_state_immigration_database


def get_database_by_table(database_settings):
    server_url = database_settings['URL']
    database_name = database_settings['NAME']

    server = Server(server_url)
    database = server[database_name]

    # get the data from mastodon database
    documents = []
    for doc_id in database:
        document = database[doc_id]

        # Filter "_rev"
        filtered_document = {key: value for key, value in document.items() if key != "_rev" and key != "_id"}

        # Create document with "_id" as key
        sorted_document = sorted(filtered_document.items(), key=lambda x: x[1], reverse=True)

        sorted_document = dict(sorted_document[:10])
        sorted_document["total"] = sum(filtered_document.values())
        document_with_id_as_key = {doc_id: sorted_document}
        documents.append(document_with_id_as_key)

    return JsonResponse(documents, safe=False, json_dumps_params={'indent': 4})


def get_mastodon(request):
    return get_database_by_table(get_amin_database())


def get_state(request):
    database_settings = get_state_database()
    server_url = database_settings['URL']
    database_name = database_settings['NAME']

    server = Server(server_url)
    database = server[database_name]

    documents = []
    for doc_id in database:
        document = database[doc_id]

        # Filter "_rev"
        filtered_document = {key: value for key, value in document.items() if key != "_rev" and key != "_id"}

        # Create document with "_id" as key
        documents.append(filtered_document)

    return JsonResponse(documents, safe=False, json_dumps_params={'indent': 4})


def get_immigration(request):
    database_settings = get_state_immigration_database()
    server_url = database_settings['URL']
    database_name = database_settings['NAME']

    server = Server(server_url)
    database = server[database_name]

    documents = []
    for doc_id in database:
        document = database[doc_id]

        # Filter "_rev"
        filtered_document = {key: value for key, value in document.items() if key != "_rev" and key != "_id"}

        # Create document with "_id" as key
        documents.append(filtered_document)

    return JsonResponse(documents, safe=False, json_dumps_params={'indent': 4})
