import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime



path = 'Attendence_System/Training images'
images = []
classNames = []
alredy_attended = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def video_overlay(bgimg,img,location):
    img=cv2.resize(img,(281,455)) 
    # h,w=img1.shape[:2]
    h1,w1=img.shape[:2]
    x,y=location
    bgimg[y:y+h1,x:x+w1]=img
    return bgimg

def image_overlay(bgimg,img2,location2):
    # img2=img2.resize(img2,(315,355)) 
    h1,w1=img2.shape[:2]
    x,y=location2
    bgimg[y:y+h1,x:x+w1]=img2
    return bgimg

def markAttendance(name,alredy_attended):
    with open('Attendence_System\Attendance.csv', 'r+') as f:
        myDataList = f.readlines()


        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            if name not in nameList and name not in alredy_attended:
                print("Writing name: Dr",name)
                now = datetime.now()
                dtString = now.strftime("%m/%d/%Y,%H:%M:%S")
                f.writelines(f'\n{name},{dtString}')
                alredy_attended.append(name)
            else:
                print(("ALREADY MARKED"))
                break

encodeListKnown = findEncodings(images)
print('Encoding Complete')

bgimg=cv2.imread('RESOURCES\BACKGROUND.jpg')
print("dimensions=" , bgimg.shape)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

folderModepath = 'RESOURCES\CARDS'
modePathList = os.listdir(folderModepath)

imgModeList=[]
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModepath,path)))
# print(len(imgModeList))







while True:
    success, img = cap.read()
    img2=imgModeList[0]
    merge=video_overlay(bgimg,img,location=(37,80)) 
    merge=image_overlay(bgimg,img2,location2=(351,129)) 
    cv2.namedWindow("Merge", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Merge", 700, 800)
    # imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    facesCurFrame = face_recognition.face_locations(img)
    encodesCurFrame = face_recognition.face_encodings(img, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name, alredy_attended)

    cv2.imshow("Merge",merge)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# /////////////////////////////////////////////////////////////////////

# def video_overlay(bgimg,img1,location1):
#     img1=cv2.resize(img1,(281,455)) 
#     # h,w=img1.shape[:2]
#     h1,w1=img1.shape[:2]
#     x,y=location1
#     bgimg[y:y+h1,x:x+w1]=img1
#     return bgimg

# def image_overlay(bgimg,img2,location2):
#     # img2=img2.resize(img2,(315,355)) 
#     h1,w1=img2.shape[:2]
#     x,y=location2
#     bgimg[y:y+h1,x:x+w1]=img2
#     return bgimg

# bgimg=cv2.imread('RESOURCES\BACKGROUND.jpg')
# cap=cv2.VideoCapture(0)

# print("dimensions=" , bgimg.shape)

# cap.set(3, 640)
# cap.set(4, 480)


# folderModepath = 'RESOURCES\CARDS'
# modePathList = os.listdir(folderModepath)

# imgModeList=[]
# for path in modePathList:
#     imgModeList.append(cv2.imread(os.path.join(folderModepath,path)))
# # print(len(imgModeList))



# while True:
#     success,img1=cap.read()
#     img2=imgModeList[0]
#     merge=video_overlay(bgimg,img1,location1=(37,80)) 
#     merge=image_overlay(bgimg,img2,location2=(351,129)) 
#     cv2.namedWindow("Merge", cv2.WINDOW_NORMAL)
#     cv2.resizeWindow("Merge", 700, 800)
#     cv2.imshow("Merge",merge)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break



