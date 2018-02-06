import curses

from random import randint

from constants import HEIGHT, WIDTH, TIMEOUT, MAX_X, MAX_Y, POID_SIZE, POID_POPULATION
from food import Poid


def stay_in_window(poid):
    if poid.x < 0:
        poid.x = MAX_X + poid.x
    elif poid.x > MAX_X:
        poid.x = MAX_X - poid.x

    if poid.y < 0:
        poid.y = MAX_Y + poid.y
    elif poid.y > MAX_Y:
        poid.y = MAX_Y - poid.y

def move_poids(poids):
    for poid in poids:
        neighbours = poid.nearest_neighbours(poids)
        poid.separate(neighbours)
        poid.align(neighbours)
        poid.cohere(neighbours)
        stay_in_window(poid)
        poid.render()


if __name__ == "__main__":

    curses.initscr()

    window = curses.newwin(HEIGHT, WIDTH, 0, 0)
    window.timeout(TIMEOUT)
    window.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    window.border()

    the_poids = []
    for p in xrange(POID_POPULATION):
        the_poids.append(Poid(randint(1, MAX_X),
                              randint(1, MAX_Y),
                              randint(1, POID_SIZE),
                              randint(1, POID_SIZE),
                              window))

    while True:
        window.clear()
        window.border()
        move_poids(the_poids)
        # food.render()

        window.addstr(0, 5, "Snek-Poid")
        event = window.getch()

        if event == 27:
            break

        if event == 32:
            key = -1
            while key != 32:
                key = window.getch()


    curses.endwin()
