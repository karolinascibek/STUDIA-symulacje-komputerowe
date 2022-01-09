from Ant import Ant

class Alg_Ants_Langton():

    ants = []
    n = 100

    def __init__(self, n, number_ants):
        self.ants = self.create_ants(number_ants, n)
        self.n = n

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

    def alg(self, iterations):
        n = self.n
        board = self.create_board(n, n)

        for i in range(iterations):
            for idx, ant in enumerate(self.ants):
                x, y = ant.current_coord

                if x < 0:
                    ant.set_current_coord(n - 1, y)
                if x >= n:
                    ant.set_current_coord(0, y)
                if y < 0:
                    ant.set_current_coord(x, n - 1)
                if y >= n:
                    ant.set_current_coord(x, 0)

                x, y = ant.current_coord

                if board[x][y] == 0:
                    board[x][y] = idx+1
                    ant.move("L")

                else:
                    board[x][y] = 0
                    ant.move("R")
        return board

