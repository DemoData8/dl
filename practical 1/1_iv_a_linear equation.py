# Suppose, a fruit-seller sold 20 mangoes and 10 oranges in one day for a total of $350. The next day he sold 17 mangoes and 22 oranges for $500. If the prices of the fruits remained unchanged on both the days, what was the price of one mango and one orange?
#
# This problem can be easily solved with a system of two linear equations.
#
# Let's say the price of one mango is x and the price of one orange is y. The above problem can be converted like this:
#
# 20x + 10y = 350
# 17x + 22y = 500

import numpy as np

A = np.array([[20, 10], [17, 22]])
B = np.array([350, 500])
R = np.linalg.solve(A,B)
x, y = np.linalg.solve(A,B)

print(R)
print("x =", x)
print("y =", y)

