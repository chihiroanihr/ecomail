import os, io
from google.cloud import vision
import pandas as pd

def contentVerify(image):

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"ServiceAccountToken.json"
    client = vision.ImageAnnotatorClient()

    image_path = os.path.join('',image)
    
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    # construct an image instance
    image = vision.types.Image(content=content)

    # annotate Image Response
    response = client.text_detection(image=image)

    # returns TextAnnotation
    df = pd.DataFrame(columns=['locale', 'description'])
    texts = response.text_annotations

    for text in texts:
        df = df.append(
            dict(
                locale=text.locale,
                description=text.description
            ),
            ignore_index=True
        )

    # likelihood of image being an advertisement
    score = 0
    
    signlist = ['\$', '\%']
    for sign in signlist:
        score += 1.25 * df['description'].str.count(sign).sum()
    
    keylist = ['Price', 'Offer', 'Sale', 'Discount', 'Free', 'Promo', 'Shop', 'Code', 'Try', 'Bonus', 'Save', 'Extra', 'Event', 'Clearance']
    
    for keyword in keylist:
        score += 1.5 * df['description'].str.count(keyword).sum()

    return score
    
#print(contentVerify("Tester.png"))