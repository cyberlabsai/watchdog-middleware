from flask import Flask, jsonify, request, json
from db import updateTweetRead, getTweets
import Tweet

app = Flask(__name__)

@app.route('/')
def root():
    return ('Cyberlabs supremo')

@app.route('/termometer', methods=['GET'])
def termometer():
    if request.method == 'GET':
        tweets = getTweets()
        response = []
        ids=[]
        for tweet in tweets:
                jsonObj = {
                        'id':'',
                        'base64':'',
                        'tweet':'',
                        'isImage':'',
                        'username':'',
                        'url':'',
                        'toxic':''
                }
                t = Tweet.Tweet(tweet[0],tweet[1],tweet[2],tweet[3],tweet[4],tweet[5])
                jsonObj['id'] = t.id
                jsonObj['base64'] = t.base64
                jsonObj['tweet'] = t.tweetText
                jsonObj['isImage'] = t.isImage
                jsonObj['username'] = t.username
                jsonObj['url'] = t.url
                jsonObj['toxic'] = t.inappropriate
                response.append(jsonObj)
                ids.append(str(t.id))
        
        updateTweetRead(ids)
        
    
    return jsonify(response)


