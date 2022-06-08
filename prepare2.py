"""
#读取照片并圈出人脸
import numpy as np
import cv2
import face_recognition
image = face_recognition.load_image_file("./image/00.jpg")
#return (A,B,C,D)(top, right, bottom, left) (D,A,B,C)
face_locations = face_recognition.face_locations(image)
print(face_locations)
image1=image*1
image1[:,:,0]=image[:,:,2]
image1[:,:,2]=image[:,:,0]
for (A,B,C,D) in face_locations:
    cv2.rectangle(image1,(D,A),(B,C),(0,255,0),2)
cv2.imshow('image',image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""
#摄像头读取并识别人脸
import numpy as np
import cv2
 
import face_recognition
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
 
#return (A,B,C,D)(top, right, bottom, left) (D,A,B,C)
    face_locations = face_recognition.face_locations(frame)
 
    for (A,B,C,D) in face_locations:
        cv2.rectangle(frame,(D,A),(B,C),(0,255,0),2)
    cv2.imshow('image',frame)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
"""
#人脸比对，单对单的比对，和多对单的比对（对比识别）
import numpy as np
import cv2
import face_recognition
lxy=face_recognition.face_encodings(face_recognition.load_image_file('./image/3.jpg'))
jyh=face_recognition.face_encodings(face_recognition.load_image_file('./image/1.jpg'))
wxh=face_recognition.face_encodings(face_recognition.load_image_file('./image/4.jpg'))
zql=face_recognition.face_encodings(face_recognition.load_image_file('./image/5.jpg'))
#ss=face_recognition.compare_faces([dongqing,lisisi],zhujun)
#hezhao=face_recognition.face_encodings(face_recognition.load_image_file('mypic.jpg'))
#ss=face_recognition.compare_faces(hezhao,lisisi,0.5)
zangjincheng=face_recognition.load_image_file('./image/2.jpg')
 
locations=face_recognition.face_locations(zangjincheng)
for [A,B,C,D] in locations:
    face=zangjincheng[A:C,D:B,:]
    faceencoding=face_recognition.face_encodings(face)
    ss=face_recognition.compare_faces(faceencoding,zangjincheng[0],0.5)
    print(ss)

