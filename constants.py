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

# sounds
movementSound = pygame.mixer.Sound("sounds\movement.wav")
gotFoodSound = pygame.mixer.Sound("sounds\\food.wav")
collisionSound = pygame.mixer.Sound("sounds\\collision.wav")
tornOnSound = pygame.mixer.Sound("sounds\\turnon.wav")
menuChoiceSound = pygame.mixer.Sound("sounds\\menu.wav")
mainMenuSound = pygame.mixer.Sound("sounds\\mainmenu.wav")
typeSound = pygame.mixer.Sound("sounds\\type.wav")
deleteSound = pygame.mixer.Sound("sounds\\delete.wav")
victorySound = pygame.mixer.Sound("sounds\\victory.wav")

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

for i in range(34):
    ant = IncreaseDifficulty(ant)
    print(i*3, ant)

