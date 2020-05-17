import os.path
from py4j.java_gateway import JavaGateway
from LogoFinder import Detect_Logo
from OCR import contentVerify

#This function processes the image and return the appropriate image

#Input: String (name of the image), Boolean (Filter or not)
#Output: String (name of the original/updated image)

def imageProcessor(image, filterRequested):
    decidedImage = image
#(Step 1) Given an image name, if it fails to find the image, error must be raised.
    if not os.path.isfile(image):
        raise IOError

#Don't filter out jpg. They are already compressed enough!
    ext = os.path.splitext(image)[-1].lower()
    if ext == ".jpg":
       filterRequested = False;

#(Step 2) Using OCR, verify whether the image is for the advertisement purpose or not.
    score = 0
    advertisement = False
    
    #If there is a brand name, it is possible that it's going to be the advertisement
    if Detect_Logo(image):
        score += 1
    
    score += contentVerify(image)
    
    #If the score reaches the threshold, then consider it as an advertisement
    if score >= 10:
        advertisement = True

#(Step 3) Using Java, Convert image from original to Grayscale without modifying the original image
    if filterRequested and advertisement:
        gateway = JavaGateway()
        convertImage = gateway.entry_point
        convertImage.runImageProcessing(image)
        decidedImage = 'Filtered.png'
        gateway.close()
    
#based on the "filterRequest" Boolean, send the name of original/updated image
    return decidedImage

#Tester
print(imageProcessor('DEMO1.png', True))