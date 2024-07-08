import cv2
import os 
import matplotlib.pyplot as plt

from logger import logging
from image_preprocessor import extract_id_card
from face_verification import detect_extract_face
from utils import save_image
from face_verification import face_comparision
from ocr_engine import extract_text
from image_postprocessor import extract_information


def main_content(image_file, face_image_file):
    if face_image_file is not None:
        face_image = cv2.imread(face_image_file)
        logging.info('Face image successfully uploaded')

        if image_file is not None:
            image = cv2.imread(image_file)
            logging.info('ID card image successfully uploaded')

            # crop the unnecessary background
            image_roi, _ = extract_id_card(image)

            # TESTING PURPOSE
            plt.imshow(image_roi)
            plt.show()

            logging.info('Image ROI completed')
            # crop only the face 
            face_image_path2 = detect_extract_face(image_roi)
            
            face_image_path1 = save_image(face_image, 'face_image.jpg', path ='data\\raw_images')

            # check for comparision between the image of normal face and ID card face
            is_face_verified = face_comparision(face_image_path1, face_image_path2)

            # extract text from ocr engine named easyocr
            extracted_text = extract_text(image_roi)
            print('The output from extracted_text:',extracted_text)
            text_info =  extract_information(extracted_text)
            print('The output from text info:',text_info)

    return text_info





def test_main_content():
    id_card_actual_path = 'E:\\Computer-Vision\\e-KYC\\data\\test_image\\bigyan_passport_image.jpg'
    face_image_actual_path = 'E:\\Computer-Vision\\e-KYC\\data\\test_image\\bigyan_face_image.jpg'

    if not os.path.exists(id_card_actual_path) or not os.path.exists(face_image_actual_path):
        print("Please provide valid paths for both the ID card image and the face image.")
        return
    result = main_content(id_card_actual_path, face_image_actual_path)
    print("Extracted Information:", result)



if __name__ == "__main__":
    test_main_content()