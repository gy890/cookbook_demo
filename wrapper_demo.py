# coding=utf-8
"""
Created on 2017-07-10

@Filename: wrapper_demo
@Author: Gui


"""
import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper
