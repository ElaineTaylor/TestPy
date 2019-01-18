# -*- coding:utf-8 -*-

from collections import Iterator
print(isinstance((x for x in range(10)),Iterator))
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('abc',Iterator))
print(isinstance(iter([]),Iterator))
print(isinstance(iter('abc'),Iterator))