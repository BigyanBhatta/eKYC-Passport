import pandas as pd
from datetime import datetime
import json

def extract_information(data_string):
    updated_data_string = data_string.replace('.', '')
    words = [word.strip() for word in updated_data_string.split('|') if len(word.strip()) > 2]

    #initialize a dictionary to store extracted information
    extracted_info = {
        'Surname':'',
        'First Name': '',
        'Nationality': '',
        'Date of Issue': '',
        'Date of Birth': '',
        'Expiry Date': '',
        'Place of Birth': ''
    }
    
    try:
        surname_index = words.index("SURNANE") + 1
        extracted_info["Surname"] = words[surname_index]

        name_index = words.index('GIVEN NAMES') + 1
        extracted_info["First Name"] = words[name_index]

        nationality_index = words.index("NATIONALITY") + 3
        extracted_info["Nationality"] = words[nationality_index]

        date_count = 0
        for i, word in enumerate(words):
            try:
                parsed_date = datetime.strptime(word.upper(), "%d %b %Y")
                formatted_date = parsed_date.strftime("%d %b %Y")
                
                if date_count == 0:
                    extracted_info['Date of Issue'] = formatted_date
                    date_count += 1
                
                elif date_count ==1:
                    extracted_info['Date of Birth'] = formatted_date
                    date_count+= 1
                
                elif date_count ==2:
                    extracted_info['Expiry Date'] = formatted_date
    
            except ValueError:
                continue    

        place_of_birth_index = words.index("PLACE OF BIRTH") + 2
        extracted_info['Place of Birth'] = words[place_of_birth_index]


    except ValueError:
        print("Error: Some required information is missing or incorrectly formatted.")
        
    return extracted_info   

    