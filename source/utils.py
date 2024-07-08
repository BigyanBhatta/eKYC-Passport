import os
import yaml 
import cv2

from logger import logging


def read_yaml(yaml_path:str) -> dict:
    with open(yaml_path) as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
    
    logging.info('yaml file loaded successfully')
    return yaml_data



def save_image(image, filename, path = "."):
    """
    To save an image to a speicified path with the given filename.
    Args:
        image[np.ndarray]: array of input image
        filename[str]: filename of the saved image
        path[str, optional]: path to save the image, Defaults to "." 
    
    """
    full_path = os.path.join(path, filename)
    cv2.imwrite(full_path, image)
    logging.info('Image saved to the specified path successfully')
    
    return full_path

def file_exists(image_path):
    is_exists = os.path.exists(image_path)

    if is_exists:
        logging.info(f'The file exists at the specified_path: {image_path}')
        return True
    else:
        return None