# -*- coding:utf-8 -*-
def person(name ,age, **kw):
	print('name',name,'age' ,age,'other',kw)

person('Elaine',25)
person('Taylor',28,city='New York')
person('swift',30,city='New York',job='singer')

extra={'city':'Beijing','job':'writer'}
person('Jack',26,**extra)

def person1(name,age,**kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name:',name, 'age:',age,'other:',kw)

person1('Bob',26,city='Shanghai',addr='changsha',zip=123456)

def person2(name,age,*,city,job):
	print('name',name,'age',age,city,job)
	
person2('Jackee',24,city='Guangzhou',job='Engineer')


	

