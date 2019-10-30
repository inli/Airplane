import pygame
import time
import sys

class setting(object):
    """description of class"""
    def __init__(self,bgScreen):
        WHITE = (255,255,255)
        self.chosen_color = (220,150,130)#橙色

        self.bScreen = bgScreen
        self.overimg = pygame.image.load('../img/over.png')
        self.overimg = pygame.transform.scale(self.overimg,(300,200))
        self.overimg.set_colorkey((0,0,0))#mask color = black
        
        pygame.init()
        self.font_agr = pygame.font.SysFont("Algerian",65)        
        self.text_pacific = self.font_agr.render("Pacific",True,WHITE,None)
        self.text_thunder = self.font_agr.render("Thunder",True,WHITE,None)
        
        self.font_no = pygame.font.SysFont(None,30)
        self.text_start = self.font_no.render("  Start Game",True,WHITE,None)
        self.text_quit = self.font_no.render("  Quit Game",True,WHITE,None)
        
        self.text_start_on = self.font_no.render(">> Start Game",True,self.chosen_color,None)
        self.text_quit_on = self.font_no.render(">> Quit Game",True,self.chosen_color,None)
        
        
        self.game_on = False
        

        
    def gameover(self,score):
        self.game_on = False
        y = self.bScreen.y
        x = self.bScreen.x
        while True:
            self.bScreen.screen.blit(self.bScreen.background,(0,0))
            self.bScreen.screen.blit(self.overimg,(0,y/5))
            self.bScreen.screen.blit(self.font_no.render("score:"+str(score),True,(255,255,255),None),(x/2-40,y/2))
            pygame.display.update()

    def gamestart(self):
        print('game start')
        self.game_on = True

    def gameload(self):
        
        startbutton = True
        while not self.game_on:
            self.bScreen.screen.blit(self.bScreen.background,(0,0))
            self.bScreen.screen.blit(self.text_pacific,(10,100))
            self.bScreen.screen.blit(self.text_thunder,(15,180))
        
            if startbutton == True:
                self.bScreen.screen.blit(self.text_start_on,(15,400))
                self.bScreen.screen.blit(self.text_quit,(15,450))
            else:
                self.bScreen.screen.blit(self.text_start,(15,400))
                self.bScreen.screen.blit(self.text_quit_on,(15,450))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        startbutton = False
                    elif event.key == pygame.K_UP:
                        startbutton = True
                    elif event.key == pygame.K_RETURN:
                        print('enter')
                        if startbutton == True:
                            self.gamestart()
                            break
                        else:
                            sys.exit()
            pygame.display.update()

    def score_blit(self,score):
        self.bScreen.screen.blit(self.font_no.render("score:"+str(score),True,(255,255,255),None),(0,0))
    def gamePause(self):
        y = self.bScreen.y
        x = self.bScreen.x
        while(True): 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        return


       

       

        

