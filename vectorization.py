l1=[1,2,3,4]
l2=[5,6,7,8]

add=[x+y for x,y in zip(l1,l2)]
print(add)

import numpy as np 

a1=np.array([1,2,3,4])  #this is vectorization 
a2=np.array([5,6,7,8])
print(a1+a2)


print(a1*a2)

'''
main difference between vectorization and broadcasting 
is 
broadcasting                 vectorization
-expands shape                 -replaces loops
-op on diiferent shapes        -op avoiding loops
-shape compatibility           -speed and simplicity
-nump arth and func            -libraries



