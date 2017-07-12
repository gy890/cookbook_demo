# coding=utf-8
"""
Created on 2017-07-10

@Filename: singleton_demo
@Author: Gui


"""


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super.__init__(*args, **kwargs)

    def __class__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class Spam(metaclass=Singleton):
    def __index__(self):
        print('Creating Spam')