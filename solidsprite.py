import pygame
from box import Box
import numpy as np
from sprite import Sprite
class SolidSprite(Box,Sprite):
    def __init__(self,x,y,w,h, x2, y2, w2, h2,filename,frame_nb,z_index=0,transparent_color=(255,0,0)):
        Sprite.__init__(self, x, y, w, h, filename, frame_nb, z_index, transparent_color)
        Box.__init__(self,x,y,w,h,x2, y2, w2, h2)