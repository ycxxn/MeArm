import numpy as np 
def pos2theta(p0x,p0y,p0z):
    p0x=p0x-5
    #parameter
    d1 = 5.2
    a2 = 8
    a3 = 8
    theta1 = np.arctan2(p0y,p0x)
    p1x = p0x*np.cos(theta1)+p0y*np.sin(theta1)
    p1z = p0z-d1
    c = np.sqrt(p1x**2+p1z**2)
    #Law of cosines
    alpha = np.arccos((a2**2+c**2-a3**2)/(2*a2*c))
    beta = np.arccos((a2**2+a3**2-c**2)/(2*a2*a3))
    gamma = np.arctan(p1x/p1z)
    
    theta2 = -np.pi/2+gamma-alpha
    theta3 = np.pi-beta

    def deg2rad(theta):
        return theta*180/np.pi

    # return 90+int(deg2rad(theta1)),180+int(deg2rad(theta2)),int(deg2rad(theta3))
    return 90+int(deg2rad(theta1)),180+int(deg2rad(theta2)),90-(int(deg2rad(theta3)+int(deg2rad(theta2))))



    