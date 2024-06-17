import cv2
import dlib
import numpy as np
from keras.models import load_model
from moviepy.editor import ImageSequenceClip

# 加载人脸检测器和情感分类器模型
face_detector = dlib.get_frontal_face_detector()
emotion_classifier = load_model('emotional\\model_v6_23.hdf5')

# 定义情感标签
emotion_labels = ['Angry', 'Disgust', 'Fear',
                  'Happy', 'Sad', 'Surprise', 'Neutral']


def process_frame(gray, frame):
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
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, emotion, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    return frame


def process_img_or_png(path):
    # 加载图片
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    processed_frame = process_frame(gray, image)

    # 显示结果图片
    cv2.imshow("Emotion Detection", processed_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


'''
def process_gif(path):
    # 读取gif文件并将其转换为帧列表
    gif = cv2.VideoCapture(path)
    frames = []
    while True:
        ret, frame = gif.read()
        if not ret:
            break
        frames.append(frame)

    output_frames = []

    # 对每一帧进行情感分析
    for frame in frames:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        processed_frame = process_frame(gray, frame)

        # 保存处理后的帧到新的列表中，以便稍后将其重新组合成gif
        output_frames.append(processed_frame)

    # 组合帧成gif
    output_clip = ImageSequenceClip(output_frames, fps=24)
    output_clip.write_gif("output.gif")
    from PIL import Image


def process_mp4(path):
    # 打开视频文件
    cap = cv2.VideoCapture(path)

    # 为输出视频文件定义编码器和创建 VideoWriter 对象
    fourcc = cv2.VideoWriter_fourcc(*'MP4V') 
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

    while(cap.isOpened()):
        ret, frame = cap.read()

        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            processed_frame = process_frame(gray, frame)

            # 将帧写入到文件
            out.write(processed_frame)

            # 显示帧
            cv2.imshow('Video Emotion Detection', processed_frame)

            # 按下 Q 键退出
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # 释放视频文件和保存的文件
    cap.release()
    out.release()

    # 释放所有窗口
    cv2.destroyAllWindows()'''


def process_gif(path):
    cap = cv2.VideoCapture(path)
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            processed_frame = process_frame(gray, frame)
            if processed_frame is not None:
                # 显示帧
                cv2.imshow('GIF Emotion Detection', processed_frame)
                # 增加等待时间让帧显示得更慢
                if cv2.waitKey(35) & 0xFF == ord('q'):
                    break
        else:
            break
    # 播放结束后释放所有资源
    cap.release()
    cv2.destroyAllWindows()


def process_mp4(path):
    cap = cv2.VideoCapture(path)
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            processed_frame = process_frame(gray, frame)

            # 显示帧
            cv2.imshow('Video Emotion Detection', processed_frame)

            # 按下 Q 键退出
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    # 视频处理结束后释放所有资源
    cap.release()
    cv2.destroyAllWindows()
