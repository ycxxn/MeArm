import numpy as np
import cv2
import serial
import time
ser=serial.Serial("/dev/ttyACM0", baudrate = 115200 , timeout = 0.5) 
#linux port use /dev/ttyACMX 
#Windows port use COMX
 
def R1(data1,data2,data3,data4):  
    senddata = bytearray()

    senddata.append(0xff)
    senddata.append(0x55)
    senddata.append(data1)
    senddata.append(data2)
    senddata.append(data3)
    senddata.append(data4)
    return senddata

cap = cv2.VideoCapture(2)

def nothing(x):
    pass

cv2.namedWindow('image')
#cv2.resizeWindow("image",320,240)
cv2.createTrackbar('lh','image',20,255,nothing)
cv2.createTrackbar('ls','image',16,255,nothing)
cv2.createTrackbar('lv','image',40,255,nothing)
cv2.createTrackbar('hh','image',35,255,nothing)
cv2.createTrackbar('hs','image',255,255,nothing)
cv2.createTrackbar('hv','image',255,255,nothing)

kernel = np.ones((8,8),np.uint8)
old_cy = 240
i=0
while(True):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (320, 240))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    

    lh = cv2.getTrackbarPos('lh','image')
    ls = cv2.getTrackbarPos('ls','image')
    lv = cv2.getTrackbarPos('lv','image')
    hh = cv2.getTrackbarPos('hh','image')
    hs = cv2.getTrackbarPos('hs','image')
    hv = cv2.getTrackbarPos('hv','image')

    lower = np.array([lh,ls,lv])
    upper = np.array([hh,hs,hv])
    mask = cv2.inRange(hsv, lower, upper)
    mask=cv2.erode(mask,kernel,iterations = 2)
    mask=cv2.dilate(mask,kernel,iterations = 2)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame,contours,-1,(0,0,255),3)
    
    areas = [cv2.contourArea(c) for c in contours]
    a = len(areas)

    if a > 0 :
        max_index = np.argmax(areas)
        cnt=contours[max_index]
        M=cv2.moments(cnt)
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
        cv2.circle(frame, (cx, cy), 10, (1, 227, 254), -1)
        if max(areas) < 300:
            i=0
            print(i)
        if max(areas) > 600:
            i=i+1
            print(i)
            if i ==100:
                TXD=R1(90,160,60,0)
                ser.write(TXD)
                time.sleep(1)
                TXD=R1(90,160,60,28)
                ser.write(TXD)
                time.sleep(1)
                TXD=R1(90,90,90,28)
                ser.write(TXD)
                time.sleep(1)
                TXD=R1(60,90,90,28)
                ser.write(TXD)
                time.sleep(1)
                TXD=R1(60,90,90,0)
                ser.write(TXD)
                time.sleep(1)
                i=0
        
    cv2.imshow('frame',frame)
    cv2.imshow('image',mask)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()