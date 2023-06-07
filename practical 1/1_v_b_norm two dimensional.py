# import library
import numpy as np

# initialize matrix
twod = np.array([[ 1, 2, 3],
         [4, 5, 6]])

# compute norm of matrix
eucl_norm = np.linalg.norm(twod)

print("Euclidean norm:")
print(eucl_norm)
