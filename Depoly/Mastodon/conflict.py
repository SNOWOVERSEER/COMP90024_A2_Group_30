from couchdb import Server

# Connect to the server
server = Server("http://admin:password@172.26.129.1:5984")
# Use your database
db = server["mastodon"]

# Initialize a counter
counter = 0

# Iterate over all documents in the database
for id in db:
    doc = db.get(id, conflicts=True)
    if "_conflicts" in doc:
        # There are conflicts, resolve them
        for conflict_rev in doc["_conflicts"]:
            conflict_doc = db.get(doc.id, rev=conflict_rev)
            db.delete(conflict_doc)
            # Increment the counter and print it
            counter += 1
            print(f"Deleted {counter} conflict versions.")
