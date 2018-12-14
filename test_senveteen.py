# -*- conding:utf-8 -*-

def add_end(L=[]):
	L.append('END')
	return L
	
print(add_end([1,2,3]))
print(add_end())

def calc(number):
	sum=0;
	for n in number:
		sum=sum+n*n
	return sum
print(calc([1,2,3]))

def calc(*number):
	sum=0;
	for n in number:
		sum=sum+n*n
	return sum
print(calc(1,2,3,5))
nums=[1,2,3]
print(calc(*nums))

