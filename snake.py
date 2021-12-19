import pygame
from pygame import locals
import pygame.freetype
from pygame.constants import QUIT
from helpers import*

# It must be improved
def RednerGameOver():    
    rect = pygame.Rect(0,0, screen_width, screen_height)
    pygame.draw.rect(screen, BLACK, rect)
    myfont.render_to(screen, rect, "GAME OVER", RED)
    pygame.display.flip()
    

def RenderMainMenu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == locals.K_q:
                    running = False
                if event.key == locals.K_p:
                    running = False
                    # Start GameLOOP !!!
                if event.key == locals.K_l:
                    running = False
                    # Start Leaderboard
                if event.key == locals.K_c:
                    running = False
                    # Start credits
    
        screen.fill(BLACK)

        # game logo
        rect = myfont.get_rect("SNAKE")
        rect.left = (screen_width - rect.width) / 2
        rect.top = 10
        myfont.render_to(screen, rect, None, WHITE)

        # render menu options
        rectPlay = myfont.get_rect("(P)lay")
        rectPlay.left = (screen_width - rectPlay.width) / 2
        rectPlay.top = 200
        myfont.render_to(screen, rectPlay, None, WHITE)

        rectLeaderboard = myfont.get_rect("(L)eaderboard")
        rectLeaderboard.left = (screen_width - rectLeaderboard.width) / 2
        rectLeaderboard.top = rectPlay.bottom + 10
        myfont.render_to(screen, rectLeaderboard, None, WHITE)

        rectCredits = myfont.get_rect("(C)redits")
        rectCredits.left = (screen_width - rectCredits.width) / 2
        rectCredits.top = rectLeaderboard.bottom + 10
        myfont.render_to(screen, rectCredits, None, WHITE)

        rectQuit = myfont.get_rect("(Q)uit")
        rectQuit.left = (screen_width - rectQuit.width) / 2
        rectQuit.top = rectCredits.bottom + 10
        myfont.render_to(screen, rectQuit, None, WHITE)

        pygame.display.flip()



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
                    RenderMainMenu()
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
                if game.IsSnakeCollided():
                    RednerGameOver()
        
        if timeSinceLastMovement > MoveEveryMilliseconds:
            game.snake.MoveOnYourOwn()
            #game.DrawField()
            timeSinceLastMovement = 0
            if game.IsSnakeCollided():
                RednerGameOver()
                running = False

        if game.DidSnakeGetFood():
            score += 1
        

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


        game.DrawField()
            
        
        pygame.display.flip()
        timeSinceLastMovement += clock.tick(60)

GameLoop(timeSinceLastMovement, score)