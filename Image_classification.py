from imageprocess import imgProcess
import cv2
import numpy as np 
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

kernel = np.ones((8,8),np.uint8)
i,j=0,0
while(True):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (320, 240))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask_1 = cv2.inRange(hsv, np.array([20,16,40]), np.array([35,100,255]))
    mask_1=cv2.erode(mask_1,kernel,iterations = 2)
    mask_1=cv2.dilate(mask_1,kernel,iterations = 2)
    img_1 = imgProcess(frame,mask_1)
    img_1.drawContours()

    mask_2 = cv2.inRange(hsv, np.array([20,50,40]), np.array([35,255,255]))
    mask_2=cv2.erode(mask_2,kernel,iterations = 2)
    mask_2=cv2.dilate(mask_2,kernel,iterations = 2)
    img_2 = imgProcess(frame,mask_2)
    img_2.drawContours()
    print(img_1.getArea(),img_2.getArea())

    if img_1.getArea() is not None:
        
        if (img_1.getArea() < 300):
            i=0

        if img_1.getArea() > 600:
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
    if img_2.getArea() is not None:

        if (img_2.getArea() < 300):
            j=0

        if img_2.getArea() > 600:
            j=j+1
            print(j)
            if j==100:
                TXD=R1(90,160,60,0)
                ser.write(TXD)
                time.sleep(1)
                TXD=R1(90,160,60,28)
                ser.write(TXD)
                time.sleep(1)
                TXD=R1(90,90,90,28)
                ser.write(TXD)
                time.sleep(1)
                TXD=R1(120,90,90,28)
                ser.write(TXD)
                time.sleep(1)
                TXD=R1(120,90,90,0)
                ser.write(TXD)
                time.sleep(1)
                j=0

    mask = mask_1 + mask_2
    cv2.imshow('frame',frame)
    cv2.imshow('image',mask)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()