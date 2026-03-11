import numpy as np 

'''
append 
will add at the end

'''
a1=np.array([1,2,3])
a2=np.append(a1,4)
print(a2)

a3=np.append(a1,[5,6,7,8])
print(a3)

print(np.append(a1,a2))
