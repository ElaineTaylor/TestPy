# -*- coding:utf-8 -*-
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
	return name[0].upper()+name[1:].lower()
L1=['adam', 'LISA', 'barT']
print(list(map(normalize,L1)))

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
from functools import reduce
def prob(L):
	return reduce(product,L)

def product(x,y):
	return x*y
print(prob([9,3,5,7]))

