from Seachable import Searchable
import numpy as np

from Search import a_start
from SlidingPuzzle import Puzzle


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


def fast_heuristic_function(size):
    def function(state: Searchable):
        state: np.ndarray = state.state

        cost = 0
        counter = 1
        for row_index, row in enumerate(state):
            for column_index, element in enumerate(row):

                if element == -1:
                    continue
                counter += 1

                if counter != element:
                    cost += 1

        return cost

    return function


def bfs_heuristic(state):
    return 0


def main():
    size = 4
    puzzle = Puzzle(size)
    puzzle.reset()
    puzzle.shuffle(20)
    print('Puzzle shuffled')
    print(puzzle)
    print('-' * 100)
    heuristic = heuristic_function(size)

    path = a_start(puzzle, heuristic)

    for action in path.steps:
        if action == Puzzle.UP:
            print('UP')
        elif action == Puzzle.DOWN:
            print('DOWN')
        elif action == Puzzle.LEFT:
            print('LEFT')
        elif action == Puzzle.RIGHT:
            print('RIGHT')

        puzzle.step(action)
        print(puzzle)


if __name__ == '__main__':
    main()
