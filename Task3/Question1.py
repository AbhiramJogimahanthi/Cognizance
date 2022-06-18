import numpy as np
Z = np.array([10,11,12,13,14])
z = 5
N = np.zeros(len(Z) + (len(Z)-1)*(z))
N[::z+1] = Z
print(N)