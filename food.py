from random import randint

from constants import MAX_Y, MAX_X, WIDTH, HEIGHT, GOID_SIZE


class Food(object):

    def __init__(self, window, char='&'):
        self.reset()
        self.char = char
        self.window = window

    def render(self):
        self.window.addstr(self.y, self.x, self.char)

    def reset(self):
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)


class Goid(object):

    def __init__(self, x, y, vx, vy, r, color=None):
        self.x = x
        self.y = y,
        self.vx = vx,
        self.vy = vy
        self.color = color

    def nearest_neighbour(self, goid_list):
        neighbours = []
        for goid in goid_list:
            neighbours.append(goid)



def create_random_goid():
    """Creates a random Goid and returns it"""
    return Goid(randint(1, MAX_X), randint(1, MAX_Y), randint(1, GOID_SIZE), randint(1, GOID_SIZE), GOID_SIZE)

