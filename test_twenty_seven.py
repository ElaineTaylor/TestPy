# -*- coding:utf-8 -*-
def triangles():
	nMax=9
	n=0
	L=[1]
	while n<nMax:
		if(n==0):
			yield L
		elif(n==1):
			L.append(1)
			yield L
		else:
			num=0
			while num<n:
				data=L(n-num-2)+L(n-num-1)
				L.append(data)
			yield L
		n=n+1


for n1 in triangles():
	print(n1)

