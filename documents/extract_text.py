import pytesseract
from io import BytesIO
from PIL import Image
import requests


def extract_text(file_link):
    file_link = file_link.replace("Documents/", "Documents%2F")
    image = requests.get(file_link)
    image = Image.open(BytesIO(image.content))
    extracted_text = pytesseract.image_to_string(image)
    extracted_text = [
        ele for ele in extracted_text.strip().split("\n") if ele.strip()]
    return extracted_text
