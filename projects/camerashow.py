import cv2
# code by shuchun.liu
# email:liuscgood@gmail.com
def detect(img):
    #face detection
    hc = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_alt2.xml")
    faces = hc.detectMultiScale(img)
    
    #eye detection
    hc_eye=cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")
    eyes=hc_eye.detectMultiScale(img)

     #smile detection
    hc_smile=cv2.CascadeClassifier("haarcascades/haarcascade_mcs_nose.xml")
    smiles=hc_smile.detectMultiScale(img)
    
    for face in faces:
      cv2.rectangle(img, (face[0], face[1]), (face[0] + face[2], face[1] + face[3]), (127, 255, 0), 2)
      #write into the words
      font = cv2.FONT_HERSHEY_COMPLEX_SMALL
      cv2.putText(img,"People",(face[0]-40,face[1]-5), font, 1,(255,255,255),2)
      
    for eye in eyes:
      cv2.rectangle(img, (eye[0], eye[1]), (eye[0] + eye[2], eye[1] + eye[3]), (0, 0, 255), 2)
   
##    for smile in smiles:
##        cv2.rectangle(img, (smile[0], smile[1]), (smile[0] + smile[2], smile[1] + smile[3]), (250, 250, 0), 2)
        
                      
# create windows
cv2.namedWindow("Camera",cv2.WINDOW_AUTOSIZE)

vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False
    
while rval:    
    rval, frame = vc.read()    
    #face detection
    detect(frame)

    #display image
    cv2.imshow("Camera", frame)
    
    key = cv2.waitKey(5)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("Camera")




