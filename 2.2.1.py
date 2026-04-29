m=list(map(int,input().split()))
n=int(input())
if n in m :
	print(m.index(n))
else :
	print("Not found")
