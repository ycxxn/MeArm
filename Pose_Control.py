from Inverse_Kinematic import pos2theta
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

while(1):
    pos=pos2theta(16.313,0,5.2)
    TXD=R1(pos[0],pos[1],pos[2],0)
    ser.write(TXD)
    time.sleep(1)
    pos=pos2theta(16.313,0,5.2)
    TXD=R1(pos[0],pos[1],pos[2],30)
    ser.write(TXD)
    time.sleep(1)
    pos=pos2theta(13,0,13.2)
    TXD=R1(pos[0],pos[1],pos[2],30)
    ser.write(TXD)
    time.sleep(1)
    pos=pos2theta(13,0,13.2)
    TXD=R1(pos[0],pos[1],pos[2],0)
    ser.write(TXD)
    time.sleep(1)
