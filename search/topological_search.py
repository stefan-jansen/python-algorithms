#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'Stefan Jansen'


def dfs_topological_sort(G):
    S, res = set(), []          # History and result
    def recurse(u):             # Traversal subroutine
        if u in S: return       # Ignore visited nodes
        S.add(u)                # Otherwise: Add to history
        for v in G[u]:
            recurse(v)          # Recurse through neighbors
        res.append(u)           # Append u after traversal to list (in scope)
    for u in G:
        recurse(u)              # Cover entire graph
    res.reverse()               # It's all backward so far
    return res


