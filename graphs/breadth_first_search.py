#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'Stefan Jansen'

from collections import deque


def bfs(G, s):
    P, Q = {s: None}, deque([s])        # Parents and FIFO queue
    while Q:
        u = Q.popleft()                 # Constant-time for deque
        for v in G[u]:
            if v in P: continue         # Already has parent
            P[v] = u                    # Reached from u: u is parent
            Q.append(v)
    return P