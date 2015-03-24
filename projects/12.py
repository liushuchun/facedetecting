##import numpy as np
##import cv2
##
##face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
##eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
##
##img = cv2.imread('one.jpg')
##gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##
##
##faces = face_cascade.detectMultiScale(gray, 1.3, 5)
##for (x,y,w,h) in faces:
##    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
##    roi_gray = gray[y:y+h, x:x+w]
##    roi_color = img[y:y+h, x:x+w]
##    eyes = eye_cascade.detectMultiScale(roi_gray)
##    for (ex,ey,ew,eh) in eyes:
##        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
##
##cv2.imshow('img',img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()
import cv2

##def detect(path):
##    img = cv2.imread(path,0)
##    cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
##    rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (10,10))
##
##    if len(rects) == 0:
##        return [], img
##    rects[:, 2:] += rects[:, :2]
##    return rects, img
##
##def box(rects, img):
##    for x1, y1, x2, y2 in rects:
##        cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 1), 2)
##    cv2.imwrite('detected.jpg', img);
##
##rects, img = detect("one.jpg")
##box(rects, img)

import cv2

img = cv2.imread("cat.jpg")
hc = cv2.CascadeClassifier("haarcascades/catface.xml")
faces = hc.detectMultiScale(img)

for face in faces:
  cv2.rectangle(img, (face[0], face[1]), (face[0] + face[2], face[1] + face[3]), (127, 255, 0), 2)

cv2.imshow("Lenna's face", img)
if cv2.waitKey(5000) == 27:
  cv2.destroyWindow("Lenna's face")
cv2.imwrite("LennaFace.jpg", img)
