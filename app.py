from flask import Flask, jsonify, request
from db import updateTweetRead
app = Flask(__name__)

@app.route('/')
def root():
    return ('Cyberlabs supremo')

@app.route('/termometer', methods=['GET', 'POST'])
def termometer():
    if request.method == 'POST':
        data = request.json
        print(data)
        updateTweetRead(1)

    elif request.method == 'GET':
        '''retornar no intervalo de 175 todas as ocorrencias de hate e o tipo (img || txt)'''
        return jsonify('nudity')

    
