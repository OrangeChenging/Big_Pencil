import dlib
import cv2

# 加载人脸检测器
detector = dlib.get_frontal_face_detector()

# 读取图片
img = cv2.imread("6.jpg")

# 将图片从BGR转换为灰度图，因为dlib的人脸检测器需要灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 检测人脸
faces = detector(gray, 1)

# 打印人脸数
print("人脸数：", len(faces))

# 在图片上添加label
for i, d in enumerate(faces):
    # 计算人脸矩形框的左上角和右下角坐标
    x1 = d.left()
    y1 = d.top()
    x2 = d.right()
    y2 = d.bottom()

    # 在图片上绘制矩形框和label
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(img, f"Face {i+1}", (x1, y1-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# 显示图片
cv2.imshow("Faces detected", img)

# 等待用户按键，然后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存带有label的图片（如果需要）
cv2.imwrite("6_faces_labeled.jpg", img)


array=[  2   1   7   0   0   4   0  14   0  27  61 143 255 255 252 255 149 21  6  16   0   0   7   0   0   0   0   0]