import pytesseract
import pandas as pd
from io import BytesIO
from PIL import Image
import requests


def verify_pancard(file_link):
    file_link = file_link.replace("Documents/", "Documents%2F")
    image = requests.get(file_link)
    image = Image.open(BytesIO(image.content))
    extracted_text = pytesseract.image_to_string(image)
    extracted_text = [
        ele for ele in extracted_text.strip().split("\n") if ele.strip()]
    df = pd.read_excel("PanCard.xlsx")
    NAME_LIST = df["Name"].tolist()
    ACCOUNT_NUMBER_LIST = df["Permanent Account Number "].tolist()
    DOB_LIST = df["Date of Birth"].tolist()
    name = ""
    dob = ""
    account_status = False
    name_status = False
    dob_status = False
    for text in extracted_text:
        if text in ACCOUNT_NUMBER_LIST:
            index = ACCOUNT_NUMBER_LIST.index(text)
            name = NAME_LIST[index]
            dob = DOB_LIST[index]
            account_status = True
            break
    for text in extracted_text:
        if name in text:
            name_status = True
        if dob in text:
            dob_status = True
    return account_status and name_status and dob_status
