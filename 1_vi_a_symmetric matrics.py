# Linear Algebra Learning Sequence
# Transpose using different Method

import numpy as np

M = np.array([[2,3,4], [3,45,8], [4,8,78]])
print("---Matrix M---\n", M)

# Transposing the Matrix M
print('\n\nTranspose as M.T----\n', M.T)

if M.T.all() == M.all():
    print("--------> Transpose is equal to M!! -----> It is a Symmetric Matrix")
else:
    print("---------> Transpose is not equal o M!! ------> It is not a Symmetric Matrix")
