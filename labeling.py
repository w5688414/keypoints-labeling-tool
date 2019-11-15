import cv2
import os
import json

imgPath = "Pic/"
labels = ["startPoint", "endPoint", "centerPoint", "startPointUp", "endPointUp", "centerPointUp"]


images = os.listdir(imgPath)
# images = ["1-1.jpg"]
global info, imgName, index, meterCount, mode, pressCount


def getPoints(event, x, y, flags, param):
    global index, mode, roiX, roiY, meterCount, imgName
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(param[0], (x, y), 5, (0, 0, 255), -1)
        if index > 5:
            print("NO MORE POINTS!")
            return
        info[labels[index]]["x"], info[labels[index]]["y"] = x, y
        index += 1


def cutTemplate(event, x, y, flags, param):
    global roiX, roiY, meterCount, imgName, info, index, mode, pressCount
    index = 0
    if event == cv2.EVENT_LBUTTONDOWN:
        roiX, roiY = x, y
        if pressCount == 0:
            info["ROI"]["x"] = x*shrink
            info["ROI"]["y"] = y*shrink

    elif event == cv2.EVENT_LBUTTONUP:
        ROI = image[roiY*shrink:y*shrink, roiX*shrink:x*shrink].copy()
        if pressCount == 0:
            info["ROI"]["w"] = (x - roiX)*shrink
            info["ROI"]["h"] = (y - roiY)*shrink
            cv2.rectangle(image_small, (roiX, roiY), (x, y), (0, 0, 255), 2)
            pressCount += 1
        elif pressCount == 1:
            # ROI = cv2.resize(ROI, (0, 0), fx=shrink, fy=shrink)
            cv2.imwrite("template/" + imgName + "_" + str(meterCount) + ".jpg", ROI)
            cv2.namedWindow("temp")
            cv2.setMouseCallback('temp', getPoints, param=[ROI])
            while 1:
                cv2.imshow("temp", ROI)
                key = cv2.waitKey(20)
                if cv2.waitKey(20) & 0xFF == 27:
                    break
            fp = open("config/"+imgName+"_"+str(meterCount)+".json", "w", encoding='utf-8')
            print(info)
            json.dump(info, fp, indent=4)
            meterCount += 1
            cv2.destroyWindow("temp")
            pressCount = 0
    elif event==cv2.EVENT_RBUTTONDOWN:
        print("press right button")

shrink = 5

for im in images:
    print(im, "开始标注")
    image = cv2.imread(os.path.join(imgPath, im))
    # image_small = cv2.resize(image, (0, 0), fx=1/shrink, fy=1/shrink)
    cv2.namedWindow("origin")
    meterCount = 1
    pressCount = 0
    imgName = im.split(".")[0]
    info = json.load(open("config/ConfigTemplate.json"))
    mode = "stop"
    cv2.setMouseCallback('origin', cutTemplate)
    while(True):
        cv2.imshow("origin", image)
        key = cv2.waitKey(20)
        if key & 0xFF == 27:
            break
    print(im, "已经标好")
    cv2.destroyWindow("origin")
    cv2.waitKey(100)








