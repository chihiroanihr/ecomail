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

    return df['description']

if __name__ == '__main__':
    imageForTest = "proteinsale.png"
    image_path = os.getcwd() + "\\img\\" + imageForTest
    print(contentVerify(image_path))