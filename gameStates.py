import pygame
from pygame import locals
import pygame.freetype
from constants import *
from helpers import *


class MainMenu():
    def __init__(self, screen, stateMachine):
        self.screen = screen
        self.stateMachine = stateMachine
    
    def Update(self):
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                self.stateMachine.Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == locals.K_q:
                    self.stateMachine.Quit()
                    return
                elif event.key == locals.K_p:
                    self.stateMachine.ChangeState("gameLoop")
                    return
                    # Start GameLOOP !!!
                elif event.key == locals.K_l:
                    self.stateMachine.ChangeState("leaderboard")
                    return
                    # Start Leaderboard
                elif event.key == locals.K_c:
                    self.stateMachine.ChangeState("credits")
                    return
                    # Start credits
            
        self.screen.fill(BLACK)
        # game logo
        rect = myfont.get_rect("SNAKE")
        rect.left = (screen_width - rect.width) / 2
        rect.top = 10
        myfont.render_to(self.screen, rect, None, WHITE)

        # render menu options
        rectPlay = myfont.get_rect("(P)lay")
        rectPlay.left = (screen_width - rectPlay.width) / 2
        rectPlay.top = 200
        myfont.render_to(self.screen, rectPlay, None, WHITE)

        rectLeaderboard = myfont.get_rect("(L)eaderboard")
        rectLeaderboard.left = (screen_width - rectLeaderboard.width) / 2
        rectLeaderboard.top = rectPlay.bottom + 10
        myfont.render_to(self.screen, rectLeaderboard, None, WHITE)

        rectCredits = myfont.get_rect("(C)redits")
        rectCredits.left = (screen_width - rectCredits.width) / 2
        rectCredits.top = rectLeaderboard.bottom + 10
        myfont.render_to(self.screen, rectCredits, None, WHITE)

        rectQuit = myfont.get_rect("(Q)uit")
        rectQuit.left = (screen_width - rectQuit.width) / 2
        rectQuit.top = rectCredits.bottom + 10
        myfont.render_to(self.screen, rectQuit, None, WHITE)

        pygame.display.flip()

class Credits():
    def __init__(self, screen, stateMachine):
        self.screen = screen
        self.stateMachine = stateMachine

    def Update(self):
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                self.stateMachine.Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == locals.K_m:
                    self.stateMachine.ChangeState("mainMenu")
            
        self.screen.fill(BLACK)
        # game logo
        rect = myfont.get_rect("CREDITS")
        rect.left = (screen_width - rect.width) / 2
        rect.top = 10
        myfont.render_to(self.screen, rect, None, WHITE)
        pygame.display.flip()


class Game():
    def __init__(self, screen, stateMachine):
        self.screen = screen
        self.stateMachine = stateMachine
        self.score = 0
        self.minHighestScore = 0
        self.snake = Snake(3, (3,3))
        self.game = GameField(25,25, self.snake)
        self.game.DrawField()
        # we track how much time passed since last movements and if snake didn't moved we move it
        self.timeSinceLastMovement = 0
        self.MoveEveryMilliseconds = 200
        self.clock = pygame.time.Clock()

    def Start(self):
        self.minHighestScore = self.stateMachine.states["leaderboard"].GetMinScore()

    
    def Update(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stateMachine.Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == locals.K_LEFT:
                    self.game.snake.MoveLeft()
                    self.timeSinceLastMovement = 0
                elif event.key == locals.K_RIGHT:
                    self.game.snake.MoveRight()
                    self.timeSinceLastMovement = 0
                elif event.key == locals.K_UP:
                    self.game.snake.MoveUp()
                    self.timeSinceLastMovement = 0
                elif event.key == locals.K_DOWN:
                    self.game.snake.MoveDown()
                    self.timeSinceLastMovement = 0
                if self.game.IsSnakeCollided():
                    self.stateMachine.ChangeState("gameOver")
                if event.key == locals.K_q:
                    self.stateMachine.ChangeState("mainMenu")
                    #DrawQuitMenu(timeSinceLastMovement, score)
                

        # if player do nothing snake moves on its own
        if self.timeSinceLastMovement > self.MoveEveryMilliseconds:
            self.game.snake.MoveOnYourOwn()
            self.timeSinceLastMovement = 0
            if self.game.IsSnakeCollided():

                if self.score > self.minHighestScore:
                    self.stateMachine.states["leaderboard"].AddNewScore("VIKA", self.score) 

                self.stateMachine.ChangeState("gameOver")

        if self.game.DidSnakeGetFood():
            self.score += 1

        # draw gamefield grid, walls, snake
        for i in range(self.game.height):
            for j in range(self.game.width):
                # if cell is empty draw square with white borders
                rect = pygame.Rect(j*tile_size, i*tile_size + gameMenuHeight, tile_size, tile_size)
                if self.game.field[i][j] == 0:
                    pygame.draw.rect(self.screen, BLACK, rect, 0)
                    #pygame.draw.rect(screen, WHITE, rect, 1)
                elif self.game.field[i][j] == 1:
                    pygame.draw.rect(self.screen, GREEN, rect, 0)
                elif self.game.field[i][j] == 2:
                    pygame.draw.rect(self.screen, RED, rect, 0)
                elif self.game.field[i][j] == 3:
                    pygame.draw.rect(self.screen, YELLOW, rect, 0)

        
        # Draw GameMenu
        scoreRect = pygame.Rect(10, 10, 80, 0)
        myfont.render_to(self.screen, scoreRect, "SCORE", WHITE)
        scoreValueRect = pygame.Rect(scoreRect.right + 10, 10, 30, 30)
        myfont.render_to(self.screen, scoreValueRect, str(self.score), WHITE, BLACK)
        quitRect = pygame.Rect(screen_width - 100, 10, 80, 0)
        myfont.render_to(self.screen, quitRect, "(Q)uit", WHITE)


        self.game.DrawField()
            
        
        pygame.display.flip()
        self.timeSinceLastMovement += self.clock.tick(60)

class GameOver():
    def __init__(self, screen, stateMachine):
        self.screen = screen
        self.stateMachine = stateMachine
    
    def Update(self):
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                self.stateMachine.Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == locals.K_m:
                    self.stateMachine.ChangeState("mainMenu")
            
        self.screen.fill(BLACK)
        # game logo
        rect = myfont.get_rect("GAME OVER")
        rect.left = (screen_width - rect.width) / 2
        rect.top = 10
        myfont.render_to(self.screen, rect, None, RED)
        pygame.display.flip()