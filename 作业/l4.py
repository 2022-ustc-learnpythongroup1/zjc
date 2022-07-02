
import face_recognition
import cv2
import numpy as np

#为提高效率做出：
#   1.以 1/4 分辨率处理每个视频帧（但仍以全分辨率显示）
#   2.仅检测每隔一帧视频中的人脸。

video_capture = cv2.VideoCapture(0)  #开摄像头

#加载示例图片并学习如何识别它
jyh_image = face_recognition.load_image_file("./image/1.jpg")
jyh_face_encoding = face_recognition.face_encodings(jyh_image)[0]

zjc_image = face_recognition.load_image_file("./image/2.jpg")
zjc_face_encoding = face_recognition.face_encodings(zjc_image)[0]

lxy_image = face_recognition.load_image_file("./image/3.jpg")
lxy_face_encoding = face_recognition.face_encodings(lxy_image)[0]

wxh_image = face_recognition.load_image_file("./image/4.jpg")
wxh_face_encoding = face_recognition.face_encodings(wxh_image)[0]

zql_image = face_recognition.load_image_file("./image/4.jpg")
zql_face_encoding = face_recognition.face_encodings(zql_image)[0]

# 创建已知人脸编码及其名称的数组
known_face_encodings = [
    jyh_face_encoding,
    zjc_face_encoding,
    lxy_face_encoding,
    wxh_face_encoding,
    zql_face_encoding
]
known_face_names = [
    "jiang yuhang",
    "zang jingcheng",
    "lu xingyu",
    "wang xihe",
    "zhang qilin"
]

# 初始化一些变量
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # 抓取单帧视频
    ret, frame = video_capture.read()

    # 将视频帧大小调整为 1/4 大小
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # 将图像从 BGR 颜色（OpenCV 使用）转换为 RGB 颜色（face_recognition使用）
    rgb_small_frame = small_frame[:, :, ::-1]

    #仅处理每隔一帧视频以节省时间
    if process_this_frame:
        # 查找当前视频帧中的所有人脸和人脸编码
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            #查看人脸是否与已知人脸匹配
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
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

            face_names.append(name)

    process_this_frame = not process_this_frame


    # 显示结果
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # 将视频帧大小调回原来大小
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # 在脸部周围画一个框
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # 在脸部下方标出名字
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # 显示生成的图像
    cv2.imshow('Video', frame)

    # 点击键盘上的“q”退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放网络摄像头
video_capture.release()
cv2.destroyAllWindows()