# -*- coding:utf-8 -*-

L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]

#按姓名排序
def by_name(t):
	return t[0]

L2=sorted(L,key=by_name)
print(L2)

#按成绩排序
def by_score(t):
	return t[1]

L3=sorted(L,key=by_score)
print(L3)