import cv2

#text variables
textFont= cv2.FONT_HERSHEY_SIMPLEX
textFactor= 0.5
textColor = (0,255,0)

scaleFactor =1
maxScale =100
scaleType =0
maxScaleType=1

windowName = "ScaleImage"
trackBarValue = "Scale"
trackBarType = "Type: \n 0: Scale up \n 1: Scale down"

path = "images/truth.png"
img = cv2.imread(path)

cv2.namedWindow(windowName,cv2.WINDOW_AUTOSIZE)


# callback implementation

def scaleImage(*arg):
    global scaleType,scaleFactor

    if scaleType ==0:
        scaleFactor = 1+arg[0]/100.0
    else :
        scaleFactor = 1 - arg[0] / 100.0

    if scaleFactor ==0:
        scaleFactor=1;

    scaleImg = cv2.resize(img,None,fx=scaleFactor, fy=scaleFactor,interpolation = cv2.INTER_LINEAR)
    if scaleType ==0:
        height,width = scaleImg.shape[:2]
        textScaleUp = "Scaling Up... " + " hieght : " + str(height) + " width : " + str(width)
        cv2.putText(scaleImg,textScaleUp,(50,50),textFont,(scaleFactor-textFactor),textColor,2)
    else:
        height, width = scaleImg.shape[:2]
        textScaleDown = "Scaling Down... " + " hieght : " + str(height) + " width : " + str(width)
        cv2.putText(scaleImg, textScaleDown, (50, 50), textFont, (scaleFactor-textFactor), textColor,2)

    cv2.imshow(windowName,scaleImg)


def scaleImageType(*arg):
    global scaleType
    scaleType = arg[0]


cv2.createTrackbar(trackBarValue,windowName,scaleFactor,maxScale,scaleImage)
cv2.createTrackbar(trackBarType,windowName,scaleType,maxScaleType,scaleImageType)

cv2.imshow(windowName,img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()