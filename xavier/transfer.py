import os, subprocess
import cv2
from datetime import datetime
import csv
import sys

def chngSrcImg(srcFilePath, imgNew):
    r = open(srcFilePath, "r")
    lines = r.readlines()
    count = 0
    for i in lines:
        if i.find("uri=file://") != -1:
            break
        count += 1
    lines[count] = "uri=file://"+imgNew+"\n"
    r.close()

    w = open(srcFilePath, "w")
    w.writelines(lines)
    w.close()

#chngSrcImg("/home/azarakuss/DeepStream-Yolo/deepstream_app_config.txt", "/home/azarakuss/Downloads/1.jpg")

if len(sys.argv) > 2:
    print("There was too many arguments")
    exit(-1)
elif len(sys.argv) < 2:
    print("Config file is missing !")
    exit(-1)
else:
    chngSrcImg("/home/azarakuss/development/sources/DeepStream-Yolo/deepstream_app_config.txt", sys.argv[1])

if subprocess.run(["deepstream-transfer-learning-app", "-c", 
            "/home/azarakuss/development/sources/DeepStream-Yolo/deepstream_app_config.txt"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
    print("There was an error !")
    exit(-1)
else:
    srcPath = "/home/azarakuss/development/xavier/records/current/"
    dstPath = "/home/azarakuss/development/xavier/records/past/"
    nowStr = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

    os.mkdir(dstPath+nowStr)
    os.rename(srcPath+"images/"+os.listdir(srcPath+"images/")[0], dstPath+nowStr+"/image_"+nowStr+".jpg")
    os.rename(srcPath+"labels/"+os.listdir(srcPath+"labels/")[0], dstPath+nowStr+"/label_"+nowStr+".txt")
    os.rename(srcPath+sorted(os.listdir(srcPath))[3], dstPath+nowStr+"/metadata_"+nowStr+".csv")
    os.rename(srcPath+sorted(os.listdir(srcPath))[3], dstPath+nowStr+"/metadata_"+nowStr+".json")

    tmpList = list()
    with open(dstPath+sorted(os.listdir(dstPath), reverse=True)[0]+"/metadata_"+sorted(os.listdir(dstPath), reverse=True)[0]+".csv") as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            defectType = row['class_name']
            h = row['img_height']
            w = row['img_width']
            x = row['img_top']
            y = row['img_left']

            tmpList.append((defectType, h, w, x, y))

    img = cv2.imread(dstPath+sorted(os.listdir(dstPath), reverse=True)[0]+"/image_"+sorted(os.listdir(dstPath), reverse=True)[0]+".jpg")
    for i in tmpList:
        img = cv2.rectangle(img, (int(i[4]), int(i[3])), 
            (int(i[4])+int(i[2]), int(i[3])+int(i[1])), 
            (0, 0, 255), 2, cv2.LINE_4)

        txtSize = cv2.getTextSize(i[0], cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.625, 1)
        img = cv2.rectangle(img, (int(i[4]), int(i[3])), 
            (int(i[4])+int(txtSize[0][0]*1.65), int(i[3])-int(txtSize[0][1]*2.25)),
            (75, 75, 75), -1, cv2.LINE_8)
        cv2.putText(img, i[0], (int(i[4])+int(txtSize[0][0]*0.125), int(i[3])-int(txtSize[0][1]*0.5)), cv2.FONT_HERSHEY_SIMPLEX, 0.625, (255, 255, 255), 1, cv2.LINE_4)

    cv2.imwrite(dstPath+sorted(os.listdir(dstPath), reverse=True)[0]+"/marked_"+sorted(os.listdir(dstPath), reverse=True)[0]+".jpg", img)
    