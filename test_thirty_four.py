# -*- coding:utf-8 -*-
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
	nn=str(n)
	return nn==nn[::-1]
print(list(filter(is_palindrome,range(1,1000))))