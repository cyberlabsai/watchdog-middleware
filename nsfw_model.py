import tensorflow as tf
import numpy as np
import os
from model import OpenNsfwModel, InputType
from image_utils import create_tensorflow_image_loader


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


    def classify(self, image):

        fn_load_image = create_tensorflow_image_loader(self.sess)

        image = fn_load_image(image)

        predictions = self.sess.run(self.model.predictions,feed_dict={self.model.input: image})

        return predictions[0]

        print("\tSFW score:\t{}\n\tNSFW score:\t{}".format(*predictions[0]))

        
o = nsfw()

o.classify("0XBTHxt.jpg")
