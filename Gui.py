import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
cv2.namedWindow('MeArm_Control')

# create trackbars for color change
cv2.createTrackbar('motor_1','MeArm_Control',90,180,nothing)
cv2.createTrackbar('motor_2','MeArm_Control',90,180,nothing)
cv2.createTrackbar('motor_3','MeArm_Control',90,180,nothing)
cv2.createTrackbar('motor_4','MeArm_Control',0,30,nothing)

img=cv2.imread("mearm.jpg")
img=cv2.resize(img,(640,480))
while(1):
    cv2.imshow('MeArm_Control',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
    # get current positions of four trackbars
    motor_1 = cv2.getTrackbarPos('motor_1','MeArm_Control')
    motor_2 = cv2.getTrackbarPos('motor_2','MeArm_Control')
    motor_3 = cv2.getTrackbarPos('motor_3','MeArm_Control')
    motor_4 = cv2.getTrackbarPos('motor_4','MeArm_Control')
    print("motor_1:",motor_1,"\t","motor_2:",motor_2,"\t","motor_3:",motor_3,"\t","motor_4:",motor_4)

cv2.destroyAllWindows()