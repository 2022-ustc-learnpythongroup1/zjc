import face_recognition
import cv2
import numpy as np

#   1.以 1/4 分辨率处理每个视频帧（但仍以全分辨率显示）
#   2.仅检测每隔一帧视频中的人脸。

#开摄像头
video_capture = cv2.VideoCapture(0)

#加载示例图片并学习如何识别它
jyh_image = face_recognition.load_image_file("./image/3.jpg")
jyh_face_encoding = face_recognition.face_encodings(jyh_image)[0]

# 创建已知人脸编码及其名称的数组
known_face_encodings = [
    jyh_face_encoding
]
known_face_names = [
    "jiang yuhang"
]

# 初始化一些变量
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

a=0

while a<3:
    #用c f 大小来判断是否识别成功
    c=0
    f=0
    while True:
        # 抓取单帧视频
        ret, frame = video_capture.read()

        # 将视频帧大小调整为 1/4 大小
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # 将图像从 BGR 颜色（OpenCV 使用）转换为 RGB 颜色（face_recognition使用）
        rgb_small_frame = small_frame[:, :, ::-1]

        #仅处理每隔一帧视频以节省时间
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                #查看人脸是否与已知人脸匹配
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.38)
                name = "Unknown"
            
                # 如果在known_face_encodings中找到匹配项，只需使用第一个匹配项即可。
                # 如果匹配项中为 True：
                # first_match_index = matches.index（True）
                # 名称 = known_face_names[first_match_index]
                # 或者，使用与新面距离最小的已知人脸
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    c=c+1
                else:
                    f=f+1
                face_names.append(name)

        process_this_frame = not process_this_frame

        if f>=2:
            a=a+1
            print("0")
            break
        if c>=20:
            print("1")
            break

if a<=3:
    print("1")
if a>3:
    print("0")
# 释放网络摄像头
video_capture.release()
cv2.destroyAllWindows()