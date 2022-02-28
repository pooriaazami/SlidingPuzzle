from Search import a_start
from SlidingPuzzle import Puzzle

from Seachable import Searchable

import numpy as np


def heuristic_function(size):
    def function(state: Searchable):
        state: np.ndarray = state.state

        cost = 0

        for row_index, row in enumerate(state):
            for column_index, element in enumerate(row):

                if element == -1:
                    continue
                x, y = divmod(element - 1, size)

                cost += abs(x - row_index) + abs(y - column_index)

        return cost

    return function


def main():
    puzzle = Puzzle(4)
    puzzle.reset()

    print('blank puzzle:')
    print(puzzle)
    print('')

    print('is_goal():')
    print(puzzle.is_goal())
    print()

    print('actions:')
    print()
    actions = [(Puzzle.UP, 'up'), (Puzzle.LEFT, 'left'), (Puzzle.DOWN, 'down'), (Puzzle.RIGHT, 'right')]

    for action, name in actions:
        for _ in range(4):
            print(f'{name}:')
            result = puzzle.step(action)
            print(puzzle)
            print(result)
            print()

    print('Siblings:')
    for sibling, _ in puzzle.siblings:
        print(sibling)
        print()

    puzzle.step(Puzzle.UP)
    puzzle.step(Puzzle.LEFT)

    print('Siblings:')
    print('actual puzzle:')
    print(puzzle)
    print()
    print()
    for sibling, _ in puzzle.siblings:
        print(sibling)
        print()

    print('-' * 100)
    puzzle = Puzzle(4)
    puzzle.reset()
    print(puzzle)
    print()
    print()
    print('heuristic:')
    h = heuristic_function(4)
    cost = h(puzzle)
    print(cost)


if __name__ == '__main__':
    main()
