import numpy as np

a1=np.arange(0,20,2)
print(a1)

print(len(a1))

#after reshaping also same elements 
print(a1.reshape((2,5)))  #returns view 
