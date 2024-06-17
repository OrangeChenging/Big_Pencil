import cv2
from faced import FaceDetector
from faced.utils import annotate_image

face_detector = FaceDetector()
face_size_threshold = 150 * 150  # 此处设置人脸的最小面积（如15*10）

cap = cv2.VideoCapture(0)  # 使用你的摄像头设备ID替换0

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
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 此处刷新速度设定为1毫秒，可以按'q'退出
        break
    
cap.release()
cv2.destroyAllWindows()