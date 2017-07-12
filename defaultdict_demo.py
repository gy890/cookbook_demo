# coding=utf-8
"""
Created on 2017-07-07

@Filename: defaultdict_demo
@Author: Gui


"""
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)