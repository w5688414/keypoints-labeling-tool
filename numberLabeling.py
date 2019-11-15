import cv2
import os
from collections import defaultdict

"""
ReadMe:
将需要标注的图片放在numbers文件夹下，会自动在生成saved文件以及存储的相应位置
每显示一张图片在键盘上按对应的数字即可，如果该图片不是数字，按回车即可
因为每次会重置存储文件夹，所以尽量一次标完，或者自己改代码的逻辑
"""


if not os.path.exists("saved"):
    os.mkdir("saved")

for i in range(11):
    if os.path.exists("saved/"+str(i)):
        os.system("rm -rf {}".format("saved/"+str(i)))
    os.mkdir("saved/"+str(i))


def zero():
    return 0


imgPath = "storeDigitData"
images = os.listdir(imgPath)

count = defaultdict(zero)

for im in images:
    image = cv2.imread(imgPath+"/"+im)
    print(im)
    while 1:
        cv2.imshow("number", image)
        key = cv2.waitKey(1)
        if 48 <= key & 0xFF <= 57:
            label = str(key & 0xFF - 48)
            count[label] += 1
            cv2.imwrite("saved/{}/{}_{}.bmp".format(
                label,
                label,
                str(count[label])
            ), image)
            break
        elif key & 0xFF == 13:
            label = "10"
            count[label] += 1
            cv2.imwrite("saved/{}/{}_{}.bmp".format(
                label,
                label,
                str(count[label])
            ), image)
            break
        elif key & 0xFF == 27:
            break
