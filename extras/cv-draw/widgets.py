from subprocess import call
from turtle import shape
import cv2, numpy as np

class VideoWidget(object):
    def __init__(self):
        self.topview = np.array(shape)

    def ShowFrame(self, frame:list, identifier:str="Blank"):
        cv2.imshow(identifier, frame)



    def SaveData(data:np.array, filename:str):
        np.savetxt(filename, data, delimiter=',')

    def LoadData(filename:str):
        return np.loadtxt(filename, delimiter='.')