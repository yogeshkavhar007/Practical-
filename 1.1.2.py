#write your code here...
import math
n=int(input())
if (1<n<=9):
	print(n*n)
elif(10<n<99):
	p=n **(0.5)
	print(f"{p:.2f}")
elif(100<n<999):
     m=n **(1/3)
     print(f"{m:.2f}")
else :
     print("Invalid")
