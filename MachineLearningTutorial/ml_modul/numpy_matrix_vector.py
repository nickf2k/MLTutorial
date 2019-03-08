import numpy as np

number_vector = np.array([1, 2, 3])
print("number vector: ")
print(number_vector)
print("shape of number_vector ")
print(number_vector.shape)

two_direction_matrix = np.array([[1, 3, -2], [3, 5, 4]])
print("number matrix 2d: ")
print(two_direction_matrix)
print("shape of number matrix 2d ")
print(two_direction_matrix.shape)

three_direction_matrix = np.array([[[3, 2, -1], [3, 5, 7]], [[7, 2, 2], [3, 4, -1]]])
print("number matrix 3d: ")
print(three_direction_matrix)
print("shape of matrix 3d ")
print(three_direction_matrix.shape)

'create special matrix '
number_1D_zeros = np.zeros((3,), int)  # tao ra mang 1 chieu cua cac so int
print("number_1d_zeros: ")
print(number_1D_zeros)

number_2D_ones = np.ones((2, 3), float)  # tao ra ma tran 2x3 cac so float la 1
print("number_2d_ones: ")
print(number_2D_ones)

number_3D_full = np.full((3, 2, 3), 7)  # tao ra mang 3 chieu 3x2x3 toan so 7
print("number_3D_full:")
print(number_3D_full)

number_eye = np.eye(5, dtype=int)  # tao ra ma tran don vi 5x5
print("number_eye:")
print(number_eye)

number_1D_arange = np.arange(3, 20, 2, int)  # tao ra vector cap so cong
print("number 1D arange: ")
print(number_1D_arange)

number_2D_random = np.random.random_sample((4, 3))
print("number_2D_random")
print(number_2D_random)

number_2D_random_int = np.random.randint(low=12, high=30, size=(3, 2),
                                         dtype=int)  # tao ra vector co cac gia tri tu low den high
print("number_2D_random_int")
print(number_2D_random_int)

