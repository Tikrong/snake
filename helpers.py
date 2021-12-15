# class for handling the snake
class Snake():
    def __init__(self, size, initialPos):
        self.size = size
        # position of the snake, cekk[0] is head
        self.cells = [initialPos]
        for i in range(size-1):
            self.cells.append((initialPos[0], initialPos[1] - 1 -i))


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
    
    def DrawField(self, _snake):
        for i in range(_snake.size):
            self.field[_snake.cells[i][0]][_snake.cells[i][1]] = 1

        

game = GameField()
snake = Snake(3, (3,3))
game.DrawField(snake)
for row in game.field:
    print(row)
