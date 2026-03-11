#one dimensional array
import numpy as np
a1=np.array([1,2,3,4,5])

print(a1)

#  Indexing used when we want specific element
print(a1[0])
#print(a1[5]) index out of range
print(a1[4])
print(a1[-1]) #last element  

#slicing(start,stop,step)
#we use : this symbol and comma for rows columns
print(a1[0:3])
print(a1[::-1])
print(a1[3:0:-2])
print(a1[2::-1])