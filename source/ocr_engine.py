import cv2 
import easyocr

from logger import logging

def extract_text(image_path, confidence_threshold = 0.1, languages = ['en']):
    ''''
    Extracts and filters text from an image using OCR, based on a confidence threshold.

    Args:
        image_path[str]: image file path
        confidence_threshold[Float, Default = 0.3]: Minimum threshold for considering the text 
        languages[list]: by default ['en'], language for text extraction

    returns:
        Raw text seperated by | in between the words
    '''
    logging.info('Text Extraction started')
    reader = easyocr.Reader(languages)

    try:
        result = reader.readtext(image= image_path)
        filtered_text = "|"
        
        for text in result:
            bounding_box, recognized_text, confidence = text
            if confidence > confidence_threshold:
                filtered_text = recognized_text + '|'
        
        return filtered_text
    
    except Exception as e:
        logging.info(f'An error occured during text extraction: {e}')
        return None
    
