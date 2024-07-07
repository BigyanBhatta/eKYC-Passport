from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'

def get_requirements(path:str) -> List[str]:
    '''
    This function will return the list of requirements file. This file will have all the dependencies.
    '''
    requirements = []
    with open(path) as file_obj:
        requirements = file_obj.readlines()
        
    requirements= [req.replace('\n', '') for req in requirements ]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name = 'e-KYC Project',
    version = '0.0.1',
    description= 'This project is responsible for OCR operation in ID card, Passport, etc',
    author = 'Bigyan Bhatta',
    author_email= 'bigyanbhatta1193@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)





