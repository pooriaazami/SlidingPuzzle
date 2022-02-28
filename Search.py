from copy import deepcopy
from queue import PriorityQueue

from Seachable import Searchable
from Utils import Path

import matplotlib.pyplot as plt


def plot_heuristic(axs, heuristic_values, new_heuristic_value, frontier_values, new_frontier_value):
    heuristic_values.append(new_heuristic_value)
    frontier_values.append(new_frontier_value)

    if len(heuristic_values) > 100:
        heuristic_values.pop(0)

    if len(frontier_values) > 100:
        frontier_values.pop(0)

    axs[0].cla()
    axs[1].cla()

    axs[0].plot(heuristic_values, color='green', label='heuristic values')
    axs[1].plot(frontier_values, color='red', label='frontier length')

    axs[0].legend()
    axs[1].legend()

    plt.pause(0.01)


def a_start(root: Searchable, heuristic):
    queue = PriorityQueue()

    initial_path = Path()
    heuristic_value = heuristic(root)
    initial_path.append(0, 0, root, heuristic_value)
    queue.put((0, initial_path))

    values = []
    frontier = []

    fig, axs = plt.subplots(2, 1)
    seen = []

    while not queue.empty():
        best_choice = queue.get()[1]
        terminal = best_choice.terminal

        if terminal.is_goal():
            plt.show()
            return best_choice
        seen.append(terminal)

        for sibling, action in terminal.siblings:
            estimate = heuristic(terminal)
            function = best_choice.cost + estimate
            path = deepcopy(best_choice)
            # path = best_choice

            if sibling not in seen:
                path.append(action, 1, sibling, estimate)
                queue.put((function, path))

                plot_heuristic(axs, values, estimate, frontier, queue.qsize())

    plt.show()
    return None
