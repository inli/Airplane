import pygame
class bullet(object):
    """description of class"""
    def __init__(self, path, imgWidth,imgHeight,mskcolor):
        self.imgPath=path
        self.imgWidth=imgWidth
        self.imgHeight=imgHeight
        self.imgcvt=pygame.image.load(self.imgPath).convert()
        self.imgcvt=pygame.transform.scale(self.imgcvt,(imgWidth,imgHeight))
        self.imgcvt.set_colorkey(mskcolor)  # Black colors will not be blit.

        self.x=0
        self.y=0
    
        
      


