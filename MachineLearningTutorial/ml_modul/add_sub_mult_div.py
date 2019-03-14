import numpy as np
#add
a = np.array([[1,2,3],[3,4,5]])
b = np.array([[3,4,5],[4,5,6]])
print(a+b)
print(np.add(a,b)) #another way
print("------------")
#multiply
a = np.array([[3,4,5],[2,1,1]])  #2x3
b = np.array([[3,1],[2,1],[3,2]])  #3x2
print(a.dot(b))
print(np.dot(a,b))  #another way
print("-------------")
print("vec x vec = scalar")
a = np.array([1,3,4])
b = np.array([3,2,2])
print(np.inner(a,b))
print("-------------")
print("tensordot")
a = np.array([[1,2,3],[3,4,5]])  #2x3
b = np.array([[3,1,1],[4,2,1]])  #2x3
print(np.tensordot(a,b))