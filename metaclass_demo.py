# coding=utf-8
"""
Created on 2017-07-10

@Filename: metaclass_demo
@Author: Gui


"""


class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError('Cannot instantiate directly')


class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(k):
        print('Spam.grok')

Spam.grok(42)
s = Spam()
