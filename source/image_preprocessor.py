import cv2
import os 
from logger import logging

from utils import read_yaml
yaml_path = 'config.yaml'
config = read_yaml(yaml_path= yaml_path)

artifacts = config['artifacts']
raw_data_path = artifacts['RAW_DATA_PATH']

contour_file_name = artifacts['CONTOUR_FILE']

def read_image(image_path):
    try:
        img = cv2.imread(image_path)
        if img is None:
            logging.INFO('Error reading the image')
            raise Exception
        return img
            
    except Exception as e:
        print('Error reading image', e)
        return None
    
def extract_id_card(img):
    """
    The raw image can have a background. So, we need to extract only the card. 

    Args:
        img[np.ndarray]: Array input image

    Returns:
        np.ndarray: array of cropped image containnign the ID card, or None if card not detected.
    """
    # convert into gray-scale 
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Gaussian blurring to reduce noise
    blur_image = cv2.GaussianBlur(gray_image, ksize = (5,5), sigmaX = 0)

    #Adaptive thresholding
    threshold = cv2.adaptiveThreshold(blur_image, maxValue= 255, adaptiveMethod= cv2.ADAPTIVE_THRESH_MEAN_C, thresholdType= cv2.THRESH_BINARY_INV, blockSize= 11, C = 2)

    #Find Contours
    contours, _ = cv2.findContours(threshold, mode = cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # find the largest contour and area, assuming the ID card is the largest contour
    largest_area = 0
    largest_contour = None

    for cont in contours:
        area = cv2.contourArea(cont)
        if area > largest_area:
            largest_contour = cont
            largest_area = area 

    if largest_contour is None:
        return None
        logging.INFO('No contour found')

    x, y, w, h = cv2.boundingRect(largest_contour)

    current_work_dir = os.getcwd()
    filename = os.path.join(current_work_dir, raw_data_path, contour_file_name)

    contour_id = img[y: y+ h, x: x + w]

    cv2.imwrite(filename=filename, img = contour_id)

    return contour_id, filename






