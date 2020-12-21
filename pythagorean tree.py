# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:54:41 2020

@author: Thys Steynberg
"""

import numpy as np
import matplotlib.pyplot as plt

class Box():
    """
    Global members:
        data: np array of data points
        lengthArr: array of lengths of boxes
    __init__() members:
        Box class. Contains left and right "bottom" vertices, the length of one side
        and the angle that it is rotated with respect to the x-axis.
    """
    data = np.array([[[0],[0]],[[0],[0]],[[0],[0]],[[0],[0]],[[0],[0]]])
    lengthArr = [0]
    def __init__(self, left, right, length, angle):
        self._left = left
        self._right = right
        self._angle = angle
        self._length = length    
    @property 
    def left(self):
        return self._left
    @property 
    def right(self):
        return self._right
    @property 
    def angle(self):
        return self._angle
    @property 
    def length(self):
        return self._length

def R_matrix(point, angle):
    """
    Rotation matrix
    """
    matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle),np.cos(angle)]])
    return matrix@point

def recurPythTree(box, count):
    """
    Recursive function.
    Calculate the four points of the current box, plot them, then create two new boxes on top of it with length 1/sqrt(2) and rotations pi/4 and 7pi/4. 
    Then apply it to those two boxes
    """ 
    if count>0:
        #Get the coordinates of the four vertices + the initial vertex and store data in box.data, also store length in Box.lengthArr
        v1 = box.left
        v2 = box.right
        v3 = box.right+R_matrix([[0],[box.length]],box.angle)
        v4 = box.left+R_matrix([[0],[box.length]],box.angle)
        
        coords = np.array([v1,v2,v3,v4,v1])
        Box.lengthArr = np.append(Box.lengthArr, box.length)
        Box.data = np.append(Box.data, coords, axis=0)
        box2 = Box(v4,v1+R_matrix([[0],[box.length]],box.angle)+R_matrix([[box.length*(1/np.sqrt(2))],[0]],box.angle+np.pi/4), box.length*(1/np.sqrt(2)), box.angle+np.pi/4)
        box3 = Box(v1+R_matrix([[0],[box.length]],box.angle)+R_matrix([[box.length*(1/np.sqrt(2))],[0]],box.angle+1*np.pi/4), v3,box.length*(1/np.sqrt(2)), box.angle+7*np.pi/4)
        recurPythTree(box2, count-1)
        recurPythTree(box3, count-1)
           
def plot(data, lengths):
    """
    Plot the data given as: 
        Box.data is the coordinates of each point. Every box has 5 coordinates.
        Box.length is an array of the lengths of the box lines
    """
    counter = 0
    xc = np.array([])
    yc = np.array([])
    fig, ax = plt.subplots()  
    plt.figure(dpi=1000) 
    ax.set_aspect(1)
    for dataSection in data:
        counter+=1
        xc = np.append(xc, dataSection[0])
        yc = np.append(yc, dataSection[1])
        if(counter%5 == 0):
            plt.plot(xc, yc,color='green',linewidth = 0.35*lengths[(counter//5)-1])
            xc = np.array([])
            yc = np.array([])
    plt.show()

"""
Initial call to tree function
"""
box1 = Box(np.array([[0],[0]]), np.array([[10],[0]]), 10, 0)
recurPythTree(box1,20)
plot(Box.data, Box.lengthArr)

