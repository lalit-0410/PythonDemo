import numpy as np

# listA=[1,2,3]
# listB=[1,2,3]
# listC=[1,2,3]

# #1D
# arr=np.array(listA)
# print(arr.shape)
# print(arr.ndim)
# print(arr.size)
# print(arr.dtype)


# #2D
# arr1=np.array([listA,listB])
# print(arr1.shape)
# print(arr1.ndim)
# print(arr1.size)
# print(arr1.dtype)

# #3D
# arr3=np.array([[listA,listB,listC]])
# print(arr3.shape)
# print(arr3.ndim)
# print(arr3.size)
# print(arr3.dtype)

matrix=np.arange(1,26).reshape(5,5)
print(matrix)

print(matrix[-1])# last row

print(matrix[:,0])# first column

print(matrix[:3, :3])# extract 3*3 matrix