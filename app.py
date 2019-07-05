from flask import Flask, render_template, request, jsonify, redirect
from tiny_url.Configuration import Configuration
from tiny_url.TinyURL import TinyURL


app = Flask(__name__)
configuration = Configuration.read_from('configuration.json')
engine = TinyURL(configuration=configuration)


@app.route("/link", methods=['POST'])
def to_tiny_url():
    full_url = request.data.decode('utf-8')
    tiny_url = engine.add_link(full_url)
    print(full_url, tiny_url)
    return jsonify({'tiny': tiny_url, 'full': full_url})


@app.route("/<tiny_id>", methods=['GET'])
def get_tiny_url(tiny_id):
    full_url = engine.get_link(tiny_id)
    return redirect(full_url, code=302)


if __name__ == '__main__':
    # For debugging purposes, run on the default port
    # For production, use "flask run --port=80"
    app.run(host='0.0.0.0', port=configuration.port)
