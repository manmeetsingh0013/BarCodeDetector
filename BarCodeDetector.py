
# Import modules
import cv2
import matplotlib.pyplot as plt

import numpy as np

# Image Path
imgPath = "images/IDCard-Satya.png" # Give the path of image here.

# Read image
img = cv2.imread(imgPath)

# Create a QRCodeDetector Object
# Variable name should be qrDecoder
qrDecoder = cv2.QRCodeDetector()

opencvData,bbox,rectifiedImage = qrDecoder.detectAndDecode(img)

#convert into unit8
rectifiedImage = np.uint8(rectifiedImage)


# Check if a QR Code has been detected
if opencvData != None:
    print("QR Code Detected")
else:
    print("QR Code NOT Detected")

# Draw the bounding box
if len(opencvData) > 0:
    n = len(bbox)
    for j in range(n):
         cv2.line(img, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255,0,0), 3)

print("QR Code Detected!")

print("Decoded Data : {}".format(opencvData))

# Write the result image
resultImagePath = "QRCode-Output.png"
cv2.imwrite(resultImagePath,img)


#convert to BGR to RGB
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)