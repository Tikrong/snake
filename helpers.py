# FOR LATER
# change size-1 and size-2 for -1 and -2, it'll be the same

import random

# class for handling the snake
class Snake():
    def __init__(self, size, initialPos):
        self.size = size
        # position of the snake, cell[size-1] is head
        self.cells = []
        # position where the tail was before it was deleted (after snake moved)
        self.tailWasHere = (1,1)
        for i in range(self.size):
            self.cells.append((initialPos[0], initialPos[1] - size + 1 + i))
            print(self.cells)

    # Movement
    def MoveLeft(self):
        self.cells.append((self.cells[self.size-1][0], self.cells[self.size-1][1] - 1))
        self.tailWasHere = self.cells.pop(0)


    def MoveRight(self):
        self.cells.append((self.cells[self.size-1][0], self.cells[self.size-1][1] + 1))
        self.tailWasHere = self.cells.pop(0)

    def MoveUp(self):
        self.cells.append((self.cells[self.size-1][0] - 1, self.cells[self.size-1][1]))
        self.tailWasHere = self.cells.pop(0)

    def MoveDown(self):
        self.cells.append((self.cells[self.size-1][0] + 1, self.cells[self.size-1][1]))
        self.tailWasHere = self.cells.pop(0)

    # when player does nothing snake continue to move in the same direction it moved before
    # to calculate it we take head and neck as points and their coordinates as vectors.
    # We substract Vn from Vh and find vector from neck to head, and then add this vector to
    # head vector and get new position for head.
    # neck is the cell of the snake clostst to the head
    def MoveOnYourOwn(self):
        tmp = (self.cells[self.size-1][0] - self.cells[self.size-2][0], self.cells[self.size-1][1] - self.cells[self.size-2][1])
        self.cells.append((self.cells[self.size-1][0] + tmp[0], self.cells[self.size-1][1] + tmp[1]))
        print(self.cells)
        self.tailWasHere = self.cells.pop(0)
        print(self.tailWasHere)
        print(tmp)

    # Growth
    def Grow(self):
        self.cells.insert(0, self.tailWasHere)
        self.size += 1



# class for handling the game board

# gamefield is an 2d array where
# 0 - empty cell
# 1 - snake
# 2 - obstacle or wall
# 3 - food

class GameField():
    def __init__(self):
        self.height = 10
        self.width = 10
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
        
        # for storing information about food
        self.food = set()

    # check whether snake make a valid move, i.e. not collided with a wall or itself
    # returns true if snake is collided or false if it is alive
    def IsSnakeCollided(self, snake):
        # check whether snake has collided with a wall
        for i in range(snake.size):
            if snake.cells[i] in  self.borders:
                return True
        
        # check whether snake has collided with itself
        if len(set(snake.cells)) < snake.size:
            return True
        
        return False

    # this 
    def DrawField(self, _snake):
        for i in range(_snake.size):
            self.field[_snake.cells[i][0]][_snake.cells[i][1]] = 1
        # mark as empty the position where tail was before the movement
        self.field[_snake.tailWasHere[0]][_snake.tailWasHere[1]] = 0

    # method for placing food in the field
    def PlaceFood(self):
        while True:
            food = (random.randint(0, self.height-1), random.randint(0, self.width-1))
            if food not in self.borders and food not in self.food:
                self.food.add(food)
                self.field[food[0]][food[1]] = 3
                break
    # checks whether snake got food
    def DidSnakeGetFood(self, snake):
        if snake.cells[snake.size-1] in self.food:
            self.food.remove(snake.cells[snake.size-1])
            self.field[snake.cells[snake.size-1][0]][snake.cells[snake.size-1][1]] = 1
            snake.Grow()
            self.DrawField(snake)
            return True
        else:
            return False






