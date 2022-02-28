import random

import numpy as np

from Seachable import Searchable


class Puzzle(Searchable):
    BLANK = -1

    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    def __init__(self, size):
        self.__size = size

        self.__state = None
        self.__hole = None

        self.__maximum_element_length = len(str(self.__size * self.__size))

    def reset(self):
        self.__state = [i for i in range(1, self.__size * self.__size)]
        self.__state.append(Puzzle.BLANK)

        self.__state = np.array(self.__state).reshape(self.__size, self.__size)

        self.__hole = self.__size - 1, self.__size - 1

    def set_state(self, state, hole_pos):
        self.__state = state
        self.__hole = hole_pos

    def clone(self):
        new_puzzle = Puzzle(self.__size)
        new_puzzle.set_state(self.__state.copy(), self.__hole)

        return new_puzzle

    def shuffle(self, count):
        for _ in range(count):
            self.step(random.randint(1, 4))

    def is_goal(self):
        counter = 1

        for row in self.__state:
            for element in row:
                if element != counter:
                    break
                counter += 1

        return counter == self.__size * self.__size and element == -1

    @property
    def state(self):
        return self.__state.copy()

    def __get_new_position(self, action):
        x, y = self.__hole

        new_x, new_y = x, y
        if action == Puzzle.UP:
            new_y -= 1
            new_y = max(0, new_y)
        elif action == Puzzle.DOWN:
            new_y += 1
            new_y = min(self.__size - 1, new_y)
        elif action == Puzzle.LEFT:
            new_x -= 1
            new_x = max(0, new_x)
        elif action == Puzzle.RIGHT:
            new_x += 1
            new_x = min(self.__size - 1, new_x)

        return new_x != x or new_y != y, (new_x, new_y)

    def __swap(self, first_pos, second_pos):
        temp = self.__state[first_pos[1], first_pos[0]]
        self.__state[first_pos[1], first_pos[0]] = self.__state[second_pos[1], second_pos[0]]
        self.__state[second_pos[1], second_pos[0]] = temp

    def step(self, action):
        result, new_pos = self.__get_new_position(action)

        if not result:
            return False

        self.__swap(self.__hole, new_pos)
        self.__hole = new_pos

        return True

    @property
    def siblings(self):
        for action in [Puzzle.UP, Puzzle.DOWN, Puzzle.RIGHT, Puzzle.LEFT]:
            new_puzzle = self.clone()
            result = new_puzzle.step(action)

            if result:
                yield new_puzzle, action

    @property
    def size(self):
        return self.__state.shape

    def __str__(self) -> str:
        rows = []

        for row in self.__state:
            edited_row = '|'
            for element in row:
                element = str(element) if element != Puzzle.BLANK else ' ' * (self.__maximum_element_length - 1) + '.'
                element = ' ' * (self.__maximum_element_length - len(element)) + element + '|'
                edited_row += element

            rows.append(edited_row)

        return '\n'.join(rows)
