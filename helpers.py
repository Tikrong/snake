# FOR LATER
# change size-1 and size-2 for -1 and -2, it'll be the same

# class for handling the snake
class Snake():
    def __init__(self, size, initialPos):
        self.size = size
        # position of the snake, cell[size-1] is head
        self.cells = []
        # position where the tail was before it was deleted (after snake moved)
        self.tailWasHere = (0,0)
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
        self.cells.append(self.tailWasHere)
        self.size += 1



# class for handling the game board

class GameField():
    def __init__(self):
        self.height = 5
        self.width = 5
        # initiate game field
        self.field = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(0)
            self.field.append(row)
        # add borders to the field
        self.borders = set()
        # add vercical borders
        for x in range(self.width):
            self.borders.add((0,x))
            self.borders.add((self.height-1, x))
        # add horizontal borders
        for x in range(self.height):
            self.borders.add((x,0))
            self.borders.add((x, self.width-1))


        # add

    def DrawField(self, _snake):
        for i in range(_snake.size):
            self.field[_snake.cells[i][0]][_snake.cells[i][1]] = 1
        # mark as empty the position where tail was before the movement
        self.field[_snake.tailWasHere[0]][_snake.tailWasHere[1]] = 0



game = GameField()
snake = Snake(3, (3,3))
game.DrawField(snake)
for row in game.field:
    print(row)

print()

snake.MoveUp()
game.DrawField(snake)
snake.MoveOnYourOwn()

game.DrawField(snake)
for row in game.field:
    print(row)

print()

print(game.borders)



