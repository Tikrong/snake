import pygame
from pygame import locals
import pygame.freetype
from gameStates import *
from constants import *
from score import *
from gameover import *


pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

class StateMachine():
    def __init__(self):
        self.states = {"mainMenu": MainMenu(screen, self),
                        "credits": Credits(screen, self),
                        "leaderboard": Score(screen, self),
                        "gameLoop": Game(screen, self),
                        "gameOver": GameOver(screen, self, 3)}
        self.currentState = MainMenu(screen, self)
        self.running = True

    def Start(self):
        try:
            self.currentState.Start()
        except AttributeError:
            pass

    def Update(self):
        self.currentState.Update()

    def ChangeState(self, State):
        self.ReloadStates()
        self.currentState = State
        self.Start()
        print("changing state")

    def Quit(self):
        self.running = False

    def ReloadStates(self):
        self.states = {"mainMenu": MainMenu(screen, self),
                        "credits": Credits(screen, self),
                        "leaderboard": Score(screen, self),
                        "gameLoop": Game(screen, self),
                        "gameOver": GameOver(screen, self, 3)}

stateMachine = StateMachine()

stateMachine.Start()
while stateMachine.running:
    stateMachine.Update()
    
