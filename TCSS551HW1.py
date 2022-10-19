import numpy as np

"""
n=0
print(" ".join([str(n-i) for i in range(n)]))

def median(list):
    sortedList = sorted(list)
    if len(sortedList) % 2 == 1:
        return sortedList[int(len(sortedList) / 2)]
    else:
        return (sortedList[int(len(sortedList) / 2)] + sortedList[int(len(sortedList) / 2) -1]) / 2

print(median([1, 2, 3, 4]))
"""
u = np.linspace(1.5 * np.pi, -1.5 * np.pi, 32)
# Creates a list of 100 points from 1.5pi to -1.5pi in descending order
[x, y] = np.meshgrid(u, u)

print(x.flatten())

z = [1] * 5
z = np.array(z)

print(z.shape)

twice_identity = np.zeros((50,50))
rows = np.array(range(0,50))
cols = np.array(range(0,50))
twice_identity[rows, cols] = 2
print(twice_identity)
