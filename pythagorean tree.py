# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:54:41 2020

@author: Thys
"""

import numpy as np
import matplotlib.pyplot as plt



class Box():
    def __init__(self, left, right, length, angle):
        self.left = left
        self.right = right
        self.angle = angle
        self.legth = length
        
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def getLen(self):
        return np.linalg.norm(self.left-self.right)
    def getAngle(self):
        return self.angle
"""
Rotation matrix
"""
def R_matrix(point, angle):
    matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle),np.cos(angle)]])
    return matrix@point

"""
Recursive function.
Calculate the four points of the current box, plot them, then create two new boxes on top of it with length 1/sqrt(2) and rotations pi/4 and 7pi/4. 
Then apply it to those two boxes
"""     
def recurPythTree(box, count):
    if count>0:
        coords = np.array([box.getLeft(), box.getRight(),box.getRight()+R_matrix([[0],[box.getLen()]],box.getAngle() ),box.getLeft()+R_matrix([[0],[box.getLen()]],box.getAngle() ), box.getLeft()])
        xc = [x[0] for x in coords]
        yc = [y[1] for y in coords]
        plt.plot(xc, yc,color='green',linewidth=0.3*box.getLen())
        box2 = Box(box.getLeft()+R_matrix([[0],[box.getLen()]],abs(box.getAngle())),box.getLeft()+R_matrix([[0],[box.getLen()]],abs(box.getAngle()))+R_matrix([[box.getLen()*(1/np.sqrt(2))],[0]],abs(box.getAngle())+np.pi/4), box.getLen()*(1/np.sqrt(2)), abs(box.getAngle())+np.pi/4)
        recurPythTree(box2, count-1)
        box3 = Box(box.getLeft()+R_matrix([[0],[box.getLen()]],box.getAngle())+R_matrix([[box.getLen()*(1/np.sqrt(2))],[0]],box.getAngle()+1*np.pi/4), box.getRight()+R_matrix([[0], [box.getLen()]],box.getAngle()),box.getLen()*(1/np.sqrt(2)), box.getAngle()+7*np.pi/4)
        recurPythTree(box3, count-1)
        

fig, ax = plt.subplots()  
plt.figure(dpi=2000) 
ax.set_aspect(1)
box1 = Box(np.array([[0],[0]]), np.array([[10],[0]]), 10, 0)

recurPythTree(box1,20)
plt.show()
