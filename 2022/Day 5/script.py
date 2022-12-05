import numpy as np
import re

cratepositions = np.loadtxt("cratepositions.txt",dtype=str, delimiter=" ")

with open('moves.txt','r') as sourcefile:
    moves = [x for x in sourcefile.read().split("\n")]

for x in moves:
    item = re.search('move(\d+)', x)
    start = re.search('from(\d+)', x)
    finish = re.search('to(\d+', x)
    print(item)
    print(start)
    print(finish)
    import pdb;pdb.set_trace()
