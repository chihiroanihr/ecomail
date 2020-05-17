import os.path
from py4j.java_gateway import JavaGateway

#This function processes the image and return the appropriate image

#Input: String (name of the image), Boolean (Filter or not)
#Output: String (name of the original/updated image)

def imageProcessor(image, filterRequested):
    decidedImage = image
#(Step 1) Given an image name, if it fails to find the image, error must be raised.
    if not os.path.isfile(image):
        raise IOError

#(Step 2) Using OCR, verify whether the image is for the advertisement purpose or not.


#(Step 3) Using Java, Convert image from original to Grayscale without modifying the original image
    if filterRequested:
        gateway = JavaGateway()
        convertImage = gateway.entry_point
        convertImage.runImageProcessing(image)
        decidedImage = 'Filtered.png'
        gateway.close()
    
#based on the "filterRequest" Boolean, send the name of original/updated image
    return decidedImage

#Tester
print(imageProcessor('DEMO.jpg', True))