#!/usr/bin/env python3
#

from flask import Flask
from flask import abort, jsonify, make_response

from api import get_urls

# Globals
BUCKET='coolwatervwclub'

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route("/<path:prefix>")
def root(prefix):

    urls = get_urls(BUCKET, prefix)

    if urls == None:
        abort(404)

    return urls
