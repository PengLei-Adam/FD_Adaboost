# -*- coding: utf-8 -*-
"""
Class Window for detection

Created on Sun Nov 20 14:45:32 2016

@author: Peng Lei
"""
class FDWnd:
    def __init__(self, wnd_width, wnd_height, 
                 start_x = 0, start_y = 0, step = 4):
        self._width = wnd_width
        self._height = wnd_height
        self._x = start_x
        self._y = start_y
        self._step = step
    def getShape(self):
        return (self._width, self._height)
    def getStart(self):
        return (self._x, self._y)
    def getStep(self):
        return self._step
    def setStep(self, step):
        self._step = step
    def slide(self, func_onSliding):
        #Calling function on sliding windows
        result = []
        for self._y in range(0, self._height, self._step):
            for self._x in range(0, self._width, self._step):
                result += func_onSliding(self)
        self._x = self._y = 0
        return result
        
        
