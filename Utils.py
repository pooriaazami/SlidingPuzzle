class Path:
    def __init__(self):
        self.__actions = []
        self.__terminal = None
        self.__cost = 0
        self.__estimate = 0

    def append(self, action, cost, last_state, estimate):
        self.__actions.append(action)
        self.__cost += cost
        self.__terminal = last_state
        self.__estimate = estimate

    @property
    def steps(self):
        return self.__actions

    @property
    def cost(self):
        return self.__cost

    def show(self):
        for action in self.__actions:
            print(action)

    @property
    def terminal(self):
        return self.__terminal

    @property
    def heuristic_value(self):
        return self.__estimate

    @property
    def estimate(self):
        return self.__cost + self.__estimate

    def __eq__(self, other):
        other_actions = other.steps

        if len(other_actions) != len(self.__actions):
            return False

        for i in range(len(self.__actions)):
            if self.__actions[i] != other_actions[i]:
                return False
        return True

    def __ne__(self, other):
        return self.estimate != other.estimate

    def __lt__(self, other):
        return self.estimate < other.estimate

    def __gt__(self, other):
        return self.estimate > other.estimate

    def __le__(self, other):
        return self.estimate <= other.estimate

    def __ge__(self, other):
        return self.estimate >= other.estimate
