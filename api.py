import sys

from flask import jsonify
from google.auth import compute_engine

from google.cloud import storage


def get_urls(bucket_name,prefix=None):
    """Lists all the blobs in the bucket."""
    #storage_client = storage.Client.from_service_account_json('key/coolwatervwclub-read-only.json')
    credentials = compute_engine.Credentials()
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.get_bucket(bucket_name)

    blobs = bucket.list_blobs(prefix=prefix,delimiter='foo')
    #print("blobs: ", blobs, file=sys.stdout)

    blob_list = []
    for blob in blobs:
        item = { 'url': blob.public_url }
        blob_list.append(item)

    if not blob_list:
        return None

    return jsonify(images=blob_list)
