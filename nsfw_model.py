import tensorflow as tf
import numpy as np
import os
from model import OpenNsfwModel, InputType
from image_utils import create_tensorflow_image_loader
from io import BytesIO
from PIL import Image, ImageStat
import base64
import cv2

def decode_img_base64(base64_string):
    sbuf = BytesIO()
    sbuf.write(base64.b64decode(base64_string))
    pimg = Image.open(sbuf)
    img = cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)
    return cv2.resize(img, (224,224))

class nsfw:

    def __init__(self):
        """Cart bar detection class

        Arguments
        ---------
        frozen_path: str
            Path to .pb model. Default="carts_model/frozen_inference_graph.pb"
        gpu_memory_fraction: float
            Percentage of how much gpu should the model use. If too little model can fail to load. Default=0.5
        gpu_device: str
            Required to set env variable CUDA_VISIBLE_DEVICES so Tensorflow only uses desired gpu. Default='0'
        """ 

        """Limit visible GPUs"""
        os.environ["CUDA_VISIBLE_DEVICES"] = "0"

        self.model = OpenNsfwModel()
                
        self.model.build()

        self.sess = tf.Session()

        self.sess.run(tf.initialize_all_variables())


    def classify(self, image_str):

        img = decode_img_base64(image_str)
        cv2.imwrite("img.jpg", img)

        fn_load_image = create_tensorflow_image_loader(self.sess)

        image = fn_load_image("img.jpg")

        predictions = self.sess.run(self.model.predictions,feed_dict={self.model.input: image})

        # print("\tSFW score:\t{}\n\tNSFW score:\t{}".format(*predictions[0]))

        return predictions[0]
        

