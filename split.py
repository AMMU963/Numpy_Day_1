'''
np.split()
-->equal

np.hsplit()
np.vsplit()
np.dsplit()  #array must be 3D

'''
import numpy as np 

a1=np.array([1,2,3,4])
print(np.split(a1,2))

a2=np.array([[1,2,3],[4,5,6]])
print(np.split(a2,2))


#print(np.vsplit(a2,3)) return value eror
print(np.vsplit(a2,2))
print(np.hsplit(a2,3))

a3=np.array([[10,20,30],[40,50,60]])
a4=np.dstack((a2,a3))
print(a4)

print(a4.ndim)
print(np.dsplit(a4,2))