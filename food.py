import math

from operator import itemgetter

from constants import SEPARATION_FACTOR, NUM_NEIGHBOURS, COHERENCE_FACTOR


class Poid(object):

    def __init__(self, x, y, vx, vy, window, char="*"):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.window = window
        self.char = char

    def render(self):
        self.window.addstr(self.y, self.x, self.char)

    def _distance(self, poid_a, poid_n):
        x = poid_a[0] - poid_n[0]
        y = poid_a[1] - poid_n[1]
        return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

    def nearest_neighbours(self, poid_list):
        new_poids = []

        for poid in poid_list:
            new_poids.append((self._distance((self.x, self.y), (poid.x, poid.y)), poid))

        new_poids.sort(key=itemgetter(0))
        return [poid[1] for poid in new_poids]

    def separate(self, neighbours):
        x, y = 0, 0
        for neighbour in neighbours[:NUM_NEIGHBOURS]:
            if self._distance((self.x, self.y), (neighbour.x, neighbour.y)) < SEPARATION_FACTOR:
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
