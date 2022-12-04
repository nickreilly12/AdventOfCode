import numpy as np

with open('data', 'r') as sourcefile:
    data = [x for x in sourcefile.read().split()]

N = len(data[0])