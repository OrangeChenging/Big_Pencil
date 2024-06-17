# './video/zhou.mp4'

# videodet.py
import cv2
from faced import FaceDetector
from faced.utils import annotate_image


def fun(name):

    face_detector = FaceDetector()

    name = str(name)
    new_name = name.replace("\\", "//")
    cap = cv2.VideoCapture(new_name)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        rgb_img = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2RGB)

        bboxes = face_detector.predict(rgb_img)
        ann_img = annotate_image(frame, bboxes)

        cv2.imshow('image', ann_img)

        # 使用 'q' 键来退出视频流
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


'''
import cv2
from faced import FaceDetector
from faced.utils import annotate_image

def fun(name):
    face_detector = FaceDetector()
    face_size_threshold = 90 * 90  # 此处设置人脸的最小面积
    
    name = str(name)
    new_name = name.replace("\\","//")
    cap = cv2.VideoCapture(new_name)  # 使用你的视频文件路径替换'your_video.mp4'

    while True:
        ret, img = cap.read()

        if not ret:
            break

        rgb_img = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2RGB)

        bboxes = face_detector.predict(rgb_img)
    # 过滤小于阈值的人脸
        bboxes = [bbox for bbox in bboxes if bbox[2]*bbox[3] > face_size_threshold]

        annotated_img = annotate_image(img, bboxes)

        cv2.imshow('image',annotated_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 此处刷新速度设定为1毫秒，可以调整
            break
    
    cap.release()
    cv2.destroyAllWindows()
'''

'''
face_detector = FaceDetector()
face_size_threshold = 150 * 150  # 此处设置人脸的最小面积（如15*10）

cap = cv2.VideoCapture('your_video.mp4')  # 使用你的视频文件路径替换'your_video.mp4'

while True:
    ret, img = cap.read()

    if not ret:
        break

    rgb_img = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2RGB)

    bboxes = face_detector.predict(rgb_img)
    # 过滤小于阈值的人脸
    bboxes = [bbox for bbox in bboxes if bbox[2]*bbox[3] > face_size_threshold]

    annotated_img = annotate_image(img, bboxes)

    cv2.imshow('image', annotated_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 此处刷新速度设定为1毫秒，可以调整
        break

cap.release()
cv2.destroyAllWindows()
'''
