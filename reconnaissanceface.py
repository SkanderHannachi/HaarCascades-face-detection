import cv2 
import numpy as np 

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/lbpcascades/lbpcascade_frontalface.xml')


def draw(coor,img) : 
    """Déssine un rectangle quand il y'a detection faciale. """
    for (x,y,w,h) in coor:
        cv2.rectangle(img,(x,y),(x+w,y+h),(100,10,100),2)
        roi_color = img[y:y+h, x:x+w]


while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print(face_cascade.getFeatureType())
    faces = face_cascade.detectMultiScale(gray, 1.3, 3)
    print(faces)
    draw(faces,frame)    
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
