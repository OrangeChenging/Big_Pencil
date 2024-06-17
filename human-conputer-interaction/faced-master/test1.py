import dlib
from skimage import io
detector = dlib.get_frontal_face_detector()
img = io.imread("10.jpg")
win = dlib.image_window()
win.set_image(img)
faces = detector(img, 1)
print("人脸数：", len(faces))
win.add_overlay(faces)
dlib.hit_enter_to_continue()
