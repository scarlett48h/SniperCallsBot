from flask import Flask, send_from_directory
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

server = Flask(__name__, static_folder='../static', static_url_path='')

@server.route('/')
def serve_index():
    return send_from_directory(server.static_folder, 'index.html')

@server.route('/<path:path>')
def serve_path(path):
    return send_from_directory(server.static_folder, path)