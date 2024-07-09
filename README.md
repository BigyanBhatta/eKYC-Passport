# e-KYC Project

This project implements an electronic Know Your Customer (e-KYC) system using computer vision techniques. The system verifies the identity of a person by comparing their face image with the image on their ID card and extracting relevant information from the ID card.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Usage](#usage)
    - [Running the Application](#running-the-application)
    - [Testing the Application](#testing-the-application)
    - [Output](#output)
5. [Source File](#Source-File)
    - [image_preprocessor.py](#1-image_preprocessor.py)
    - [ocr_engine.py](#2-ocr_engine.py)
    - [face_verification.py](#3-face_verification.py)
    - [image_postprocessor.py](#4-image_postprocessor.py)
    - [app.py](#5-app.py)
    - [logger.py](#6-logger.py)
    - [utils.py](#7-utils.py)


## Project Structure
```plain-text
e-KYC/
├── data/models
│   └── haarcascade_frontalface_default.xml
├── data/raw_data
|    └── bigyan_passport_image.jpg
|    └── bigyan_face_image.jpg
├── source/
│   ├── app.py
│   ├── config.yaml
│   ├── face_verification.py
│   ├── image_postprocessor.py
│   ├── image_preprocessor.py
│   ├── logger.py
│   ├── ocr_engine.py
│   └── utils.py
├── logs/
├── requirements.txt
├── setup.py
└── README.md
```

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/BigyanBhatta/eKYC-Passport.git
    cd e-KYC
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

The configuration file `config.yaml` contains necessary paths and parameters. Ensure this file is properly set up before running the application.

## Usage

### Running the Application

To run the application, use the following command:
```bash
python -u "source/app.py"
```

### Testing the Application
To test the application with sample images:

- Place your ID card image and face image in the specified directory (data/test_image/).
- Update the paths in the test_main_content() function inside app.py.
``````
 Note: I haven't pushed the folder 'raw_image' which contains 'bigyan_face_image.jpg' and 'bigyan_passport_image.jpg' in the repository for privacy purpose. 
``````
### Output
The output of the application will display the verification status of the faces and the extracted information from the ID card in the console.

Output Example:
```bash
Faces are verified
Extracted Information: {
    'Surname': 'BHATTA',
    'First Name': 'BIGYAN',
    'Nationality': 'NEPALI',
    'Date of Issue': '02 JAN 2024',
    'Date of Birth': '09 NOV 2000',
    'Expiry Date': '01 JAN 2034',
    'Place of Birth': 'DHADING'
}
```
## Source File

#### 1. image_preprocessor.py
Contains functions to read and preprocess images, including extracting the ID card region from the image.

#### 2. ocr_engine.py
Uses EasyOCR to extract text from the ID card image.

#### 3. face_verification.py
Uses DeepFace to verify if the face in the face image matches the face on the ID card image.

#### 4. image_postprocessor.py
Extracts and formats the information from the text extracted by the OCR engine.

#### 5. app.py
Main application file that integrates all the modules to process and verify the images, and extract information.

#### 6. logger.py
Sets up the logging configuration.

#### 7. utils.py
Contains utility functions used across the project.

#### 8. setup.py
The setup.py file contains project metadata and can be used to install the project as a package. 