# -*- conding:utf-8 -*-
def trim(s):
	if len(s)==0:
		return s
	elif s[0]==' ':
		return trim(s[1:])
	elif s[-1]==' ':
		return trim(s[:-1])
	return s

print(trim(' Hello World '))
print(trim('Hello World  '))
print(trim('    Hello'))
print(trim('Hello    World'))