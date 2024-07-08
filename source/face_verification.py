from deepface import DeepFace
import numpy as np 
import cv2 
import os 
import matplotlib.pyplot as plt

from logger import logging
from utils import file_exists
from utils import read_yaml


config_path = 'source/config.yaml'
config = read_yaml(config_path)

artifacts = config['artifacts']
cascade_path = artifacts['HAARCASCADE_PATH']
output_path = artifacts['RAW_DATA_PATH']


def detect_extract_face(img):
    # haar cascade works better with gray image
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #load haar cascade classifier
    face_cascade = cv2.CascadeClassifier(cascade_path)

    faces = face_cascade.detectMultiScale(gray_img, scaleFactor= 1.1, minNeighbors= 5)

    max_area = 0
    largest_face = None

    for (x, y, w, h) in faces:
        area = w * h
        if area > max_area:
            largest_face = (x, y, w, h)
            max_area = area

    # extract the largest cascade (face)
    if largest_face is not None:
        (x, y, w, h) = largest_face
    
        # increase dimension by 15 percent
        new_w = int(w * 1.5)
        new_h = int(h * 1.5)

        new_x = max(0, x-int((new_w - w) / 2))
        new_y = max(0, y - int((new_h - h)/2))

        # extract the enlarged (zoomed) face
        extracted_face = img[new_y: new_y + new_h, new_x : new_x + new_w]

        # testing purpose
        plt.imshow(extracted_face)
        plt.show()

        current_work_dir = os.getcwd()
        filename = os.path.join(current_work_dir, output_path, "extracted_face.jpg")

        if os.path.exists(filename):
            os.remove(filename)

        cv2.imwrite(filename= filename, img = extracted_face)
        logging.info(f'The extracted face is saved at {filename}')
        return filename
    
    else:
        return None


def deepface_face_comparision(image1_path="data\\raw_images\\extracted_face.jpg", image2_path = "data\\raw_images\\face_image.jpg"):
    image1_exists = file_exists(image1_path)
    image2_exitst = file_exists(image2_path)

    if not(image1_exists or image2_exitst):
        logging.info('Either of the file doesnt exist, check the path provided')
        return False

    verification = DeepFace.verify(img1_path= image1_path, img2_path= image2_path)

    if len(verification) > 0 and verification['verified']:
        print('Faces are verified')
        logging.info('Face verification successful')
        return True
    else:
        return False


def face_comparision(image1_path, image2_path, model_name = 'deepface'):
    is_verified = False
    if model_name == 'deepface': 
        is_verified = deepface_face_comparision(image1_path, image2_path)
    
    return is_verified

def get_face_embeddings(image_path):
    #check if image exists or not 
    image_exists = file_exists(image_path)

    if not(image_exists):
        print('check the path of the provided image')
        return None
    
    embedding_objs = DeepFace.represent(img_path= image_path, model_name= 'Facenet')
    embedding = embedding_objs[0]['embeddings']

    if len(embedding) > 0:
        return embedding 
    return None


