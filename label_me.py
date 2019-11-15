import cv2
import os
import json
import copy
imgPath = "Pic/"

global coordinates
# 鼠标回调函数
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:   # 处理鼠标左键双击
        # cv2.circle(img,(x,y),100,(255,0,0),-1)  # 在鼠标点击位置创建圆
        print("point1:=", x, y)
        point_size = 1
        point=(x,y)
        point_color = (0, 0, 255)  # BGR
        thickness = 2  # 可以为 0 、4、8
        cv2.circle(img, point, point_size, point_color, thickness)
        cv2.imshow('image', img)
        objects.append(copy.deepcopy([x,y]))
        # print("click")
    if(event)==cv2.EVENT_RBUTTONDOWN:
        return
    # print(event)

image_index=0
object_index=0
images = os.listdir(imgPath)
img_path=os.path.join(imgPath,images[image_index])
cv2.namedWindow("image")
cv2.setMouseCallback('image',draw_circle)  # 设置回调函数
img=cv2.imread(img_path)
objects=[]
# cv2.imshow('image', img)
coordinates={}

def getCoordinates():
    dict_list = {}
    object_name = 'o' + str(object_index)
    for i in range(len(objects)):
        x_name = 'x' + str(i)
        y_name = 'y' + str(i)
        dict_list[x_name] = objects[i][0]
        dict_list[y_name] = objects[i][1]
    # dict_data[object_name]=copy.deepcopy(dict_list)
    coordinates[object_name] = copy.deepcopy(dict_list)
    objects.clear()


while(True):
    cv2.imshow('image',img)
    waitkey_num = cv2.waitKeyEx()
    if waitkey_num== 27:  # esc键退出
        print(waitkey_num)
        break
    elif waitkey_num == 63233:
        object_index+=1
        getCoordinates()
        if(coordinates):
            json_name=images[image_index].split('.')[0]+".json"
            with open(json_name,'w') as f:
                json.dump(coordinates,f,indent=4)
                print("保存文件完成...")
            coordinates.clear()
        image_index=image_index+1
        if(image_index==len(images)):
            break
        img_path = os.path.join(imgPath, images[image_index])
        img = cv2.imread(img_path)
        object_index=0
        print("down")
    elif waitkey_num == 63235:
        object_index+=1
        print(objects)
        getCoordinates()
        print("right")
    # print(waitkey_num)



# cv2.waitKey(5000)
cv2.destroyAllWindows()

# import cv2
# import numpy as np
#
# # 鼠标回调函数
# def draw_circle(event,x,y,flags,param):
#
#     if event == cv2.EVENT_LBUTTONDOWN:   # 处理鼠标左键双击
#         print(event)
#         cv2.circle(img,(x,y),100,(255,0,0),-1)  # 在鼠标点击位置创建圆
#
# # 创建一个黑背景图像
# img = np.zeros((512,512,3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_circle)  # 设置回调函数
#
# while(1):
#     cv2.imshow('image',img)
#     if cv2.waitKey(20) & 0xFF == 27:  # esc键退出
#         break
# cv2.destroyAllWindows()