import pygame
from pygame import locals
import pygame.freetype
from gameStates import *
from constants import *


pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

class StateMachine():
    def __init__(self):
        self.states = {"mainMenu": MainMenu(screen, self),
                        "credits": Credits(screen, self),
                        "leaderboard": LeaderBoard(screen, self),
                        "gameLoop": Game(screen, self),
                        "gameOver": GameOver(screen, self)}
        self.currentState = self.states["mainMenu"]
        self.running = True


    def Update(self):
        self.currentState.Update()

    def ChangeState(self, state):
        self.ReloadStates()
        self.currentState = self.states[state]
        print("changing state")

    def Quit(self):
        self.running = False

    def ReloadStates(self):
        self.states = {"mainMenu": MainMenu(screen, self),
                        "credits": Credits(screen, self),
                        "leaderboard": LeaderBoard(screen, self),
                        "gameLoop": Game(screen, self),
                        "gameOver": GameOver(screen, self)}

stateMachine = StateMachine()

while stateMachine.running:
    stateMachine.Update()
    
