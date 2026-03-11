import numpy as np

a1=np.array([1,2,3,4])
a2=np.array([[1,2,3],[4,5,6]])

#for shape
print(a1.shape)
print(a2.shape)

#for type
print(type(a1))
print(type(a2))

#for dim
print(a1.ndim)
print(a2.ndim)

#for total number of elements
print(a1.size)
print(a2.size)

#for reshaping the array
print(a2.shape)
print(a2.reshape(3,2)) 

'''
after reshaping elements must be equal 
before and after

'''

#for dtype (dtype of element in array)
print(a1.dtype)

#bytes for each element
print(a1.itemsize)

#for total memory used
print(a1.nbytes)