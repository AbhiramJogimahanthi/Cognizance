import numpy as np
dim = int(input("Enter the dimension of identitiy matrix: "))
matrix = np.identity(dim, dtype="int")
print(matrix)