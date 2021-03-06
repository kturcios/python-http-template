from flask import Flask, request, jsonify
import os

from function import handler

app = Flask(__name__)

class Event:
    def __init__(self):
        self.body = request.get_data()
        self.headers = request.headers
        self.method = request.method
        self.query = request.args
        self.path = request.path

class Context:
    def __init__(self):
        self.hostname = os.environ['HOSTNAME']

def format_response(resp):
    if resp == None:
        return ('', 204)

    if 'response' not in resp:
        resp['response'] = ""
    elif type(resp['response']) == dict:
        resp['response'] = jsonify(resp['response'])
    
    if 'status_code' not in resp:
        resp['status_code'] = 200

    if 'headers' not in resp:
        resp['headers'] = []

    return (resp['response'], resp['status_code'], resp['headers'])

@app.route('/', defaults={'path': ''}, methods=['GET', 'PUT', 'POST', 'PATCH', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'PUT', 'POST', 'PATCH' 'DELETE'])
def call_handler(path):
    event = Event()
    context = Context()
    response_data = handler.handle(event, context)
    
    resp = format_response(response_data)
    return resp
