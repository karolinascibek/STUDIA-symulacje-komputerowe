from Ant import Ant


class Alg_Ants_Langton():

    ants = []
    n = 100
    board = []

    def __init__(self, n, number_ants):
        self.ants = self.create_ants(number_ants, n)
        self.n = n
        self.board = self.create_board(n, n)

    def create_board(self, n, m):
        self.n = n
        board = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(0)
            board.append(row)
        return board

    def display_board(self, board):
        for row in board:
            print(row)

    def create_ants(self, number_ants, n):
        return [Ant(n) for i in range(number_ants)]

    def check_coord(self, ant, n):
        x, y = ant.current_coord
        if x < 0:
            x = n - 1
        if x >= n:
            x = 0
        if y < 0:
            y = n - 1
        if y >= n:
            y = 0
        ant.set_current_coord(x, y)

    def alg(self, iterations):
        n = self.n

        for i in range(iterations):
            for idx, ant in enumerate(self.ants):
                self.check_coord(ant, n)
                x, y = ant.current_coord

                if self.board[x][y] == 0:
                    self.board[x][y] = idx+1
                    ant.move("L")

                else:
                    self.board[x][y] = 0
                    ant.move("R")

                self.check_coord(ant, n)

        return self.board

