import curses

from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT

from constants import HEIGHT, WIDTH, TIMEOUT, SNEK_X, SNEK_Y
from snek import Snek
from food import Food


if __name__ == "__main__":

    curses.initscr()
    curses.beep()
    curses.beep()

    window = curses.newwin(HEIGHT, WIDTH, 0, 0)
    window.timeout(TIMEOUT)
    window.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    window.border(0)

    snek = Snek(SNEK_X, SNEK_Y, window)
    food = Food(window)

    while True:
        window.clear()
        window.border(0)
        snek.render()
        food.render()

        window.addstr(0, 5, snek.score)
        event = window.getch()

        if event == 27:
            break

        if event in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
            snek.change_direction(event)

        if snek.head.x == food.x and snek.head.y == food.y:
            snek.eat_food(food)

        if event == 32:
            key = -1
            while key != 32:
                key = window.getch()

        snek.update()
        if snek.collided:
            break

    curses.endwin()
