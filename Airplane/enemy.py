import random
from airplanes import *
import time
import pygame.mixer
class enemy(airplanes):
    """description of class"""
    def __init__(self, path, bgScreen, width, height, bullet,level=1):
        airplanes.__init__(self,path, bgScreen, width, height, bullet)
        self.boom_img = pygame.image.load('../img/boom.png').convert()
        self.boom_img = pygame.transform.scale(self.boom_img,(width,height))
        self.boom_img.set_colorkey((0,0,0))#mask color = black
                
        self.life = level + 5

    def init_position(self,x=-1):
        if(x==-1):
            self.x = random.random()*(300-self.imgHeight)+self.imgHeight/2
        else:
            self.x = x
        self.y = self.imgHeight/2
        self.rcd_time = 0.0
        self.start_time = time.time()

    def move(self,speed=3):
        self.y =self.imgHeight/2 + speed * int(time.time() - self.start_time)*10

  
    def shoot(self,start_time,speed = 1,gap = 5):
       
        #bullet on
        t = time.time() - start_time
        if(t-self.rcd_time>gap):
            on_t = time.time()
            crt_y = self.y
            self.bullets_pos.append([self.x , self.y,on_t,crt_y])
            self.rcd_time = t
        
        #blit bullets
        for p in self.bullets_pos:
            cnt_time = int((time.time() - p[2])*100)
            crt_y = p[1]
            crt_x = p[0]
            if(crt_y<self.bScreen.y):
                crt_y = p[1] + speed * cnt_time
            self.bScreen.screen.blit(self.bullet.imgcvt,(crt_x,crt_y))
            

    def to_bottom(self):
        if(self.y>self.bScreen.y*0.8):
            return True
        else:
            return False
    
    def shotby(self,airplane):
       
       for p in airplane.bullets_pos:     
           #print(abs(p[0] - self.x),p[3])
           if (abs(p[0] - self.x) < self.imgWidth and p[3] < self.y - self.imgHeight/2) :
               airplane.bullets_pos.remove(p)
               pygame.init()
               boom_sound = pygame.mixer.Sound("../img/boom2.wav")
               boom_sound.set_volume(0.2)
               boom_sound.play()
               self.imagecvt.set_alpha(self.life * 5 + 70)
               self.life -= 1
               if self.life == 0:
                   return True
           else:
               return False
    
            
            
            
            
           


