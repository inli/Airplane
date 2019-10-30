import pygame
from pygame.locals import *
from sys import exit 
from hero import *
from bgScreen import *
from enemy import *
from bullet import *
from hero import *
from setting import *
import time


def key_control(hero0,set):
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            print ("exit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                hero0.move_one(0)
                hero0.left = True
                hero0.left_t = time.time()
            elif event.key == K_d or event.key == K_RIGHT:
                hero0.move_one(1)
                hero0.right = True
                hero0.right_t = time.time()
            elif event.key == K_w or event.key == K_UP:
                hero0.up = True
            elif event.key == K_s or event.key == K_DOWN:
                hero0.down = True
            #elif event.key == K_SPACE:
            #    hero0.bullet_on()
            elif event.key == K_p:
                set.gamePause()

        elif event.type == KEYUP:
            if event.key == K_a or event.key == K_LEFT:
                hero0.left = False
            elif event.key == K_d or event.key == K_RIGHT:
                hero0.right = False
            elif event.key == K_w or event.key == K_UP:
                hero0.up = False
            elif event.key == K_s or event.key == K_DOWN:
                hero0.down = False

def new_enemy(flag=0):
    # flag:0,1,2,3,4
    path = '../img/enemy'+str(flag)+'.png'
    enemy_n=enemy(path,bgScreen,30+flag,30+flag,bullet1,flag)
    enemy_n.init_position()
    return enemy_n


    
if __name__=="__main__":
   

    #setting
    BLACK=(0,0,0)
    WHITE=(255,255,255)

    bgImageFile='../img/bg2.png'
    bulImageFile0 =  '../img/bullet0.png'
    bulImageFile1 =  '../img/bullet1.png'
    heroImageFile = '../img/air0.png'

    bgScreen=bgScreen(bgImageFile,300,600)
   
    bullet0 = bullet(bulImageFile0,10,10,WHITE)
    bullet1 = bullet(bulImageFile1,5,5,BLACK)
    
    hero0 = hero(heroImageFile,bgScreen,50,50,bullet0)
    
    
    set = setting(bgScreen)

    start_time = time.time()
    rcd_time = 0
    enemys = []
    score = 0

    boom_blit = []

    
    set.gameload()
    while set.game_on:
       
        bgScreen.screen.blit(bgScreen.background,(0,0))
        hero0.display(WHITE)
        
        t = time.time() - start_time
        gap = 50                    #飞机之间的最小间隔
        new_en_pos = range(bgScreen.x//gap)
        new_en_pos = random.sample(new_en_pos,2)
        

        if (t - rcd_time > 2):
            for i in new_en_pos:
                type = int(random.random()*4)
                new_en = new_enemy(type)
                new_en.init_position(i*gap)
                enemys.append(new_en)
                
            rcd_time = t
        
        for en in enemys:
            en.display(WHITE)
            en.move()
            en.shoot(start_time)
            
            if en.shotby(hero0) == True:
                score += 10
                
                boom_blit.append([time.time(),en.x,en.y])
                enemys.remove(en)
            
            if(en.to_bottom() == True):
                
                print("game over")
                print("score：",score)
                set.gameover(score)
                break
        
        for boom in boom_blit:
            if time.time() - boom[0] < 0.2:
                en.bScreen.screen.blit(en.boom_img,(boom[1],boom[2]))
            else:
                boom_blit.remove(boom)

        key_control(hero0,set)
        hero0.move()
        hero0.shoot()
        set.score_blit(score)
        pygame.display.update()

    
