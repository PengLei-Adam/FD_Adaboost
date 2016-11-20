# -*- coding: utf-8 -*-
"""
Image Object for image processing based on numpy as the data matrix.
Functions :
    Convert source image to integral image.
    
Created on Mon Nov 14 21:59:22 2016

@author: Peng Lei
"""

import numpy as np
import cv2

class FDImage:
    def __init__(self, img):
        if isinstance(img, basestring):
            self.readFile(img)
        elif isinstance(img, np.ndarray):
            self.readData(img)
        else:
            print 'Error type for initiation'
    
    
    def readFile(self, img_path):
        img = cv2.imread(img_path)
        """
        if img null :
            throws ...
        """
        self.data = img
        if img.ndim == 2:
            self.height, self.width = img.shape
            self.channels = 1
        elif img.ndim == 3:
            self.height, self.width, self.channels = img.shape
    def readData(self, img):
        self.data = img;
        if img.ndim == 2:
            self.height, self.width = img.shape
            self.channels = 1
        elif img.ndim == 3:
            self.height, self.width, self.channels = img.shape
            
    def cvtIntegral(self):
        integral = np.zeros((self.height, self.width))
        imgGray = self.cvtGray()
        s = 0
        for i in range(self.width):
            s += imgGray[0, i]
            integral[0, i] = s
        for j in range(1, self.height):
            s = 0
            for i in range(self.width):
                s += imgGray[j, i]
                integral[j, i] = integral[j - 1, i] + s
        
        return integral
        
    def cvtGray(self):
        if self.channels == 1:
            return self.data
        elif self.channels == 3:
            temp = np.zeros((self.height, self.width))
            for i in range(self.height):
                for j in range(self.width):
                    bgr = self.data[i,j]
                    temp[i, j] = bgr[0]*0.114 + bgr[1]*0.587 + bgr[2]*0.299
            return temp