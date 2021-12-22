# !!! DEPRECATED!!!

import pygame
from pygame import locals
import pygame.freetype
from constants import *
# module for handling score table
import csv
import datetime

class Score():
    def __init__(self, screen, stateMachine):
        with open("scores.csv", "r", newline='') as file:
            scoresreader = csv.DictReader(file)
            self.scores = []
            for row in scoresreader:
                self.scores.append(row)
            self.maxNumOfRecords = 10
            self.screen = screen
            self.stateMachine = stateMachine



    def AddNewScore(self, name, score):
        # find at which position to add new score
        for x in range(self.maxNumOfRecords):
            try:
                if score > int(self.scores[x]["SCORE"]):
                    newRecord = {"PLACE": x, "NAME": name, "SCORE": score, 
                                "DATE": datetime.date.today().strftime("%d-%m-%y")}
                    self.scores.insert(x, newRecord)
                    break
            except IndexError:
                newRecord = {"PLACE": x, "NAME": name, "SCORE": score, 
                            "DATE": datetime.date.today().strftime("%d-%m-%y")}
                self.scores.insert(x, newRecord)
                break

        if len(self.scores) > self.maxNumOfRecords:
            self.scores.pop(-1)
        with open("scores.csv", "w", newline='') as file:
                        fieldnames = ["PLACE", "NAME", "SCORE", "DATE"]
                        writer = csv.DictWriter(file, fieldnames)
                        writer.writeheader()
                        for row in self.scores:
                            writer.writerow(row)

    def GetMinScore(self):
        # there are empty slots in table minimal score is 0
        if len(self.scores) < self.maxNumOfRecords:
            return 0
        else:
            return int(self.scores[self.maxNumOfRecords - 1]["SCORE"])

    def Start(self):
        self.screen.fill(BLACK)
        # Header
        rect = myfont.get_rect("LEADERBOARD")
        rect.left = (screen_width - rect.width) / 2
        rect.top = 10
        myfont.render_to(self.screen, rect, None, WHITE)

        # Render Score table
        # Render Headers
        # place
        rectPlace = pygame.Rect(20, 50, 20, 20)
        pygame.draw.rect(self.screen, RED, rectPlace)
        myfont.render_to(self.screen, rectPlace, "№", WHITE)

        # name
        rectName = pygame.Rect(rectPlace.right + 15, 50, 140, 20)
        pygame.draw.rect(self.screen, RED, rectName)
        myfont.render_to(self.screen, rectName, "NAME", WHITE)
        
        # date
        rectDate = pygame.Rect(0, 50, 120, 20)
        rectDate.right = screen_width - 20
        pygame.draw.rect(self.screen, RED, rectDate)
        myfont.render_to(self.screen, rectDate, "DATE", WHITE)
        
        # score
        rectScore = pygame.Rect(0, 50, 100, 20)
        rectScore.right = rectDate.left - 20
        pygame.draw.rect(self.screen, RED, rectScore)
        myfont.render_to(self.screen, rectScore, "SCORE", WHITE)

        pygame.draw.line(self.screen, WHITE, (20,rectScore.bottom+10), (screen_width-20, rectScore.bottom+10), 2)
            

        # Render Contents
        for n in range(len(self.scores)):
            # place
            rectPlace = pygame.Rect(20, n*42+100, 20, 20)
            pygame.draw.rect(self.screen, RED, rectPlace)
            myfont.render_to(self.screen, rectPlace, str(n+1), WHITE)

            # name
            rectName = pygame.Rect(rectPlace.right + 15, n*42+100, 140, 20)
            pygame.draw.rect(self.screen, RED, rectName)
            myfont.render_to(self.screen, rectName, self.scores[n]["NAME"], WHITE)
            
            # date
            rectDate = pygame.Rect(0, n*42+100, 120, 20)
            rectDate.right = screen_width - 20
            pygame.draw.rect(self.screen, RED, rectDate)
            myfont.render_to(self.screen, rectDate, self.scores[n]["DATE"], WHITE)
            
            # score
            rectScore = pygame.Rect(0, n*42+100, 100, 20)
            rectScore.right = rectDate.left - 20
            pygame.draw.rect(self.screen, RED, rectScore)
            myfont.render_to(self.screen, rectScore, self.scores[n]["SCORE"], WHITE)

            pygame.draw.line(self.screen, WHITE, (20,rectScore.bottom+10), (screen_width-20, rectScore.bottom+10), 2)
            
        pygame.display.flip()

    def Update(self):
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                self.stateMachine.Quit()
            #if event.type == pygame.KEYDOWN:
                #if event.key == locals.K_m:
                    #self.stateMachine.ChangeState(MainMenu(self.screen, self.stateMachine))


        
            
