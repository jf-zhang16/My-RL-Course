from grid import Grid
import numpy as np

# state-values predicted by first view Monte Carlo
play = Grid()
iterations = 10
values = np.zeros((4, 4))
returns = {(i, j): list() for i in range(4) for j in range(4)}
deltas = {(i, j): list() for i in range(4) for j in range(4)}
gamma = 0.9

for a in range(iterations):
    episode = play.generate_episode()
    G = 0
    for i, step in enumerate(episode[::-1]):
        # episode = []  # episode contains [s0, action0, reward1,s1, s1, action1],...[sT-1, actionT-1, final_reward, sT]
        G = gamma*G + step[2]
        if step[0] not in [x[0] for x in episode[::-1][i+1:]]:
            idx = (step[0][0], step[0][1])
            returns[idx].append(G)
            newValue = np.average(returns[idx])
            deltas[idx[0], idx[1]].append(np.abs(values[idx[0], idx[1]]-newValue))
            values[idx[0], idx[1]] = newValue
        # else:

