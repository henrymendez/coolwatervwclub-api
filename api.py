from flask import jsonify

from google.auth import compute_engine
from google.cloud import storage


def get_urls(bucket_name,prefix=None):
    """Lists all the blobs in the bucket."""
    # Local debugging. Uncomment below line, comment following 2
    #storage_client = storage.Client.from_service_account_json('key/coolwatervwclub-read-only.json')
    credentials = compute_engine.Credentials()
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.get_bucket(bucket_name)

    blobs = bucket.list_blobs(prefix=prefix,delimiter=None)

    blob_list = []
    for blob in blobs:
        # Don't return urls that end in /
        if blob.public_url.endswith('/'):
            continue
        item = { 'url': blob.public_url }
        blob_list.append(item)

    if not blob_list:
        return None

    return jsonify(images=blob_list)
