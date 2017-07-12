# coding=utf-8
"""
Created on 2017-07-07

@Filename: deque
@Author: Gui


"""
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)

if __name__ == '__main__':
    with open(r'schemas.js') as f:
        for line, prevlines in search(f, 'find', 5):
            for pline in prevlines:
                print(pline, end=' ')
            print(line, end=' ')
            print('-' * 20)