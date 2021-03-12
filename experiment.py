import numpy as np

# part of reverse
# a = [[[2, 1], [1, 0], -1, [3, 1]], [[3, 1], [0, -1], -1, [3, 0]], [[2, 0], [-1, 0], -1, [2, 0]], [[2, 0], [-1, 0], -1, [1, 0]]]
# print(len(a))
# print(a[::-1])
# print(a[::-1][0][0])
# print(a[::-1][1][0])
# print(a[::-1][2][0])
# print(a[::-1][3][0])
# print("The experiment begins")
# for i, step in enumerate(a[::-1]):
#     if step[0] not in [x[0] for x in a[::-1][i+1:]]:
#         print(f"i is {i}")
#         print(f"step[0] is {step[0]}")
#         idx = (step[0][0], step[0][1])
#         print(f"idx is {idx}")
#         print(f"step[0][0] is {step[0][0]}")
#     else:
#         print(f"i is {i}")
#         print(f"{step[0]} has appeared")

# part of average
alist = np.array([1, 2, 3, 4, 5, 6])
print(alist)
print(np.average(alist))



