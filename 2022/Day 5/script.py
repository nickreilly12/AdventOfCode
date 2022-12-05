import numpy as np
import re


cratepositions = np.loadtxt("cratepositions.txt",dtype=str, delimiter=" ")

with open('moves.txt','r') as sourcefile:
    moves = [x for x in sourcefile.read().split("\n")]

for x in moves:
    res = [int(i) for i in x.split() if i.isdigit()]
    mv = res[0]
    fm = res[1]
    to = res[2]
    print(mv)
    print(fm)
    print(to)