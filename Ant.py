import random


class Ant():
    color = "blue"
    current_coord = (50, 50)
    direction = "W"

    # (y, x)
    coord_moves = {'W': (0, -1), 'E': (0, 1), 'N': (-1, 0), 'S': (1, 0)}
    direction_moves = {
        "L": {'W': 'S', 'E': 'N', 'N': 'W', 'S': 'E'},
        "R": {'W': 'N', 'E': 'S', 'N': 'E', 'S': 'W'}
    }

    def __init__(self, n):
        self.current_coord = (random.randint(0, n), random.randint(0, n - 1))
        self.direction = list(self.coord_moves.keys())[random.randint(0, 3)]
        self.draw_color()

    def draw_positions(self):
        pass

    def draw_color(self):
        rgb = (random.randrange(255), random.randrange(255), random.randrange(255))
        self.color = '#%02x%02x%02x' % rgb

    def move(self, side):
        # ruch w lewo z kierunku w jakim ustawiona jest mrówka
        direction = self.direction_moves[side][self.direction]

        # przesunięcie mrówki
        x = self.current_coord[0] + self.coord_moves[direction][0]
        y = self.current_coord[1] + self.coord_moves[direction][1]
        self.current_coord = (x, y)

        # ustawienie akltualnego kierunku mrówki
        self.direction = direction
        return self.current_coord

    def set_current_coord(self, x, y):
        self.current_coord = (x, y)




