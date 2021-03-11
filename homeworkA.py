import numpy as np


class Grid:
    def __init__(self, start_state):
        """
        :param start_state: is the initial state which is a list
        """
        self.dimension = 4
        self.state = start_state
        self.terminate = [3, 3]
        self.motions = []

    def reward(self):
        if self.state == self.terminate:
            return 9
        else:
            return -1

    def step(self):






