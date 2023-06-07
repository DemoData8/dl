import numpy as np
import matplotlib.pyplot as plt

u = np.array([1,6])
print(u)
v = np.array([4,2])
print(v)

manhatan_norm = np.linalg.norm(u+v)
print("Manhattan Norm")
print(manhatan_norm)

