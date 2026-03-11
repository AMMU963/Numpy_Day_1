''' 
both converts from multi dim to 1d 
.ravel -->return a view 
.flatten -->returns a copy

'''
import numpy as np

a1=np.arange(0,20,2).reshape((2,5))
print(a1)
print(a1.ravel())
print(a1.flatten())


a2=np.array([[1,2,3,4],[6,7,8,9]])
print(a2)

r=a2.ravel()
f=a2.flatten()

print(a2)
print(r)
print(f)

a2[0,0]=20

print(a2)
print(r)
print(f)






