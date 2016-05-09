#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Stefan Jansen'


def bisect_right(a, x, lo=0, hi=None):

    if hi is None:                  # Searching to the end
        hi = len(a)
    while lo < hi:                  # More than one possibility
        mid = (lo + hi) // 2        # Bisect (find midpoint)
        if x < a[mid]: hi = mid     # Value < middle? Go left
        else: lo = mid + 1          # Otherwise: go right
    return lo