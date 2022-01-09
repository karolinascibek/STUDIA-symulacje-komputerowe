class Alg_Ants_Langton():

    def alg(self, board, ants, iterations):
        n = len(board)

        for i in range(iterations):
            for idx, ant in enumerate(ants):
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