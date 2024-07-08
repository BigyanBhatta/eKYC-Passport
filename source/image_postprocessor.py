import pandas as pd
from datetime import datetime
import json

def extract_information(data_string):
    updated_data_string = data_string.replace('.', '')
    words = [word.strip() for word in updated_data_string.split('|') if len(word.strip()) > 2]

    # #initialize a dictionary to store extracted information
    # extracted_info = {
    #     'SURNAME':'',
    #     'GIVEN NAMES': '',
    #     'PERSONAL NO': '',
    #     'SEX': '',
    #     'DATE OF ISSUE': '',
    #     'DATE OF EXPIRY': '',
    #     'DATE OF BIRTH': '',
    #     'PLACE OF BIRTH': ''
    # }
    
    # try:
    #     name_index = words.index("GOVT OF INDIA") + 1
    #     extracted_info["Name"] = words[name_index]

    #     fathers_name_index = name_index + 1
    #     extracted_info["Father's Name"] = words[fathers_name_index]

    #     id_number_index = words.index("Permanent Account Number") + 1
    #     extracted_info["ID"] = words[id_number_index]

    #     dob_index = None
    #     for i, word in enumerate(words):
    #         try:
    #             datetime.strptime(word, "%d/%m/%Y")
    #             dob_index = i
    #             break
    #         except ValueError:
    #             continue

    #     if dob_index is not None:
    #         extracted_info["DOB"] = datetime.strptime(words[dob_index], "%d/%m/%Y")
    #     else:
    #         print("Error: Date of birth not found.")
    # except ValueError:
    #     print("Error: Some required information is missing or incorrectly formatted.")
        
    # return extracted_info   
    return words 

    