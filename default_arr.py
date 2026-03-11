#with default values

import numpy as np
#with zeros
a1=np.zeros((3))
a2=np.zeros((2,3))
a3=np.zeros((2,3,3))

print(a1)
print(a1.shape)

print(a2)
print(a2.shape)

print(a3)
print(a3.shape)

#with ones

a1=np.ones((3))
a2=np.ones((2,3))
a3=np.ones((2,3,3))

print(a1)
print(a1.shape)

print(a2)
print(a2.shape)

print(a3)
print(a3.shape)

#with our wish elemet
a1=np.full((3),2)
a2=np.full((2,3),4)
a3=np.full((2,3,3),5)

print(a1)
print(a1.shape)

print(a2)
print(a2.shape)

print(a3)
print(a3.shape)

#for diagonal filling
a1=np.eye(3)  #only one arg is enough
a2=np.eye(2)
a3=np.eye(1)

print(a1)
print(a2)
print(a3)