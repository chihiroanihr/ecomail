import os, io
from google.cloud import vision
from google.cloud.vision import types

def Detect_Logo(image):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'
    client = vision.ImageAnnotatorClient()
    image_path = os.path.join('', image)
    
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    
    visionImage = vision.types.Image(content=content)
    response = client.logo_detection(image=visionImage)
    return response

print(Detect_Logo('Grocery.jpg'))