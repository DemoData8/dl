import numpy as np

# Define matrix x
x = np.array([[0, 1, 1],
              [1, 1, 0],
              [1, 0, 1]])

# Define vector y
y = [3.65, 1.55, 3.42]

# Solve the system of linear equations
scalars = np.linalg.solve(x, y)

# Print the scalars
print(scalars)
