#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Stefan Jansen'

from random import randint


count = 0


def partition(seq):
    pi, seq = seq[0], seq[1:]                       # Pick and remove the pivot
    lo = [x for x in seq if x <= pi]                # All the small elements
    hi = [x for x in seq if x > pi]                 # All the large ones
    return lo, pi, hi                               # pi is "in the right place


def quicksort(seq):
    global count
    count += 1
    if len(seq) <= 1: return seq                    # Base case
    lo, pi, hi = partition(seq)                     # pi is in its place
    return quicksort(lo) + [pi] + quicksort(hi)     # Sort lo and hi separately


if __name__ == '__main__':
    seq_length = 20
    seq = [randint(0, seq_length) for _ in range(seq_length)]
    print(seq)
    print(quicksort(seq))
    print(count)
