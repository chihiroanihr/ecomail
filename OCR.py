import os, io, re
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
    
    signlist = ["$", "%"]
    for sign in signlist:
        score += 1.25 * len(re.findall(sign, str(df['description'][0])))
    
    keylist = ['PRICE', 'OFFER', 'SALE', 'DISCOUNT', 'FREE', 'PROMO', 'SHOP', 'CODE','TRY', 'BONUS', 'SAVE', 'EXTRA', 'EVENT', 'CLEARANCE', 'POINT', 'LIMITED', 'OFF', 'BEST PRICE' 'SPECIAL', 'HOT SALE', 'BIG SALE', 'HALF PRICE', 'VALUE']
    
    for keyword in keylist:
        score += 1.5 * len(re.findall(keyword, str(df['description'][0]).upper()))

    return score
    
#print(contentVerify("DEMO.png"))
if __name__ == '__main__':
    imageForTest = "proteinsale.png"
    image_path = os.getcwd() + "\\img\\" + imageForTest
    print(contentVerify(image_path))
