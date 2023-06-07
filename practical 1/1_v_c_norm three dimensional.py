# import library
import numpy as np

# initialize matrix
threed = np.array([[[ 1, 2, 3],
         [4, 5, 6]],[[ 11, 12, 13],
         [14, 15, 16]]])

# compute norm of matrix
mink_norm = np.linalg.norm(threed)

print("Minkowski norm:")
print(mink_norm)
