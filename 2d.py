#two dimensional array
#all elements will store in one subscript only

import numpy as np

a1=np.array([[1,2,3],[4,5,6]])
print(a1)

a2=np.array([[1,2,3],[3,4,5],[5,6,7]])
print(a2)


#indexing
print(a1[1,2])
print(a2[2,1])  #(row,column)


#slicing
print(a1[0:2:,0:2:])  #row is for first comma ,next column
print(a1[::-1,::-1])
print(a2[::-1,::-1])

print(np.ndim(a2))
print(a2.shape)
print(a2.size)
print(a2.itemsize)

