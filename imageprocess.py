import cv2
import numpy as np

class imgProcess:
    def __init__(self,frame,img):
        self.frame = frame
        self.img = img

    def drawContours(self):
        self.contours,self.hierarchy = cv2.findContours(self.img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(self.frame,self.contours,-1,(0,0,255),3)

    def getArea(self):
        self.areas = [cv2.contourArea(c) for c in self.contours]
        self.a = len(self.areas)
        if self.a > 0 :
            self.max_index = np.argmax(self.areas)
            return max(self.areas)

a=None 
b=2
if (a or b) is not None :
    print("yes")