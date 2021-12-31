import pygame
import pygame.freetype
import os

pygame.init()

#screen size
screen_height = 600
screen_width = 500

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,125,0)
RED = (125,0,0)
YELLOW = (255,255,0)
ORANGE = (180,100,0)

# sizes
tile_size = 20
gameMenuHeight = 40

# fonts
myfont = pygame.freetype.Font(os.path.join("fonts", "clacon2.ttf"), 32)
myfont.antialiased = False
myfontSmall = pygame.freetype.Font(os.path.join("fonts", "clacon2.ttf"), 16)
myfontSmall.antialiased = False

# sounds
movementSound = pygame.mixer.Sound(os.path.join("sounds", "movement.wav"))
gotFoodSound = pygame.mixer.Sound(os.path.join("sounds", "food.wav"))
collisionSound = pygame.mixer.Sound(os.path.join("sounds", "collision.wav"))
tornOnSound = pygame.mixer.Sound(os.path.join("sounds", "turnon.wav"))
menuChoiceSound = pygame.mixer.Sound(os.path.join("sounds", "menu.wav"))
mainMenuSound = pygame.mixer.Sound(os.path.join("sounds", "mainmenu.wav"))
typeSound = pygame.mixer.Sound(os.path.join("sounds", "type.wav"))
deleteSound = pygame.mixer.Sound(os.path.join("sounds", "delete.wav"))
victorySound = pygame.mixer.Sound(os.path.join("sounds", "victory.wav"))

ant = 300
def IncreaseDifficulty(tmp):
        # 15 point
        if tmp > 200:
            tmp -= 20
        # 45 points
        elif tmp > 100:
            tmp -= 7
        # 75 points
        elif tmp > 50:
            tmp -= 4
        # 102 points
        elif tmp > 25:
            tmp - 2
        return tmp

