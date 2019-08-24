from nsfw_model import nsfw

class Tweet():
    def __init__(self, id, tweetText, image, base64, username, inappropriate=None):
        self.id = id
        self.tweetText = tweetText
        self.image = image
        self.base64 = base64
        self.username = username
        self.inappropriate = inappropriate
    
    def validate(self):
        if self.image:
            nsfw = nsfw()
            self.inappropriate = nsfw.classify(self.base64)
        else:
            #train nlp ...
            pass
        
    
