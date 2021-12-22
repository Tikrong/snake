import pygame
from pygame import locals
import pygame.freetype
from constants import *
from helpers import *
import csv
import datetime


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
                    self.stateMachine.ChangeState(Game(self.screen, self.stateMachine))
                    return
                    # Start GameLOOP !!!
                elif event.key == locals.K_l:
                    self.stateMachine.ChangeState(Score(self.screen, self.stateMachine))
                    return
                    # Start Leaderboard
                elif event.key == locals.K_c:
                    self.stateMachine.ChangeState(Credits(self.screen, self.stateMachine))
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
                    self.stateMachine.ChangeState(MainMenu(self.screen, self.stateMachine))
            
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
                    self.stateMachine.ChangeState(GameOver(self.screen, self.stateMachine, self.score))
                    #if self.score > self.minHighestScore:
                        #self.stateMachine.states["leaderboard"].AddNewScore("VIKA", self.score)
                    return
                if event.key == locals.K_q:
                    self.stateMachine.ChangeState(MainMenu(self.screen, self.stateMachine))
                    #DrawQuitMenu(timeSinceLastMovement, score)
                

        # if player do nothing snake moves on its own
        if self.timeSinceLastMovement > self.MoveEveryMilliseconds:
            self.game.snake.MoveOnYourOwn()
            self.timeSinceLastMovement = 0
            if self.game.IsSnakeCollided():
                self.stateMachine.ChangeState(GameOver(self.screen, self.stateMachine, self.score))
                return

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

class Score():
    def __init__(self, screen, stateMachine):
        with open("scores.csv", "r", newline='') as file:
            scoresreader = csv.DictReader(file)
            self.scores = []
            for row in scoresreader:
                self.scores.append(row)
            self.maxNumOfRecords = 10
            self.screen = screen
            self.stateMachine = stateMachine



    def AddNewScore(self, name, score):
        # find at which position to add new score
        for x in range(self.maxNumOfRecords):
            try:
                if score > int(self.scores[x]["SCORE"]):
                    newRecord = {"PLACE": x, "NAME": name, "SCORE": str(score), 
                                "DATE": datetime.date.today().strftime("%d-%m-%y")}
                    self.scores.insert(x, newRecord)
                    break
            except IndexError:
                newRecord = {"PLACE": x, "NAME": name, "SCORE": str(score), 
                            "DATE": datetime.date.today().strftime("%d-%m-%y")}
                self.scores.insert(x, newRecord)
                break

        if len(self.scores) > self.maxNumOfRecords:
            self.scores.pop(-1)
        with open("scores.csv", "w", newline='') as file:
                        fieldnames = ["PLACE", "NAME", "SCORE", "DATE"]
                        writer = csv.DictWriter(file, fieldnames)
                        writer.writeheader()
                        for row in self.scores:
                            writer.writerow(row)

    def GetMinScore(self):
        # there are empty slots in table minimal score is 0
        if len(self.scores) < self.maxNumOfRecords:
            return 0
        else:
            return int(self.scores[self.maxNumOfRecords - 1]["SCORE"])

    def Start(self):
        self.screen.fill(BLACK)
        # Header
        rect = myfont.get_rect("LEADERBOARD")
        rect.left = (screen_width - rect.width) / 2
        rect.top = 10
        myfont.render_to(self.screen, rect, None, WHITE)

        # Render Score table
        # Render Headers
        # place
        rectPlace = pygame.Rect(20, 50, 20, 20)
        pygame.draw.rect(self.screen, RED, rectPlace)
        myfont.render_to(self.screen, rectPlace, "№", WHITE)

        # name
        rectName = pygame.Rect(rectPlace.right + 15, 50, 140, 20)
        pygame.draw.rect(self.screen, RED, rectName)
        myfont.render_to(self.screen, rectName, "NAME", WHITE)
        
        # date
        rectDate = pygame.Rect(0, 50, 120, 20)
        rectDate.right = screen_width - 20
        pygame.draw.rect(self.screen, RED, rectDate)
        myfont.render_to(self.screen, rectDate, "DATE", WHITE)
        
        # score
        rectScore = pygame.Rect(0, 50, 100, 20)
        rectScore.right = rectDate.left - 20
        pygame.draw.rect(self.screen, RED, rectScore)
        myfont.render_to(self.screen, rectScore, "SCORE", WHITE)

        pygame.draw.line(self.screen, WHITE, (20,rectScore.bottom+10), (screen_width-20, rectScore.bottom+10), 2)
            

        # Render Contents
        for n in range(len(self.scores)):
            # place
            rectPlace = pygame.Rect(20, n*42+100, 20, 20)
            pygame.draw.rect(self.screen, RED, rectPlace)
            myfont.render_to(self.screen, rectPlace, str(n+1), WHITE)

            # name
            rectName = pygame.Rect(rectPlace.right + 15, n*42+100, 140, 20)
            pygame.draw.rect(self.screen, RED, rectName)
            myfont.render_to(self.screen, rectName, self.scores[n]["NAME"], WHITE)
            
            # date
            rectDate = pygame.Rect(0, n*42+100, 120, 20)
            rectDate.right = screen_width - 20
            pygame.draw.rect(self.screen, RED, rectDate)
            myfont.render_to(self.screen, rectDate, self.scores[n]["DATE"], WHITE)
            
            # score
            rectScore = pygame.Rect(0, n*42+100, 100, 20)
            rectScore.right = rectDate.left - 20
            pygame.draw.rect(self.screen, RED, rectScore)
            myfont.render_to(self.screen, rectScore, self.scores[n]["SCORE"], WHITE)

            pygame.draw.line(self.screen, WHITE, (20,rectScore.bottom+10), (screen_width-20, rectScore.bottom+10), 2)
            
        pygame.display.flip()

    def Update(self):
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                self.stateMachine.Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == locals.K_m:
                    self.stateMachine.ChangeState(MainMenu(self.screen, self.stateMachine))


class GameOver():
    def __init__(self, screen, stateMachine, score):
        self.screen = screen
        self.stateMachine = stateMachine
        self.cursor = 0
        self.name = []
        self.maxLenOfName = 8
        self.rectForName = pygame.Rect(0,0,0,0)
        self.score = score

    def Start(self):
        # Draw borders
        rectBorder = pygame.Rect(0,0, 200, 100)
        rectBorder.left = (screen_width - rectBorder.width)/2
        rectBorder.top = (screen_height - rectBorder.height)/2
        pygame.draw.rect(self.screen, RED, rectBorder, width=3)
        

        # GameOver text
        rectGameOver = myfont.get_rect("GAME OVER")
        rectGameOver.left = (screen_width-rectGameOver.width) / 2
        rectGameOver.top = rectBorder.top + 5
        myfont.render_to(self.screen, rectGameOver, None, WHITE)

        # Place for name
        rectName = myfont.get_rect("ASDFGHJQ")
        print(rectName.width)
        rectName.left = (screen_width-rectName.width) / 2
        rectName.top = rectGameOver.top + 30

        rectUnderscore = myfont.get_rect("________")
        rectUnderscore.left = rectName.left
        rectUnderscore.top = rectName.bottom + 5
        myfont.render_to(self.screen, rectUnderscore, None, WHITE)
        
        self.rectForName = rectName



        #for n in range(self.maxLenOfName):


        pygame.display.flip()

    
    def Update(self):
        
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                self.stateMachine.Quit()
            if event.type == pygame.KEYDOWN:
                #if event.key == locals.K_m:
                    #self.stateMachine.ChangeState("mainMenu")
                if event.key == locals.K_BACKSPACE and self.cursor > 0:
                    self.DeleteLetter(self.cursor)
                    self.cursor -= 1
                    self.name.pop(-1)
                
                # when player press return and the name is typed add this name to the leaderboard
                elif event.key == locals.K_RETURN and len(self.name) > 0:
                    newState = Score(self.screen, self.stateMachine)
                    newState.AddNewScore("".join(self.name), self.score)
                    self.stateMachine.ChangeState(newState)
                    return

                # the ability to type name
                letter = event.unicode
                if letter.isalpha() and len(self.name) < self.maxLenOfName:
                    self.RenderLetter(letter.upper(), self.cursor)
                    self.name.append(letter.upper())
                    self.cursor += 1

    def RenderLetter(self, letter, cursor):
        rectLetter = myfont.get_rect(letter)
        rectLetter.left = self.rectForName.left + (rectLetter.width+2) * cursor
        rectLetter.top = self.rectForName.top
        pygame.draw.rect(self.screen, GREEN, rectLetter)
        myfont.render_to(self.screen, rectLetter, None, WHITE)
        pygame.display.flip()

    def DeleteLetter(self, cursor):
        rectLetter = myfont.get_rect(self.name[-1])
        rectLetter.left = self.rectForName.left + (rectLetter.width+2) * (cursor - 1)
        rectLetter.top = self.rectForName.top
        pygame.draw.rect(self.screen, BLACK, rectLetter)
        pygame.display.flip()


        
            
