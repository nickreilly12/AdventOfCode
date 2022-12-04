import numpy as np

lines = np.loadtxt('data', 'U')
bits = int(len(lines[0]))
data = lines.view('U1').astype(int).reshape(lines.shape[0],bits)

print(data)