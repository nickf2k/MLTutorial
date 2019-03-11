import numpy as np
from numpy import linalg
A = np.array([1,2,3,2,-3,4])
print(linalg.norm(A))  #norm A - ||A||
print(linalg.norm(A, ord=1))  # L1 norm
print(linalg.norm(A, ord=-1)) #test something

