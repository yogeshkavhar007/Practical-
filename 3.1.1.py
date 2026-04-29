import numpy as np

# write your code here..
row,col=map(int,input().split())

matric=[]

for i in range (row):
	matric.extend(map(int,input().split()))

array=np.array(matric).reshape(row,col)
print(array)
print(array.ndim)
print(array.shape)
print(array.size)
