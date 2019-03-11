import numpy as np
number_2d = np.array([[1,2,4,4], [3,2,3,1]])
print(number_2d)
print("shape",number_2d.shape)
print("thay doi kich thuoc mang 2x4 -> 2x2x2")
number_3d = number_2d.reshape(2,2,2)
print(number_3d)
print("shape",number_3d.shape)

print("tao ra mng 3 x 3 x 3 ngau nhien")
numbers = np.random.randint(low=12,size=(3,3,3))
print(numbers)
# duoi ve mang 1 chieu
print("duoi mang 1 chieu")
flatten_numbers = numbers.flatten()
print("mang sau khi duoc doi ra boi flatten")
print(flatten_numbers)
#mo rong dong
print("mo rong dong, tu 1 mang number_2d 2x4 ben tren -> 2x1x4 (1 = axis)")
number_3d_axis_1 = np.expand_dims(number_2d,axis=1)
print(number_3d_axis_1)
print(number_3d_axis_1.shape)
#giam chieu cua mang
print("tao ra number-3d")
number_3d = np.random.randint(12,size=(1,2,2))
print(number_3d)
print("giam chieu cua number-3d")
number_2d_axis_0 = np.squeeze(number_3d, axis=0)
print(number_2d_axis_0)
print(number_2d_axis_0.shape)

#chuyen vi
print("tao ra ma tran chuyen vi cua number_2d")
number_2d_transpose = number_2d.T
print(number_2d_transpose)