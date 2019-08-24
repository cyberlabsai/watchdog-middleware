from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return ('Hello, World!')

@app.route('/termometer', methods=[GET, POST])
def termometer():
    if request.method == 'POST':
        pass

    elif request.method == 'GET':
        return jsonify('nudity')

    
