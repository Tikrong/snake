# !!! DEPRECATED !!!
# Here we will  realize adding new name to the leaderboard

import pygame
from pygame import locals
import pygame.freetype
from constants import *
from helpers import *

class GameOver():
    def __init__(self, screen, stateMachine, score):
        self.screen = screen
        self.stateMachine = stateMachine
        self.cursor = 0
        self.name = []
        self.maxLenOfName = 8
        self.rectForName = pygame.Rect(0,0,0,0)
        self.score = score

    def Start(self):
        # Draw borders
        rectBorder = pygame.Rect(0,0, 200, 100)
        rectBorder.left = (screen_width - rectBorder.width)/2
        rectBorder.top = (screen_height - rectBorder.height)/2
        pygame.draw.rect(self.screen, RED, rectBorder, width=3)
        

        # GameOver text
        rectGameOver = myfont.get_rect("GAME OVER")
        rectGameOver.left = (screen_width-rectGameOver.width) / 2
        rectGameOver.top = rectBorder.top + 5
        myfont.render_to(self.screen, rectGameOver, None, WHITE)

        # Place for name
        rectName = myfont.get_rect("ASDFGHJQ")
        print(rectName.width)
        rectName.left = (screen_width-rectName.width) / 2
        rectName.top = rectGameOver.top + 30

        rectUnderscore = myfont.get_rect("________")
        rectUnderscore.left = rectName.left
        rectUnderscore.top = rectName.bottom + 5
        myfont.render_to(self.screen, rectUnderscore, None, WHITE)
        
        self.rectForName = rectName



        #for n in range(self.maxLenOfName):


        pygame.display.flip()

    
    def Update(self):
        
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                self.stateMachine.Quit()
            if event.type == pygame.KEYDOWN:
                #if event.key == locals.K_m:
                    #self.stateMachine.ChangeState("mainMenu")
                if event.key == locals.K_BACKSPACE and self.cursor > 0:
                    self.DeleteLetter(self.cursor)
                    self.cursor -= 1
                    self.name.pop(-1)
                
                # when player press return and the name is typed add this name to the leaderboard
                elif event.key == locals.K_RETURN and len(self.name) > 0:
                    self.stateMachine.states["leaderboard"].AddNewScore("".join(self.name), self.score)

                # the ability to type name
                letter = event.unicode
                if letter.isalpha() and len(self.name) < self.maxLenOfName:
                    self.RenderLetter(letter.upper(), self.cursor)
                    self.name.append(letter.upper())
                    self.cursor += 1

    def RenderLetter(self, letter, cursor):
        rectLetter = myfont.get_rect(letter)
        rectLetter.left = self.rectForName.left + (rectLetter.width+2) * cursor
        rectLetter.top = self.rectForName.top
        pygame.draw.rect(self.screen, GREEN, rectLetter)
        myfont.render_to(self.screen, rectLetter, None, WHITE)
        pygame.display.flip()

    def DeleteLetter(self, cursor):
        rectLetter = myfont.get_rect(self.name[-1])
        rectLetter.left = self.rectForName.left + (rectLetter.width+2) * (cursor - 1)
        rectLetter.top = self.rectForName.top
        pygame.draw.rect(self.screen, BLACK, rectLetter)
        pygame.display.flip()
        

                
        
        
        
        
        """     
        self.screen.fill(BLACK)
        # game logo
        rect = myfont.get_rect("GAME OVER")
        rect.left = (screen_width - rect.width) / 2
        rect.top = 10
        myfont.render_to(self.screen, rect, None, RED)
        pygame.display.flip()
        """
