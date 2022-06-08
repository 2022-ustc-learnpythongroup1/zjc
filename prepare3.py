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
#识别
import face_recognition

picture_of_me = face_recognition.load_image_file("./image/2.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

unknown_picture = face_recognition.load_image_file("./image/21.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

# Now we can see the two face encodings are of the same person with `compare_faces`!

results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

if results[0] == True:
    print("It's a picture of me!")
else:
    print("It's not a picture of me!")