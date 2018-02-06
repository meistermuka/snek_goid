from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT

from constants import SNEK_LENGTH, MAX_Y, MAX_X, TIMEOUT

class Body(object):
    def __init__(self, x, y, char="-"):
        self.x = x
        self.y = y
        self.char = char

    @property
    def coord(self):
        return self.x, self.y


class Snek(object):

    REV_DIR_MAP = {
        KEY_UP: KEY_DOWN,
        KEY_DOWN: KEY_UP,
        KEY_LEFT: KEY_RIGHT,
        KEY_RIGHT: KEY_LEFT
    }

    def __init__(self, x, y, window):

        self.body_list = []
        self.hit_score = 0
        self.timeout = TIMEOUT

        for i in range(SNEK_LENGTH, 0, -1):
            self.body_list.append(Body(x -i, y))

        # Adding the head
        self.body_list.append(Body(x, y, '0'))
        self.window = window
        self.direction = KEY_RIGHT
        self.last_head_coord = (x, y)
        self.direction_map = {
            KEY_UP: self.move_up,
            KEY_DOWN: self.move_down,
            KEY_LEFT: self.move_left,
            KEY_RIGHT: self.move_right
        }

    @property
    def score(self):
        return self.hit_score

    def add_body(self, body_list):
        self.body_list.extend(body_list)

    def eat_poid(self):
        body = Body(self.last_head_coord[0], self.last_head_coord[1])
        self.body_list.insert(-1, body)
        self.hit_score += 1

    @property
    def collided(self):
        return any([body.coord == self.head.coord for body in self.body_list[:-1]])

    def update(self):
        last_body = self.body_list.pop(0)
        last_body.x = self.body_list[-1].x
        last_body.y = self.body_list[-1].y
        self.body_list.insert(-1, last_body)
        self.last_head_coord = (self.head.x, self.head.y)
        self.direction_map[self.direction]()

    def change_direction(self, direction):
        if direction != Snek.REV_DIR_MAP[self.direction]:
            self.direction = direction

    def render(self):
        for body in self.body_list:
            self.window.addstr(body.y, body.x, body.char)

    @property
    def head(self):
        return self.body_list[-1]

    @property
    def coord(self):
        return self.head.x, self.head.y

    def move_up(self):
        self.head.y -= 1
        if self.head.y < 1:
            self.head.y = MAX_Y

    def move_down(self):
        self.head.y += 1
        if self.head.y > MAX_Y:
            self.head.y = 1

    def move_left(self):
        self.head.x -= 1
        if self.head.x < 1:
            self.head.x = MAX_X

    def move_right(self):
        self.head.x += 1
        if self.head.x > MAX_X:
            self.head.x = 1
