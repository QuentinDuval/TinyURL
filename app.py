from flask import Flask, render_template, request, jsonify
from tiny_url.Storage import *


app = Flask(__name__)


@app.route("/<tiny>", methods=['GET'])
def get_tiny_url(tiny):
    # TODO - redirection?
    # content = request.data
    return jsonify({'hello': 'world'})


@app.route("/link", methods=['POST'])
def set_tiny_url(tiny):
    long_url = request.data
    # TODO - write in DB
    return jsonify({'hello': 'world'})


if __name__ == '__main__':
    # For debugging purposes, run on the default port
    # For production, use "flask run --port=80"
    storage = Storage()
    storage.init_datamodel()
    storage.add_link('http://tiny', 'http://long/full/url')
    print(storage.get_all_link())
    print(storage.get_full('http://tiny'))
    app.run(host='0.0.0.0', port=80)
