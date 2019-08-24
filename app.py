from flask import Flask, jsonify, request
from db import updateTweetRead, getTweets
import Tweet

from sklearn.externals import joblib

class NLP:

        def __init__(self):
                self.classifier = joblib.load("modelo.pkl")
                self.vectorizer = joblib.load("vectorizer.pkl")

        def classify(self, texts):
                """Retorna se comentario e ofensivo ou nao

                Arguments
                ---------
                texts: numpy.ndarray
                Lista contendo as frases/tweets eg: texts = ["Brazil JS 'e o bicho"]

                Returns
                -------
                results: list
                Lista numpy contendo 0 para se frase nao e ofensiva 1 se ela for
                """

                freq = self.vectorizer.transform(texts)
                return self.classifier.predict(freq)

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

    
