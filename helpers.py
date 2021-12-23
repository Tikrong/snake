# FOR LATER
# change size-1 and size-2 for -1 and -2, it'll be the same

import random

# class for handling the snake
class Snake():
    def __init__(self, size, initialPos):
        self.size = size
        # position of the snake, cell[size-1] is head
        self.cells = []
        for i in range(self.size):
            self.cells.append((initialPos[0], initialPos[1] - size + 1 + i))

    # Movement
    # If player tries to move snake in oppisite direction (it goes left player presses right)
    # snake wont move and the function returns False, that means no movement happend
    def MoveLeft(self):
        cell = (self.cells[self.size-1][0], self.cells[self.size-1][1] - 1)
        if self.IsSnakeMovesBackwards(cell):
            return False
        self.cells.append(cell)
        self.cells.pop(0)
        return True

    def MoveRight(self):
        cell = (self.cells[self.size-1][0], self.cells[self.size-1][1] + 1)
        if self.IsSnakeMovesBackwards(cell):
            return False
        self.cells.append(cell)
        self.cells.pop(0)
        return True

    def MoveUp(self):
        cell = (self.cells[self.size-1][0] - 1, self.cells[self.size-1][1])
        if self.IsSnakeMovesBackwards(cell):
            return False
        self.cells.append(cell)
        self.cells.pop(0)
        return True

    def MoveDown(self):
        cell = (self.cells[self.size-1][0] + 1, self.cells[self.size-1][1])
        if self.IsSnakeMovesBackwards(cell):
            return False
        self.cells.append(cell)
        self.cells.pop(0)
        return True

    # when player does nothing snake continue to move in the same direction it moved before
    # to calculate it we take head and neck as points and their coordinates as vectors.
    # We substract Vn from Vh and find vector from neck to head, and then add this vector to
    # head vector and get new position for head.
    # neck is the cell of the snake clostst to the head
    def MoveOnYourOwn(self):
        tmp = (self.cells[self.size-1][0] - self.cells[self.size-2][0], self.cells[self.size-1][1] - self.cells[self.size-2][1])
        self.cells.append((self.cells[self.size-1][0] + tmp[0], self.cells[self.size-1][1] + tmp[1]))
        self.cells.pop(0)


    # Growth
    def Grow(self):
        self.cells.insert(0, (self.cells[0]))    
        self.size += 1

    def IsSnakeMovesBackwards(self, cell):
        return self.cells[-2] == cell



# class for handling the game board

# gamefield is an 2d array where
# 0 - empty cell
# 1 - snake
# 2 - obstacle or wall
# 3 - food

class GameField():
    def __init__(self, height, width, snake):
        self.height = height
        self.width = width
        self.snake = snake
        # initiate game field
        self.field = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(0)
            self.field.append(row)
        # add borders to the field
        self.borders = set()
        # add horizontal borders to the set of obstacles and to the gamefield
        for x in range(self.width):
            self.borders.add((0,x))
            self.borders.add((self.height-1, x))
            self.field[0][x] = 2
            self.field[self.height-1][x] = 2
        # add horizontal borders to the set of obstacles and to the gamefield
        for x in range(self.height):
            self.borders.add((x,0))
            self.borders.add((x, self.width-1))
            self.field[x][0] = 2
            self.field[x][self.width-1] = 2
        
        # add snake to the game field
        for y,x in snake.cells:
            self.field[y][x] = 1

        # place initial food
        self.food = self.PlaceFood()
        
        

    # check whether snake make a valid move, i.e. not collided with a wall or itself
    # returns true if snake is collided or false if it is alive
    def IsSnakeCollided(self):
        
        y,x = self.snake.cells[-1]
        # check whether snake has collided with a wall
        if self.field[y][x] == 2:
            return True
            
        # check whether snake has collided with itself
        for i in range(self.snake.size - 1):
            if self.snake.cells[-1] == self.snake.cells[i]:
                return True
            
        
        
        return False

    # this 
    def DrawField(self):
        for y in range(self.height):
            for x in range(self.width):
                if (y,x) in self.snake.cells:
                    self.field[y][x] = 1
                elif (y,x) == self.food:
                    self.field[y][x] = 3
                elif (y,x) in self.borders:
                    self.field[y][x] = 2
                else:
                    self.field[y][x] = 0

    # method for placing food in the field
    def PlaceFood(self):
        while True:
            food = (random.randint(0, self.height-1), random.randint(0, self.width-1))
            if self.field[food[0]][food[1]] == 0:
                self.field[food[0]][food[1]] = 3
                return food

    # checks whether snake got food
    def DidSnakeGetFood(self):
        y,x = self.snake.cells[-1]
        if self.field[y][x] == 3:
            self.snake.Grow()
            self.food = self.PlaceFood()
            return True
        else:
            return False






