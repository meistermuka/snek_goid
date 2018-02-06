import math

from operator import itemgetter
from random import randint

from constants import MAX_Y, MAX_X, GOID_SIZE, SEPARATION_FACTOR, NUM_NEIGHBOURS, COHERENCE_FACTOR


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

    def _distance(self, goid_a, goid_n):
        x = goid_a[0] - goid_n[0]
        y = goid_a[1] - goid_n[1]
        return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

    def nearest_neighbours(self, goid_list):
        new_goids = []

        for goid in goid_list:
            new_goids.append((self._distance((self.x, self.y), (goid.x, goid.y)), goid))

        new_goids.sort(key=itemgetter(0))
        return [goid[1] for goid in new_goids]

    def separate(self, neighbours):
        x, y = 0, 0
        for neighbour in neighbours[:NUM_NEIGHBOURS]:
            if self._distance((self.x, self.y), neighbour) < SEPARATION_FACTOR:
                x += self.x - neighbour.x
                y += self.y - neighbour.y

        self.vx = x
        self.vy = y
        self.x += x
        self.y += y

    def align(self, neighbours):
        x, y = 0, 0
        for neighbour in neighbours[:NUM_NEIGHBOURS]:
            x += neighbour.vx
            y += neighbour.vy

        dx, dy = x / NUM_NEIGHBOURS, y / NUM_NEIGHBOURS
        self.vx += dx
        self.vy += dy
        self.x += dx
        self.y += dy

    def cohere(self, neighbours):
        x, y = 0, 0
        for neighbour in neighbours[:NUM_NEIGHBOURS]:
            x += neighbour.x
            y += neighbour.y

        dx, dy = ((x / NUM_NEIGHBOURS) - self.x)/COHERENCE_FACTOR, ((y / NUM_NEIGHBOURS) - self.y)/COHERENCE_FACTOR
        self.vx += dx
        self.vy += dy
        self.x += dx
        self.y += dy





def create_random_goid():
    """Creates a random Goid and returns it"""
    return Goid(randint(1, MAX_X), randint(1, MAX_Y), randint(1, GOID_SIZE), randint(1, GOID_SIZE), GOID_SIZE)

