from PIL import Image
import pygame
import time

class airplanes(object):
    """description of class"""
   
    def __init__(self,path,bgScreen,width,height,bullet):
        self.imgWidth=width             #width
        self.imgHeight=height           #height
        self.imgName=path
        
        self.imagecvt=pygame.image.load(path).convert()
        self.imagecvt=pygame.transform.scale(self.imagecvt,(self.imgWidth,self.imgHeight))
      
        self.bScreen = bgScreen #背景
        self.bullet=bullet      #子弹
        self.bullets_pos=[]     #子弹位置
        
        
    def display(self,mskcolor):
        self.imagecvt.set_colorkey(mskcolor)  # Black colors will not be blit.
        self.bScreen.screen.blit(self.imagecvt,(self.x,self.y))
   
        