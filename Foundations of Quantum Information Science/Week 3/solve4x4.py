import numpy as np
from qis101_utils import as_latex


#Solve 4x4 matrix program

matrix = np.array([[1, 2, -1,-1], [3, 2, 4, 4], [4, 4, 3, 4],[2,0,1,5]])
vals = np.array([5, 15, 22, 15])
sol = np.linalg.solve(matrix, vals)
print(sol)