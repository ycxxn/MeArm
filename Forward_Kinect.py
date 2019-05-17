import numpy as np 

def theta2pos(theta1,theta2,theta3):
    d1=0
    d2=8
    d3=8
    y=d2*np.cos(theta2*np.pi/180)+d3*np.sin(np.pi/2+theta2*np.pi/180-theta3*np.pi/180)
    z=d2*np.sin(theta2*np.pi/180)-d3*np.cos(np.pi/2+theta2*np.pi/180-theta3*np.pi/180)
    x=y*np.cos(theta1*np.pi/180)
    y=y*np.sin(theta1*np.pi/180)
    if x < 0.001:
        x=0.0
    return x,y,z

ans=theta2pos(90,45,90)
print(ans)



