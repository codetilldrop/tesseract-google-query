from google import google

from PIL import Image
import pytesseract

image_text = pytesseract.image_to_string(Image.open('img.png'))
print image_text
query_res = google.search(image_text)
top_query = query_res[0]
print top_query.description