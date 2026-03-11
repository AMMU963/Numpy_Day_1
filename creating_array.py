'''
-->np.array()
   simply by passing list and dtype
-->np.asarray()  with nditer()
   list,dtype,order=F(rows),C(columns)
   to see the dif we use np.nditer(array_name)
-->frombuffer()
   to cnvert string to array
   while creating string we should use b and 
   dtype,offset,count
   entire string can be converted into one element
-->fromiter()
  used for genratoras and iterators

'''
import numpy as np

#using asarray(list,dtype,order=C,F)for fid we should use nditer()
a1=np.asarray([[1,2,3,4],[5,6,7,8]],dtype=float,order='C')
print(a1)
for i in np.nditer(a1):
    print(i)

a2=np.asarray([[1,2,3,4],[5,6,7,8]],dtype=int,order='F')
print(a2)
for i in np.nditer(a2):
    print(i)



#frombuffer
s1=b"vikhitha"
a2=np.frombuffer(s1,dtype='S1')
print(a2)

s1='vikhitha'  #from list also we can convert lsit to array
a3=np.array(list(s1))
print(a3)

s1=b"vikhitha"
a2=np.frombuffer(s1,dtype='S1',offset=3,count=2)
print(a2)











