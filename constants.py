import pygame
import pygame.freetype

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
myfont = pygame.freetype.Font("clacon2.ttf", 32)
myfont.antialiased = False
myfontSmall = pygame.freetype.Font("clacon2.ttf", 16)
myfontSmall.antialiased = False

for i in range(3):
    print(i)