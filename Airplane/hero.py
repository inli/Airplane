from airplanes import *
from bullet import *
import pygame

class hero(airplanes):
    """description of class"""
    def __init__(self,path,bgScreen, width, height, bullet):
        airplanes.__init__(self,path, bgScreen, width, height, bullet)
        
        #move key status
        self.left=False
        self.right=False
        self.up=False
        self.down=False

        self.left_t=time.time()
        self.right_t=time.time()
        self.up_t=time.time()
        self.down_t=time.time()

        # init position
        self.x = self.bScreen.x/2 - self.imgWidth/2
        self.y = self.bScreen.y - self.imgHeight
        self.bullet.x=self.x
        self.bullet.y=self.y

        self.rcd_time = time.time()

    def move(self,pace=0.7):
        t = time.time()
        if(self.x>0 and t - self.left_t > 0.15 and self.left == True):
            self.x=self.x-pace
        elif(self.x<self.bScreen.x-self.imgWidth and t - self.right_t > 0.15 and self.right == True):
            self.x=self.x+pace
        elif(self.y>self.bScreen.y*0.8 and self.up_t > 0.1 and self.up == True):
            self.y=self.y-pace
        elif(self.y<self.bScreen.y-self.imgHeight and self.down_t > 0.1 and self.down == True):
            self.y=self.y+pace
    
    def move_one(self,drct):
        '''
        drct[0:left 1:right]
        '''
        if drct == 0:
            self.x = self.x - self.imgWidth/2
        else:
            self.x = self.x + self.imgWidth/2




    #def bullet_on(self):
    #    on_t = time.time()
    #    crt_y = self.y
    #    self.bullets_pos.append([self.x + self.imgWidth/3 , self.y,on_t,crt_y])
    
    def shoot(self,speed = 5):
        """ bullets_pos=[0:x, 1:origin_y, 2:on_time, 3:current_y]"""

        t = time.time()
        if t - self.rcd_time > 0.5:
            

            self.bullets_pos.append([self.x + self.imgWidth/3 , self.y,time.time(),self.y])
            self.bullets_pos.append([self.x + self.imgWidth/6 , self.y - self.bullet.imgHeight/2,time.time(),self.y])
            self.bullets_pos.append([self.x + self.imgWidth*2/3 , self.y - self.bullet.imgHeight/2,time.time(),self.y])
            self.rcd_time = t

        for p in self.bullets_pos:
            cnt_time = time.time() - p[2]
            if(p[3] > 0):
                p[3] = p[1] -  speed * cnt_time *100
                self.bScreen.screen.blit(self.bullet.imgcvt,(p[0],p[3]))
               
            elif(p[3] < 0):
                self.bullets_pos.remove(p)
               
            
          


