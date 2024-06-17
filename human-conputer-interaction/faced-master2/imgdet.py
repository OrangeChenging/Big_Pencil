
#imgdet.py
import cv2
from faced import FaceDetector
from faced.utils import annotate_image

def fun(name):

    face_detector = FaceDetector()

    name = str(name)
    new_name = name.replace("\\","//")
    img = cv2.imread(new_name)

    rgb_img = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2RGB)

    # Receives RGB numpy image (HxWxC) and
   # returns (x_center, y_center, width, height, prob) tuples. 
    bboxes = face_detector.predict(rgb_img)

   # Use this utils function to annotate the image.
    ann_img = annotate_image(img, bboxes)

   # Show the image
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', ann_img)

    while cv2.getWindowProperty('image', cv2.WND_PROP_VISIBLE) >= 1:
        cv2.waitKey(1)

    cv2.destroyAllWindows()



'''
import cv2
from faced import FaceDetector
from faced.utils import annotate_image

def fun(name):

    face_detector = FaceDetector()

    name = str(name)
    new_name = name.replace("\\","//")
    img = cv2.imread(new_name)
    #img = cv2.imread("C://Users//13590//Downloads//VOCdevkit//VOC2007//JPEGImages//000001.jpg")
    #img = imageio.mimread(name)

    rgb_img = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2RGB)

# Receives RGB numpy image (HxWxC) and
# returns (x_center, y_center, width, height, prob) tuples. 
    bboxes = face_detector.predict(rgb_img)

# Use this utils function to annotate the image.
    ann_img = annotate_image(img, bboxes)

# Show the image
    cv2.imshow('image',ann_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''
