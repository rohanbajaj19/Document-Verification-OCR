import pandas as pd

from documents.extract_text import extract_text


def verify_pancard(file_link):
    extracted_text = extract_text(file_link)
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
