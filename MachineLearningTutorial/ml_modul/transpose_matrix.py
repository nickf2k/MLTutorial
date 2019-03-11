import numpy as np
number_2d = np.array([[1,2,4,4], [3,2,3,1]])
print(number_2d)
print("shape",number_2d.shape)
number_3d = number_2d.reshape(2,2,2)
print(number_3d)
print("shape",number_3d.shape)
