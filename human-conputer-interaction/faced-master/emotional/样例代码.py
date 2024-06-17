# imgdet.py – 处理JPG和PNG图片
import cv2
import dlib
from keras.models import load_model
import numpy as np

def fun(path):
    # 加载人脸检测器和情感分类器模型
    face_detector = dlib.get_frontal_face_detector()
    emotion_classifier = load_model('model_v6_23.hdf5')  

    # 定义情感标签
    emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

    # 加载图片
    image = cv2.imread(path)  # 从传入参数获取图片路径

    # 将图片转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用人脸检测器检测人脸
    faces = face_detector(gray)

    # 对每个人脸进行情感识别
    for face in faces:
        # 提取人脸区域
        (x, y, w, h) = (face.left(), face.top(), face.width(), face.height())
        face_roi = gray[y:y+h, x:x+w]

        # 调整人脸区域大小为模型所需的输入大小
        face_roi = cv2.resize(face_roi, (48, 48))
        face_roi = face_roi.astype('float') / 255.0
        face_roi = np.expand_dims(face_roi, axis=0)
        face_roi = np.expand_dims(face_roi, axis=3)

        # 进行情感分类
        emotion_pred = emotion_classifier.predict(face_roi)[0]
        emotion_label_arg = np.argmax(emotion_pred)
        emotion = emotion_labels[emotion_label_arg]

        # 在人脸上绘制情感标签
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(image, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # 显示结果图片
    cv2.imshow("Emotion Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()