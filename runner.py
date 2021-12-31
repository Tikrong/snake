import pygame
from pygame import locals
import pygame.freetype
from gameStates import *
from constants import *


pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

class StateMachine():
    def __init__(self):
        self.currentState = MainMenu(screen, self)
        self.running = True
        tornOnSound.play()

    def Start(self):
        try:
            self.currentState.Start()
        except AttributeError:
            pass

    def Update(self):
        self.currentState.Update()

    def ChangeState(self, State):
        self.currentState = State
        self.Start()

    def Quit(self):
        self.running = False

stateMachine = StateMachine()

stateMachine.Start()
while stateMachine.running:
    stateMachine.Update()
    
