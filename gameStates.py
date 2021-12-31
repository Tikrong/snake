import pygame
from pygame import locals
import pygame.freetype
from constants import *
from helpers import *
import csv
import datetime
import time


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
                    menuChoiceSound.play()
                    return
                    # Start Leaderboard
                elif event.key == locals.K_c:
                    self.stateMachine.ChangeState(Credits(self.screen, self.stateMachine))
                    return
                    # Start credits
            
    def Start(self):
        self.screen.fill(BLACK)
        # game logo
        rect = myfont.get_rect("SNAKE")
        rect.left = (screen_width - rect.width) / 2
        rect.top = 10
        myfont.render_to(self.screen, rect, None, WHITE)

        # render menu options
        rectPlay = myfont.get_rect("(P)lay")
        rectPlay.left = (screen_width - rectPlay.width) / 2
        rectPlay.top = 130
        myfont.render_to(self.screen, rectPlay, None, WHITE)

        rectLeaderboard = myfont.get_rect("(L)eaderboard")
        rectLeaderboard.left = (screen_width - rectLeaderboard.width) / 2
        rectLeaderboard.top = rectPlay.bottom + 10
        myfont.render_to(self.screen, rectLeaderboard, None, WHITE)

        rectCredits = myfont.get_rect("(C)redits")
        rectCredits.left = (screen_width - rectCredits.width) / 2
        rectCredits.top = rectLeaderboard.bottom + 15
        myfont.render_to(self.screen, rectCredits, None, WHITE)
        
        rectQuit = myfont.get_rect("(Q)uit")
        rectQuit.left = (screen_width - rectQuit.width) / 2
        rectQuit.top = rectCredits.bottom + 15
        myfont.render_to(self.screen, rectQuit, None, WHITE)

        # render hint 
        rectHelp = myfontSmall.get_rect("Press 'P' to start the game")
        rectHelp.left = (screen_width - rectHelp.width) / 2
        rectHelp.bottom = screen_height - 5
        myfontSmall.render_to(self.screen, rectHelp, None, WHITE)


        # render logo
        try:
            logo = pygame.image.load("snake_logo.png")
            logo.convert_alpha()
            logo = pygame.transform.scale(logo, (150,150))
            rectLogo = pygame.Rect((screen_width-logo.get_width())/2, rectQuit.bottom + 100, 0,0)
            self.screen.blit(logo, rectLogo)
        except FileNotFoundError:
            print("Snake logo isn't found")

        pygame.display.flip()

class Credits():
    def __init__(self, screen, stateMachine):
        self.screen = screen
        self.stateMachine = stateMachine
        menuChoiceSound.play()

    def Update(self):
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                self.stateMachine.Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == locals.K_m:
                    self.stateMachine.ChangeState(MainMenu(self.screen, self.stateMachine))
                    mainMenuSound.play()

    def Start(self):
        
            
        self.screen.fill(BLACK)
        # game logo
        rect = myfont.get_rect("CREDITS")
        rect.left = (screen_width - rect.width) / 2
        rect.top = 10
        myfont.render_to(self.screen, rect, None, WHITE)
        pygame.draw.line(self.screen,  WHITE, (rect.left, rect.bottom+5), (rect.right, rect.bottom+5), 2)

        # render hint 
        rectHelp = myfontSmall.get_rect("Press 'M' to go to the Main Menu")
        rectHelp.left = (screen_width - rectHelp.width) / 2
        rectHelp.bottom = screen_height - 5
        myfontSmall.render_to(self.screen, rectHelp, None, WHITE)

        # render text
        text = ["THIS GAME WAS CREATED TO PRACTICE PYTHON AND JUST FOR FUN",
                "IT IS AVAILABALE FOR DOWNLOAD AT MY GITHUB:",
                "github.com/Tikrong/snake",
                "line",
                "USED RESOURCES:",
                "* SNAKE IMAGE *",
                "pixelartmaker.com/art/12b7d2d3028378e",
                "* SKULL IMAGE *", 
                "pixilart.com/art/just-a-skull-and-bones-afd73ef8e6a0ecd",
                "* SOUNDS *",
                "opengameart.org"]
        
        i = 0
        for line in text:
            # draw line
            if line == "line":
                rect = myfontSmall.get_rect("ABC")
                rect.left = 20
                rect.top = (rect.height+10)*i + 50
                pygame.draw.line(self.screen, WHITE, (rect.left, rect.top + rect.height/2), (rect.left+100, rect.top + rect.height/2))
                i += 1
                pygame.display.flip()
            else:
                rect = myfontSmall.get_rect(line.upper())
                rect.left = 20
                rect.top = (rect.height+10)*i + 50
                myfontSmall.render_to(self.screen, rect, None, WHITE)
                i += 1
                pygame.display.flip()


        #self.RenderText()

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
        self.MoveEveryMilliseconds = 300
        self.clock = pygame.time.Clock()

    def Start(self):
        pass

    def IncreaseDifficulty(self):
        # 15 point
        if self.MoveEveryMilliseconds > 200:
            self.MoveEveryMilliseconds -= 20
        # 45 points
        elif self.MoveEveryMilliseconds > 100:
            self.MoveEveryMilliseconds -= 7
        # 75 points
        elif self.MoveEveryMilliseconds > 50:
            self.MoveEveryMilliseconds -= 4
        # 102 points
        elif self.MoveEveryMilliseconds > 25:
            self.MoveEveryMilliseconds - 2
    
    # this function draws the collision of the snake
    def DrawCollision(self):
        # we paint the neck of the snake because the head is already on the obstacle, but we didn't render it yet
        # because we move the snake, then check for collisions and onlyt then render
        y, x = self.snake.cells[-2]
        rect = pygame.Rect(x*tile_size, y*tile_size + gameMenuHeight, tile_size, tile_size)
        pygame.draw.rect(self.screen, ORANGE, rect, 0)
        pygame.display.flip()
        time.sleep(1)
        return

    
    def Update(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stateMachine.Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == locals.K_LEFT:
                    if self.game.snake.MoveLeft():
                        self.timeSinceLastMovement = 0
                        movementSound.play()
                elif event.key == locals.K_RIGHT:
                    if self.game.snake.MoveRight():
                        self.timeSinceLastMovement = 0
                        movementSound.play()
                elif event.key == locals.K_UP:
                    if self.game.snake.MoveUp():
                        self.timeSinceLastMovement = 0
                        movementSound.play()
                elif event.key == locals.K_DOWN:
                    if self.game.snake.MoveDown():
                        self.timeSinceLastMovement = 0
                        movementSound.play()
                if self.game.IsSnakeCollided():
                    collisionSound.play()
                    self.DrawCollision()
                    self.stateMachine.ChangeState(GameOver(self.screen, self.stateMachine, self.score))
                    return
                if event.key == locals.K_q:
                    # when player quits and has enough points for leaderboard position we put him there
                    minHighestScore = Score(self.screen, self.stateMachine).GetMinScore()
                    if self.score > minHighestScore:
                        self.stateMachine.ChangeState(GameOver(self.screen, self.stateMachine, self.score))
                        return
                    else:
                        self.stateMachine.ChangeState(MainMenu(self.screen, self.stateMachine))
                        mainMenuSound.play()
                        return

                if self.game.DidSnakeGetFood():
                    self.score += 1
                    gotFoodSound.play()
                    # increase difficulty every 3 points
                    if self.score % 3 == 0:
                        self.IncreaseDifficulty()

                self.DrawGameField()
                

        # if player do nothing snake moves on its own
        if self.timeSinceLastMovement > self.MoveEveryMilliseconds:
            self.game.snake.MoveOnYourOwn()
            
            self.timeSinceLastMovement = 0
            if self.game.IsSnakeCollided():
                collisionSound.play()
                self.DrawCollision()
                self.stateMachine.ChangeState(GameOver(self.screen, self.stateMachine, self.score))
                return
            if self.game.DidSnakeGetFood():
                self.score += 1
                gotFoodSound.play()
                # increase difficulty every 3 points
                if self.score % 3 == 0:    
                    self.IncreaseDifficulty()

            movementSound.play()
            self.DrawGameField()

        self.timeSinceLastMovement += self.clock.tick(120)

    def Start(self):
        self.DrawGameField()

    def DrawGameField(self):
        self.game.DrawField()
        # draw gamefield grid, walls, snake
        self.screen.fill(BLACK)

        for i in range(self.game.height):
            for j in range(self.game.width):
                # if cell is empty draw black square
                rect = pygame.Rect(j*tile_size, i*tile_size + gameMenuHeight, tile_size, tile_size)
                if self.game.field[i][j] == 0:
                    pygame.draw.rect(self.screen, BLACK, rect, 0)
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

        

        #  Draw hint
        rectHint = myfontSmall.get_rect("USE ARROW KEYS TO CONTROL THE SNAKE")
        rectHint.left = (screen_width - rectHint.width) / 2
        rectHint.bottom = screen_height - 23
        myfontSmall.render_to(self.screen, rectHint, None, WHITE)
            
        pygame.display.flip()


class Score():
    def __init__(self, screen, stateMachine):
        self.maxNumOfRecords = 10
        try:
            self.scores = self.OpenScoreTable(self.maxNumOfRecords)
        except FileNotFoundError:
            self.RebuildScoresTable()
            self.scores = self.OpenScoreTable(self.maxNumOfRecords)
        self.screen = screen
        self.stateMachine = stateMachine

    def OpenScoreTable(self, maxNumOfRecords):
        with open("scores.csv", "r", newline='') as file:
            scoresreader = csv.DictReader(file)
            scores = []
            for row in scoresreader:
                scores.append(row)
            # make sure that there are only 10 rows showing in score table
            scores = scores[:maxNumOfRecords]
            
            #  check that the score file isn't corrupt
            #  check that headers are correct
            correctHeaders = ['PLACE', 'NAME', 'SCORE', 'DATE']
            for header, headerBackup in zip(scoresreader.fieldnames, correctHeaders):
                if header != headerBackup:
                    self.RebuildScoresTable()
                    scores = self.OpenScoreTable(maxNumOfRecords)
                    break
            
            # check that scores  contain ingegers
            for row in scores:
                try:
                    int(row["SCORE"])
                except ValueError:
                    self.RebuildScoresTable()
                    scores = self.OpenScoreTable(maxNumOfRecords)
                    break

            return scores

    def RebuildScoresTable(self):
        with open("scores.csv", "w", newline='') as file:
            fieldnames = ["PLACE", "NAME", "SCORE", "DATE"]
            writer = csv.DictWriter(file, fieldnames)
            writer.writeheader()
            row = {"PLACE": 1, "NAME": "PYTHON", "SCORE": "100", 
                            "DATE": "23-12-21"}
            writer.writerow(row)


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
        
        # make sure that there are only 10 records in the table
        self.scores = self.scores[:self.maxNumOfRecords]

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
        pygame.draw.line(self.screen, WHITE, (rect.left, rect.bottom+5), (rect.right, rect.bottom+5), 2)


        # Render Score table
        # Render Headers
        # place
        rectPlace = pygame.Rect(20, 70, 20, 20)
        myfont.render_to(self.screen, rectPlace, "№", WHITE)

        # name
        rectName = pygame.Rect(rectPlace.right + 15, 70, 140, 20)
        myfont.render_to(self.screen, rectName, "NAME", WHITE)
        
        # date
        rectDate = pygame.Rect(0, 70, 120, 20)
        rectDate.right = screen_width - 20
        myfont.render_to(self.screen, rectDate, "DATE", WHITE)
        
        # score
        rectScore = pygame.Rect(0, 70, 100, 20)
        rectScore.right = rectDate.left - 20
        myfont.render_to(self.screen, rectScore, "SCORE", WHITE)

        pygame.draw.line(self.screen, WHITE, (20,rectScore.bottom+10), (screen_width-20, rectScore.bottom+10), 2)

        # render hint 
        rectHelp = myfontSmall.get_rect("Press 'M' to go to the Main Menu")
        rectHelp.left = (screen_width - rectHelp.width) / 2
        rectHelp.bottom = screen_height - 5
        myfontSmall.render_to(self.screen, rectHelp, None, WHITE)    

        # Render Contents
        for n in range(len(self.scores)):
            # place
            rectPlace = pygame.Rect(20, n*42+120, 20, 20)
            myfont.render_to(self.screen, rectPlace, str(n+1), WHITE)

            # name
            rectName = pygame.Rect(rectPlace.right + 15, n*42+120, 140, 20)
            myfont.render_to(self.screen, rectName, self.scores[n]["NAME"], WHITE)
            
            # date
            rectDate = pygame.Rect(0, n*42+120, 120, 20)
            rectDate.right = screen_width - 20
            myfont.render_to(self.screen, rectDate, self.scores[n]["DATE"], WHITE)
            
            # score
            rectScore = pygame.Rect(0, n*42+120, 100, 20)
            rectScore.right = rectDate.left - 20
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
                    mainMenuSound.play()


class GameOver():
    def __init__(self, screen, stateMachine, score):
        self.screen = screen
        self.stateMachine = stateMachine
        self.name = []
        self.maxLenOfName = 8
        self.rectForName = pygame.Rect(0,0,0,0)
        self.score = score
        self.minHighestScore = Score(self.screen, self.stateMachine).GetMinScore()
        self.IsScoreGoingToLeaderboard = self.score > self.minHighestScore
        if self.IsScoreGoingToLeaderboard:
            self.updateFunction = self.GetUserName
        else:
            self.updateFunction = self.RenderGameOver

    def Start(self):
        

        # Check whether user's score is enough to get him into the table
        if self.IsScoreGoingToLeaderboard:
            victorySound.play()
            # Draw borders
            rectBorder = pygame.Rect(0,0, 340, 200)
            rectBorder.left = (screen_width - rectBorder.width)/2
            rectBorder.top = (screen_height - rectBorder.height)/2
            pygame.draw.rect(self.screen, BLACK, rectBorder)
            pygame.draw.rect(self.screen, RED, rectBorder, width=3)
            
            # GameOver text
            rectGameOver = myfont.get_rect("GAME OVER")
            rectGameOver.left = (screen_width-rectGameOver.width) / 2
            rectGameOver.top = rectBorder.top + 10
            myfont.render_to(self.screen, rectGameOver, None, WHITE)

            # Render Victory sign
            # render skull
            try:
                cup = pygame.image.load("cup_fz.png")
                cup.convert_alpha()
                cup = pygame.transform.scale(cup, (60,60))
                rectCup = pygame.Rect((screen_width-cup.get_width())/2, rectGameOver.bottom + 10, cup.get_width(), cup.get_height())

                self.screen.blit(cup, rectCup)
            except FileNotFoundError:
                rectCup = pygame.Rect((screen_width-60)/2, rectGameOver.bottom + 10, 60, 60)
                print("Cup img isn't found")

            # text
            rectText = myfontSmall.get_rect("CONGRATULATIONS!")
            rectText.left = (screen_width-rectText.width) / 2
            rectText.top = rectCup.bottom + 20
            myfontSmall.render_to(self.screen, rectText, None, WHITE)

            rectText2 = myfontSmall.get_rect("Provide your name for the leaderboard")
            rectText2.left = (screen_width-rectText2.width) / 2
            rectText2.top = rectText.bottom + 5
            myfontSmall.render_to(self.screen, rectText2, None, WHITE)

            # Place for name
            rectName = myfont.get_rect("ASDFGHJQ")
            rectName.left = (screen_width-rectName.width) / 2
            rectName.top = rectText2.bottom + 10

            rectUnderscore = myfont.get_rect("________")
            rectUnderscore.left = rectName.left
            rectUnderscore.top = rectName.bottom + 5
            myfont.render_to(self.screen, rectUnderscore, None, WHITE)
            self.rectForName = rectName

            # Hint
            rectHint = myfontSmall.get_rect("PRESS 'RETURN' TO SUBMIT")
            rectHint.left = (screen_width - rectHint.width) / 2
            rectHint.bottom = screen_height - 23
            pygame.draw.rect(self.screen, BLACK, (0, rectHint.top, screen_width, rectHint.height))
            myfontSmall.render_to(self.screen, rectHint, None, WHITE)

        else:
            # Draw borders
            rectBorder = pygame.Rect(0,0, 340, 150)
            rectBorder.left = (screen_width - rectBorder.width)/2
            rectBorder.top = (screen_height - rectBorder.height)/2
            pygame.draw.rect(self.screen, RED, rectBorder)
            pygame.draw.rect(self.screen, RED, rectBorder, width=3)
            
            # GameOver text
            rectGameOver = myfont.get_rect("GAME OVER")
            rectGameOver.left = (screen_width-rectGameOver.width) / 2
            rectGameOver.top = rectBorder.top + 10
            myfont.render_to(self.screen, rectGameOver, None, WHITE)
            
            # render skull
            try:
                skull = pygame.image.load("skull_fz.png")
                skull.convert_alpha()
                skull = pygame.transform.scale(skull, (60,50))
                rectSkull = pygame.Rect((screen_width-skull.get_width())/2, rectGameOver.bottom + 10, skull.get_width(), skull.get_height())
                self.screen.blit(skull, rectSkull)
            except FileNotFoundError:
                rectSkull = pygame.Rect((screen_width-60)/2, rectGameOver.bottom + 10, 60, 50)
                print("Skull img isn't found")
            
            # ordinary game over text
            rectTryAgain = myfontSmall.get_rect("PRESS 'R' TO TRY AGAIN")
            rectTryAgain.left = (screen_width-rectTryAgain.width) / 2
            rectTryAgain.top = rectSkull.bottom + 15
            myfontSmall.render_to(self.screen, rectTryAgain, None, WHITE)

            rectQuitToMenu = myfontSmall.get_rect("PRESS 'Q' TO QUIT")
            rectQuitToMenu.left = (screen_width-rectQuitToMenu.width) / 2
            rectQuitToMenu.top = rectTryAgain.bottom + 10
            myfontSmall.render_to(self.screen, rectQuitToMenu, None, WHITE)


        pygame.display.flip()

    
    def Update(self):
        self.updateFunction()
        

    def RenderName(self):
        pygame.draw.rect(self.screen, BLACK, self.rectForName)
        rectName = myfont.get_rect("".join(self.name))
        rectName.left = self.rectForName.left
        rectName.top = self.rectForName.top
        myfont.render_to(self.screen, rectName, None, WHITE)
        pygame.display.flip()

    def GetUserName(self):
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                self.stateMachine.Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == locals.K_BACKSPACE and len(self.name) > 0:
                    self.name.pop(-1)
                    self.RenderName()
                    deleteSound.play()
                
                # when player press return and the name is typed add this name to the leaderboard
                elif event.key == locals.K_RETURN and len(self.name) > 0:
                    newState = Score(self.screen, self.stateMachine)
                    newState.AddNewScore("".join(self.name), self.score)
                    self.stateMachine.ChangeState(newState)
                    return

                # the ability to type name
                letter = event.unicode
                if letter.isalpha() and len(self.name) < self.maxLenOfName:
                    self.name.append(letter.upper())
                    self.RenderName()
                    typeSound.play()
        

    def RenderGameOver(self):
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                self.stateMachine.Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == locals.K_q:
                    self.stateMachine.ChangeState(MainMenu(self.screen, self.stateMachine))
                if event.key == locals.K_r:
                    self.stateMachine.ChangeState(Game(self.screen, self.stateMachine))



        
            
