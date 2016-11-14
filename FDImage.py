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
    def __init__(self, img_path):
        self.readFile(img_path)
    
    def __init__(self, img_data, img_w, img_h, img_ch):
        self.data = img_data
        self.width = img_w
        self.height = img_h
        self.channels = img_ch
    
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
            
    def cvtIntegral(self):
        integral = np.zeros((self.height, self.width))
        imgGray = self.cvtGray()
        
        
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