import  pygame
from helpers import*

pygame.init()

#screen size
screen_height = 600
screen_width = 450

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)

# sizes
tile_size = 50

screen = pygame.display.set_mode((screen_width, screen_height))

game = GameField()
snake = Snake(3, (3,3))
game.DrawField(snake)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # drow gamefield
    for i in range(game.height):
        for j in range(game.width):
            if game.field[i][j] == 1:
                rect = pygame.Rect(j*tile_size, i*tile_size, tile_size, tile_size)
                pygame.draw.rect(screen, WHITE, rect, 1)


    pygame.display.flip()



print("I am the winner")