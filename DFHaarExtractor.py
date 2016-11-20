# -*- coding: utf-8 -*-
"""
Haar feature extractor
Created on Sun Nov 20 15:20:51 2016

@author: Peng Lei
"""

def rectSum(interimg, x, y, width, height):
    #compute the sum of pixels in a window from the intergral image
    topLeft = (x, y)
    topRight = (x + width - 1, y)
    bottomLeft = (x, y + height - 1)
    bottomRight = (x + width - 1, y + height - 1)
    return interimg[bottomRight] - interimg[topRight] \
            + interimg[topLeft] - interimg[bottomLeft]

class DFHaarExtractor:
    def __init__(self, sp_x, sp_y):
        self._xSplit = sp_x
        self._ySplit = sp_y
        self.score = 0 # for compare

    def setInterImg(self, img):
        self._interImage =  img       
        
    def compute(self, wnd):
        state = True
        wid, hei = wnd.getShape
        w, h= int(wid / self._xSplit), int(hei / self._ySplit)
        feat = 0
        for y in range(0, hei, h):
            for x in range(0, wid, w):
                s = rectSum(self._interImage, x, y, w, h)
                feat += s if state else (-s)
                state = not state
            state = not state
        return feat
        