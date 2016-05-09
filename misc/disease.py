#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Stefan Jansen'

import numpy as np


def neighbors(x, y):
    return [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]


def infect(matrix, start_x, start_y, strength):
    n, m = matrix.shape

    if start_x in [-1, n] or start_y in [-1, m]:
        return matrix
    elif matrix[start_x, start_y] < strength:
        matrix[start_x, start_y] = np.nan # np.nan compares as inf
        for neighbor in neighbors(start_x, start_y):
            matrix = infect(matrix, *neighbor, strength)
    return matrix


size = 10
midpoint = size // 2
matrix = np.random.randint(low=1, high=10, size=(size, size)).astype(float)
print(np.array(matrix))

strength = matrix[midpoint, midpoint] + 1 # so there are infections
print('\nstrenght:', strength, '\n')

print(infect(matrix, midpoint, midpoint, strength))
