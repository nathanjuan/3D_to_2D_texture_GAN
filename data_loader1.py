import scipy
import imageio
from glob import glob
import numpy as np
import matplotlib.pyplot as plt
import cv2
import random

class DataLoader():
    def __init__(self, dataset_name, img_res=(256, 256)):
        self.dataset_name = dataset_name
        self.img_res = img_res
        
        
    #def batch_generator(intput_set, output_set, size)
        #for (

    def load_data(self, batch_size = 1, is_testing=False):
        data_type = "train" if not is_testing else "test"
        path_in = glob('./datasets/output/brick/test/*')
        path_out = glob('./datasets/input/brick/test/*')
        batch_images_in = np.random.choice(path_in, size=batch_size)
        batch_images_out = np.random.choice(path_out, size=batch_size)
        imgs_A = []
        imgs_B = []
        for x in range(batch_size):
            i = random.randint(0, len(path_in) - 1)
            img_in = self.imread(path_in[i])
            img_out = self.imread(path_out[i])
            img_A = cv2.resize(img_in, self.img_res)
            img_B = cv2.resize(img_out, self.img_res)
            if not is_testing and np.random.random() < 0.5:
                img_A = np.fliplr(img_A)
                img_B = np.fliplr(img_B)
            imgs_A.append(img_A)
            imgs_B.append(img_B)
        imgs_A = np.array(imgs_A)/127.5 - 1.
        imgs_B = np.array(imgs_B)/127.5 - 1.

        return imgs_A, imgs_B

    def load_batch(self, batch_size=1, is_testing=False):
        data_type = "train" if not is_testing else "val"
        path_in = glob('./datasets/output/brick/test/*')
        path_out = glob('./datasets/input/brick/test/*')
        self.n_batches = int(len(path_in) / batch_size)
        for x in range(self.n_batches - 1):
            imgs_A = []
            imgs_B = []
            for y in range(batch_size):
                img_in = self.imread(path_in[x * batch_size + y])
                img_out = self.imread(path_out[x * batch_size + y])
                img_A = cv2.resize(img_in, self.img_res)
                img_B = cv2.resize(img_out, self.img_res)
                if not is_testing and np.random.random() < 0.5:
                    img_A = np.fliplr(img_A)
                    img_B = np.fliplr(img_B)
                imgs_A.append(img_A)
                imgs_B.append(img_B)
            
            #i = random.randint(0, len(path_in) - 1)
            #img_in = self.imread(path_in[i])
            #img_out = self.imread(path_out[i])
            #img_A = cv2.resize(img_in, self.img_res)
            #img_B = cv2.resize(img_out, self.img_res)
            #if not is_testing and np.random.random() < 0.5:
                #img_A = np.fliplr(img_A)
                #img_B = np.fliplr(img_B)
            #imgs_A.append(img_A)
            #imgs_B.append(img_B)
            imgs_A = np.array(imgs_A)/127.5 - 1.
            imgs_B = np.array(imgs_B)/127.5 - 1.
            #print("A length: " + str(len(imgs_A)) + "    B length: " + str(len(imgs_B)))
            yield imgs_A, imgs_B


    def imread(self, path):
        return imageio.imread(path).astype(np.float)
