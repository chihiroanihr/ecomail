import os.path

#This function processes the image and return the appropriate image

#Input: String (name of the image), Boolean (Filter or not)
#Output: String (name of the original/updated image)

def imageProcessor(image, filterRequested):
#(Step 1) Given an image name, if it fails to find the image, error must be raised.
    if not os.path.isfile(image):
        raise IOError

#At this step, you passed the IO test

#(Step 2) Using OCR, verify whether the image is for the advertisement purpose or not.


#(Step 3) Using Java, Convert image from original to Grayscale without modifying the original image
    

#based on the "filterRequest" Boolean, send the name of original/updated image

    return ""

imageProcessor('DEMO.jpg', True)