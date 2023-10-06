class Bar:
    def __init__(self):
        self.array = [
            [f'1', f'2', f'3'],
            [f'4', f'5', f'6'],
            [f'7', f'8', f'9'],
        ]
        self.cells = {
            '1': [0, 0], '2': [0, 1], '3': [0, 2],
            '4': [1, 0], '5': [1, 1], '6': [1, 2],
            '7': [2, 0], '8': [2, 1], '9': [2, 2],
        }
        self.is_winner = False
        self.is_draw = False
        self.wrong_cell = False

    def print(self):
        j = 0
        for i in range(len(self.array[j])):
            for j in range(len(self.array)):
                if j == 0:
                    print(self.array[i][j], end=' |')
                elif j == 2:
                    print(f'| {self.array[i][j]}', end='  ')
                else:
                    print(f' {self.array[i][j]}', end=' ')
            print()
            if i != len(self.array) - 1:
                print('-' * 10)
        print()

    def put_symbol(self, cell, symbol):
        self.array[self.cells[cell][0]][self.cells[cell][1]] = symbol
        del self.cells[cell]
        if not self.cells:
            self.is_draw = True

    def is_none(self, cell):
        result = self.cells.get(cell, None)
        if result != None:
            return False
        return True

    def check_is_over(self, symbol):
        for i in range(len(self.array)):
            j = 0
            if self.array[i][j] == symbol and self.array[i][j + 1] == symbol and self.array[i][j + 2] == symbol:
                self.is_winner = True
                return True
        for j in range(len(self.array)):
            i = 0
            if self.array[i][j] == symbol and self.array[i + 1][j] == symbol and self.array[i + 2][j] == symbol:
                self.is_winner = True
                return True
        i, j = 0, 0
        if  self.array[i][j] == symbol and self.array[i + 1][j + 1] == symbol and self.array[i + 2][j + 2] == symbol:
            self.is_winner = True
            return True
        elif self.array[i][j + 2] == symbol and self.array[i + 1][j + 1] == symbol and self.array[i + 2][j] == symbol:
            self.is_winner = True
            return True
        return False


class User:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol