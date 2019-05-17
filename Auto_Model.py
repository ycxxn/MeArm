import serial
import time
ser=serial.Serial("/dev/ttyACM0", baudrate = 115200 , timeout = 0.5)

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
    TXD=R1(90,160,50,0)
    ser.write(TXD)
    time.sleep(1)
    TXD=R1(90,160,50,28)
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
