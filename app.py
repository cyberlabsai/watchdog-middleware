from flask import Flask, jsonify, request
from db import updateTweetRead, getTweets
import Tweet


app = Flask(__name__)


@app.route('/')
def root():
    return ('Cyberlabs supremo')

@app.route('/termometer', methods=['GET'])
def termometer():
    '''retornar no intervalo de 175 todas as ocorrencias de hate e o tipo (img || txt)'''
    if request.method == 'GET':
        tweets = getTweets()
        response = []
        for tweet in tweets:
            t = Tweet(tweet[0],tweet[1],tweet[2],tweet[3],tweet[4])
            response.append(t)
            print(t)
        

    return jsonify('nudity')

    
