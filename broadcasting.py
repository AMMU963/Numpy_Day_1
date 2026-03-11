import numpy as np

'''
numpy automatically reshape or extend the array to
perform mathematical operation

'''
prices=np.array([100,200,300])
discount=10

final_prices=prices-(prices * discount/100)

print(final_prices)


#witthout array
prices=[100,200,300]
discount=10
final_prices=[]

for i in prices:
    f_p=i-(i*(discount//100))
    final_prices.append(f_p)

print(final_prices)

'''
--> if dim matches it simply do the op
--> if not it extend
--> for incompatible shapes  throws value error

'''
arr1=np.array([1,2,3])
arr2=np.array([10,20,30])
print(arr1+arr2)

arr3=np.array(100)
print(arr1+arr3)  #100 ia addaed to every element in arr1


a1=np.array([1,2,3])
a2=np.array([[1,2,3],[4,5,6]])
print(a1+a2)

a3=np.array([1,2])
#print(a1+a3)    value error 



