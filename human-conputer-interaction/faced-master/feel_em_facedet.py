import cv2
from feel_em import process_frame
cap = cv2.VideoCapture(0)  # 启动摄像头，参数0代表默认的摄像头

while True:
    ret, frame = cap.read()  # 摄像头返回两个参数，一个是布尔值，代表是否捕捉成功，另一个是帧

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 将捕获的帧转换为灰度图
    processed_frame = process_frame(gray, frame)  # 自定义的process_frame函数用于处理帧。

    if processed_frame is not None:
        cv2.imshow('Real Time Emotion Detection', processed_frame)  # 显示处理后的帧

    if cv2.waitKey(1) & 0xFF == ord('q'):  # 如果按了 Q 键就退出
        break

cap.release()  # 使用完摄像头之后，需要释放，否则无法被其他程序调用
cv2.destroyAllWindows()  # 销毁所有窗口