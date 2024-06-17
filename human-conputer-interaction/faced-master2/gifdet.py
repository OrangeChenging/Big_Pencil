#gifdet.py
import cv2
from faced import FaceDetector
from faced.utils import annotate_image

def fun(name):

    face_detector = FaceDetector()

    name = str(name)
    new_name = name.replace("\\","//")
    cap = cv2.VideoCapture(new_name)

    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break

        rgb_img = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2RGB)

        bboxes = face_detector.predict(rgb_img)
        ann_img = annotate_image(frame, bboxes)

        cv2.imshow('image', ann_img)

        # 用 'q' 键控制退出
        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break

    cap.release()
    cv2.destroyAllWindows()


'''
from PIL import Image, ImageSequence
import cv2
import numpy as np
from faced import FaceDetector
from faced.utils import annotate_image

def fun(name):

    face_detector = FaceDetector()

    name = str(name)
    new_name = name.replace("\\","//")
    im = Image.open(new_name) # 确保你把 'path_to_your_gif.gif' 替换成你的 GIF 文件路径

    # 分帧处理 GIF 图片
    for i, frame in enumerate(ImageSequence.Iterator(im)):
        frame = frame.convert('RGB') # 转化为 RGB

        # 转换 PIL.Image 对象为 OpenCV 中的 numpy 数组
        np_image = np.array(frame)

        # 对图像进行人脸检测
        bboxes = face_detector.predict(np_image)

        # 标注检测结果并将图像转化回RGB模式以正确显示
        ann_img = annotate_image(np_image, bboxes)
        ann_img = cv2.cvtColor(ann_img, cv2.COLOR_BGR2RGB)

        # 利用OpenCV显示图像
        cv2.imshow('Frame', ann_img)


        # 判断是否需要结束展示（例如，如果按下了"q"键）。
        if cv2.waitKey(80) & 0xFF == ord('q'): # 每800毫秒显示一帧
            break

    cv2.destroyAllWindows()
    '''