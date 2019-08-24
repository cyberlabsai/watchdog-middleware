from nsfw_model import nsfw
import json

class Tweet():
    def __init__(self, id, tweetText, imageStatus, base64, username, url, inappropriate=None):
        self.id = id
        self.tweetText = tweetText
        self.isImage = imageStatus
        self.base64 = base64
        self.username = username
        self.url = url
        self.inappropriate = inappropriate
    
    def validate(self):
        if self.isImage:
            nsfw = nsfw()
            self.inappropriate = nsfw.classify(self.base64)
        else:
            #train nlp ...
            pass
        

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)


    def show(self):
        print('-------------------------------------------------------------------------------------------------------------')
        print('Username: ', str(self.username))
        print('Text: '+str(self.tweetText))
        print('Url: '+str(self.url))
        print('Status: '+str(self.inappropriate))
        print('-------------------------------------------------------------------------------------------------------------')

    
