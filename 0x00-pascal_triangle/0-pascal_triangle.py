#!/usr/bin/python3
"""
Pascal triangle implementation
"""


def pascal_triangle(n):
    """Pascal triangle implementation"""
    pascal = []
    if n <= 0:
        return pascal
    else:
        for x in range(n):
            new_list = [1]
            if pascal:
                prev_list = pascal[-1]
                for i in range(len(prev_list) - 1):
                    new_list.append(prev_list[i] + prev_list[i + 1])
                new_list.append(1)
            pascal.append(new_list)
    return pascal
