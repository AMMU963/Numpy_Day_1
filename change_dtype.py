import numpy as np

'''
astype is used to change the dtype of element
 in array

syntax--> array_name.astype(type of data u want to convert)

'''

a1=np.array([[1,2,3],[4,5,6]])
print(a1)
print(a1.dtype)

f_a1=a1.astype(float)
print(f_a1)
print(f_a1.dtype)