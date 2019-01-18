# -*- coding:utf-8 -*-
def f(x):
	return x*x
r=map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))
str=map(str,[1,2,3,4,5,6,7,8,9])
print(list(str))


from functools import reduce
def add(x,y):
	return x+y
print(reduce(add,[1,3,5,7,9]))

def add(x,y):
	return x*10+y
print(reduce(add,[1,3,5,7,9]))

DIGITS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def str2int(s):
	def fn(x,y):
		return x*10 +y
	def char2num(s):
		return DIGITS[s]
	return reduce(fn,map(char2num,s))
	
print(str2int(DIGITS))