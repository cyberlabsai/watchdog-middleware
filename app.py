from flask import Flask, jsonify, request, json
from db import updateTweetRead, getTweets
import Tweet
from nsfw_model import nsfw
import numpy as np
from nlp import NLP
import tensorflow as tf

from model import OpenNsfwModel, InputType
from image_utils import create_tensorflow_image_loader

# model = OpenNsfwModel()

# model.build()

app = Flask(__name__)

# nsfw_model = nsfw()

nlp = NLP()

@app.route('/')
def root():
    return ('Cyberlabs supremo')

@app.route('/termometer', methods=['GET'])
def termometer():

   
    if request.method == 'GET':
        tweets = getTweets()
        response = []
        ids =[]
        for tweet in tweets:
                t = Tweet.Tweet(tweet[0],tweet[1],tweet[2],tweet[3],tweet[4],tweet[5])

                if t.isImage:
                        print("WIP for image")
                        # img = decode_img_base64(t.base64)
                        # cv2.imwrite("img.jpg", img)

                        # fn_load_image = create_tensorflow_image_loader(sess)

                        # image = fn_load_image("img.jpg")

                        # predictions = sess.run(model.predictions,feed_dict={model.input: image})

                        # if val[1] >=0.9:
                        #         t.inappropriate = 1
                        # else:
                        #         t.inappropriate = 0

                else:
                        #train nlp ...
                        t.inappropriate = nlp.classify([t.tweetText])[0]
        
                jsonObj = {
                        'id':'',
                        'base64':'',
                        'tweet':'',
                        'isImage':'',
                        'username':'',
                        'url':'',
                        'toxic':''
                        }
                jsonObj['id'] = t.id
                jsonObj['base64'] = t.base64
                jsonObj['tweet'] = t.tweetText
                jsonObj['isImage'] = t.isImage
                jsonObj['username'] = t.username
                jsonObj['url'] = t.url
                jsonObj['toxic'] = str(t.inappropriate)
                response.append(jsonObj)
                ids.append(str(t.id))
                # print(jsonObj)
                updateTweetRead(ids)
        print(response)
    return jsonify(response)

