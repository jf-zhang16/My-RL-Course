import numpy as np

class Cleaner:
    def __init__(self):
        self.actions = ['up', 'down', 'left', 'right']
        self.neighbor_actions1 = {'up': 'right', 'down': 'left', 'right': 'down', 'left': 'up'}
        self.neighbor_actions2 = {'up': 'left', 'down': 'right', 'right': 'up', 'left': 'down'}

    def get_action(self):
        """
        this function chooses the random action
        :return: the chosen action
        """
        random_action = np.random.choice(self.actions)
        p = np.random.random()
        if p < 0.8:
            return random_action
        elif 0.8<= p < 0.9:
            return self.neighbor_actions1[random_action]
        else:
            return self.neighbor_actions2[random_action]


    def reset(self):



