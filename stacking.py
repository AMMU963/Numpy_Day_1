'''
vertically
horizontally

vstack() -->up and down
hstack() --> side by side
dstack() -->creates a 3D array from 1D array and 2D array

'''
import numpy as np

#1D
a1=np.array([1,2,3])
a2=np.array([4,5,6])

print(np.vstack((a1,a2)))
print(np.hstack((a1,a2)))

print(np.dstack((a1,a2)))

#2D
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[10,20,30],[40,50,60]])

print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))

print(np.dstack((arr1,arr2)))
