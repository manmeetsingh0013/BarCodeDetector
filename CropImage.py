import cv2

point = []
drawing =False
win_name = "Cropping Demo"
text = '''Drag Left to Right, " s "- Save Image And Exit ," r "- Reset Region'''
fontScale =0.5
fontStyle = cv2.FONT_HERSHEY_SIMPLEX
fontColor = (255,255,255)
fontThickNess =1


def drawRect(action ,x,y,flags,userdata):
    global start,end,drawing,loop,point
    if action == cv2.EVENT_LBUTTONDOWN:
        if drawing is False:
            drawing = True;
            point = [(x,y)]

    elif action == cv2.EVENT_LBUTTONUP:
        if drawing is True:
            point.append((x,y))
            cv2.rectangle(source, point[0], point[1], (0, 255, 0),1,cv2.LINE_AA)
            cv2.imshow(win_name, source)
            drawing=False;


path = "images/musk.jpg"
source = cv2.imread(path,1)
copyImg = source.copy()
cv2.putText(source,text,(15,15),fontStyle,fontScale,fontColor,fontThickNess,cv2.LINE_8);
cv2.namedWindow(win_name)

cv2.setMouseCallback(win_name,drawRect)

while True:

    cv2.imshow(win_name, source)

    key = cv2.waitKey(1) & 0xFF

    # Save the crop image by pressing ESC
    if key == ord("s"):
        break

    # To clear the Region and select the rectangle again
    if key == ord("r"):
        source = copyImg.copy()
        cv2.putText(source, text, (15, 15), fontStyle, fontScale, fontColor, fontThickNess, cv2.LINE_AA);

if len(point) == 2:
    cropImg = copyImg[point[0][1]:point[1][1],point[0][0]:point[1][0]]
    newImagePath = "images/muskCrop.jpg"
    cv2.imwrite(newImagePath,cropImg)
    print("================= Image successfully Saved!!!====================")
    cv2.destroyAllWindows()

