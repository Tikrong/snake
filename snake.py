import pygame
from pygame import locals
from helpers import*

pygame.init()

clock = pygame.time.Clock()

# we track how much time passed since last movements and if snake didn't moved we move it
timeSinceLastMovement = 0
MoveEveryMilliseconds = 1000

#screen size
screen_height = 500
screen_width = 500

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)

# sizes
tile_size = 20

screen = pygame.display.set_mode((screen_width, screen_height))

snake = Snake(3, (3,3))
game = GameField(15,15,snake)
game.DrawField()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == locals.K_LEFT:
                game.snake.MoveLeft()
                print("left")
                #game.DrawField()
                timeSinceLastMovement = 0
            elif event.key == locals.K_RIGHT:
                game.snake.MoveRight()
                print("right")
                #game.DrawField()
                timeSinceLastMovement = 0
            elif event.key == locals.K_UP:
                game.snake.MoveUp()
                print("up")
                #game.DrawField()
                timeSinceLastMovement = 0
            elif event.key == locals.K_DOWN:
                game.snake.MoveDown()
                print("down")
                #game.DrawField()
                timeSinceLastMovement = 0
    
    if timeSinceLastMovement > MoveEveryMilliseconds:
        game.snake.MoveOnYourOwn()
        #game.DrawField()
        timeSinceLastMovement = 0

    game.DidSnakeGetFood()
    game.DrawField()

    # draw gamefield grid, walls, snake
    for i in range(game.height):
        for j in range(game.width):
            # if cell is empty draw square with white borders
            if game.field[i][j] == 0:
                rect = pygame.Rect(j*tile_size, i*tile_size, tile_size, tile_size)
                pygame.draw.rect(screen, BLACK, rect, 0)
                pygame.draw.rect(screen, WHITE, rect, 1)
            elif game.field[i][j] == 1:
                rect = pygame.Rect(j*tile_size, i*tile_size, tile_size, tile_size)
                pygame.draw.rect(screen, GREEN, rect, 0)
            elif game.field[i][j] == 2:
                rect = pygame.Rect(j*tile_size, i*tile_size, tile_size, tile_size)
                pygame.draw.rect(screen, RED, rect, 0)
            elif game.field[i][j] == 3:
                rect = pygame.Rect(j*tile_size, i*tile_size, tile_size, tile_size)
                pygame.draw.rect(screen, YELLOW, rect, 0)

    if game.IsSnakeCollided():
        print("GAME OVER")
    
    
        
   
    pygame.display.flip()
    timeSinceLastMovement += clock.tick(30)



print("I am the winner")