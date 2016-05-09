#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'Stefan Jansen'


def traverse_component(G, s, S=set()):
    """Traverse graph from node s, possibly avoiding nodes in S."""

    P, Q = dict(), set()                    # Predecessors + 'to do' queue
    P[s] = None                             # s has no predecessor
    Q.add(s)                                # add s to 'to do' queue
    while Q:                                # nodes on 'to do' list
        u = Q.pop()                         # pick arbitrary node
        for v in G[u].difference(P, S):     # new nodes besides predecessors and black list?
            Q.add(v)                        # add new nodes to 'to do' queue
            P[v] = u                        # record predecessor
    return P                                # traversal tree


def components(G):
    """Find connected components in graph G"""
    comp = []
    seen = set()                            # nodes already seen
    for u in G:                             # try every starting point
        if u in seen: continue              # ignore if seen
        C = traverse_component(G, u)        # traverse component
        seen.update(C)                      # add nodes of new traversal tree to seen
        comp.append(C)                      # collect the components
    return comp


def tr(G): # Transpose (rev. edges of) G
"""Kosaraju’s Algorithm for Finding Strongly Connected Components"""
    GT = {}
    for u in G: GT[u] = set() # Get all the nodes in there
    for u in G:
    for v in G[u]:
    GT[v].add(u) # Add all reverse edges
    return GT
    def scc(G):
    GT = tr(G) # Get the transposed graph
    sccs, seen = [], set()
    for u in dfs_topsort(G): # DFS starting points
    if u in seen: continue # Ignore covered nodes
    C = walk(GT, u, seen) # Don't go "backward" (seen)
    seen.update(C) # We've now seen C
    sccs.append(C)
    return sccs