import pygame
from pygame import locals
from helpers import*

pygame.init()

clock = pygame.time.Clock()

# we track how much time passed since last movements and if snake didn't moved we move it
timeSinceLastMovement = 0
MoveEveryMilliseconds = 200

#screen size
screen_height = 600
screen_width = 500

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)

# sizes
tile_size = 20
gameMenuHeight = 100

# fonts
myfont = pygame.freetype.Font("clacon2.ttf", 32)

screen = pygame.display.set_mode((screen_width, screen_height))

# Game data and logic
score = 0

snake = Snake(3, (3,3))
game = GameField(25,25,snake)
game.DrawField()

def DrawQuitMenu(timeSinceLastMovement, score):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == locals.K_y:
                    running = False
                elif event.key == locals.K_n:
                    running = False
                    GameLoop(timeSinceLastMovement, score)

        rect = pygame.Rect(50, 200, 400, 200)
        rectPromtText = pygame.Rect(rect.left + 10, rect.top + 10, 280, 90)
        rectYes = pygame.Rect(rectPromtText.left, rectPromtText.bottom, 100, 100)
        rectNo = pygame.Rect(rectPromtText.right-100, rectPromtText.bottom, 100, 100)
        pygame.draw.rect(screen, BLACK, rect)
        pygame.draw.rect(screen, WHITE, rect, 1)
        myfont.render_to(screen, rectPromtText, "Do you want to quit?", WHITE)
        myfont.render_to(screen, rectYes, "(Y)es", WHITE)
        myfont.render_to(screen, rectNo, "(N)o", WHITE)
        pygame.display.flip()

def GameLoop(timeSinceLastMovement, score):
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
                elif event.key == locals.K_q:
                    DrawQuitMenu(timeSinceLastMovement, score)
                    running = False
        
        if timeSinceLastMovement > MoveEveryMilliseconds:
            game.snake.MoveOnYourOwn()
            #game.DrawField()
            timeSinceLastMovement = 0

        if game.DidSnakeGetFood():
            score += 1
        game.DrawField()

        # draw gamefield grid, walls, snake
        for i in range(game.height):
            for j in range(game.width):
                # if cell is empty draw square with white borders
                rect = pygame.Rect(j*tile_size, i*tile_size + gameMenuHeight, tile_size, tile_size)
                if game.field[i][j] == 0:
                    pygame.draw.rect(screen, BLACK, rect, 0)
                    #pygame.draw.rect(screen, WHITE, rect, 1)
                elif game.field[i][j] == 1:
                    pygame.draw.rect(screen, GREEN, rect, 0)
                elif game.field[i][j] == 2:
                    pygame.draw.rect(screen, RED, rect, 0)
                elif game.field[i][j] == 3:
                    pygame.draw.rect(screen, YELLOW, rect, 0)

        # Draw GameMenu
        scoreRect = pygame.Rect(10, 10, 80, 0)
        myfont.render_to(screen, scoreRect, "SCORE", WHITE)
        scoreValueRect = pygame.Rect(scoreRect.right + 10, 10, 30, 30)
        myfont.render_to(screen, scoreValueRect, str(score), WHITE, BLACK)
        quitRect = pygame.Rect(screen_width - 100, 10, 80, 0)
        myfont.render_to(screen, quitRect, "(Q)uit", WHITE)


        if game.IsSnakeCollided():
            print("GAME OVER")
        
        pygame.display.flip()
        timeSinceLastMovement += clock.tick(60)

GameLoop(timeSinceLastMovement, score)