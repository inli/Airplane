import pygame
from pygame.locals import *

class bgScreen(object):
    """description of class"""
    def __init__(self, path, x,y):
        self.imgPath=path
        self.x=x
        self.y=y
        self.screen=pygame.display.set_mode((self.x,self.y),0,32)
        self.background=pygame.image.load(self.imgPath).convert()
   
    
        

