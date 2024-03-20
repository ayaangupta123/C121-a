import cv2
import numpy as np
video = cv2.VideoCapture(0)
IMG = cv2.imread("IMG_0596.jpg")
while True:
    r,frame = video.read()
    print(frame)
    frame = cv2.resize(frame,(640,480))
    IMG = cv2.resize(IMG,(640,480))
    u_black = np.array([104,153,70])
    L_black = np.array([30,30,0])
    mask1 = cv2.inRange(frame,L_black,u_black)
    result = cv2.bitwise_and(frame,frame,mask = mask1)
    f = frame - result
    f = np.where(f == 0, IMG,f)
    cv2.imshow("Video",frame)
    cv2.imshow("Mask", f)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
video.release() 
cv2.destroyAllWindows()

