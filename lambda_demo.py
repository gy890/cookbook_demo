# coding=utf-8
"""
Created on 2017-07-07

@Filename: lambda_demo
@Author: Gui


"""
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y

print(a(10))
print(b(10))