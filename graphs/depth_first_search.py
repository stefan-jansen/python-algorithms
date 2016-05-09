#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'Stefan Jansen'


def recursive_dfs(G, s, S=None):
    if S is None: S = set()         # Initialize the history
    S.add(s)                        # We've visited s
    for u in G[s]:                  # Explore neighbors
        if u in S: continue         # Already visited: Skip
        recursive_dfs(G, u, S)      # New: Explore recursively


def iterative_dfs(G, s):
    S, Q = set(), []                # Visited-set and queue
    Q.append(s)                     # We plan on visiting s
    while Q:                        # Planned nodes left?
        u = Q.pop()                 # Get one
        if u in S: continue         # Already visited? Skip it
        S.add(u)                    # We've visited it now
        Q.extend(G[u])              # Schedule all neighbors
        yield u                     # Report u as visited


def timed_dfs(G, s, d, f, S=None, t=0):
    """Depth-First Search with Timestamps"""

    if S is None: S = set()         # Initialize the history
    d[s] = t; t += 1                # Set discover time
    S.add(s)                        # We've visited s
    for u in G[s]:                  # Explore neighbors
        if u in S: continue         # Already visited. Skip
        t = dfs(G, u, d, f, S, t)   # Recurse; update timestamp
    f[s] = t; t += 1                # Set finish time
    return t                        # Return timestamp


class stack(list):
    """Subclass list for custom stack implementation"""
    add = list.append


def graph_traversal(G, s, qtype=stack):
    """General graph traversal using list-based stack"""

    S, Q = set(), qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in S: continue
        S.add(u)
        for v in G[u]:
            Q.add(v)
        yield u



def iterative_deepening_dfs(G, s):
    yielded = set()                             # Visited for the first time

    def recurse(G, s, d, S=None):               # Depth-limited DFS
        if s not in yielded:
            yield s
            yielded.add(s)
        if d == 0: return                       # Max depth zero: Backtrack
        if S is None: S = set()
        S.add(s)
        for u in G[s]:
            if u in S: continue
            for v in recurse(G, u, d-1, S):     # Recurse with depth-1
                yield v
    n = len(G)
    for d in range(n):                          # Try all depths 0..V-1
        if len(yielded) == n: break             # All nodes seen?
    for u in recurse(G, s, d):
        yield u


if __name__ == '__main__':
    a, b, c, d, e, f, g, h = range(8)
    N = [
        [b, c, d, e, f],        # a
        [c, e],                 # b
        [d],                    # c
        [e],                    # d
        [f],                    # e
        [c, g, h],              # f
        [f, h],                 # g
        [f, g]                  # h
    ]

    print(list(iterative_dfs(N, N[0][0])))
