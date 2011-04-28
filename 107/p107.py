#!/usr/local/bin/python2.7
# encoding: utf-8
"""

Created by Matthias Grawinkel on 2011-04-24.
"""

import networkx as nx
import matplotlib.pyplot as plt

def getWeight(graph):
    sum = 0
    for edge in graph.edges():
        sum+= graph[edge[0]][edge[1]]['weight']
    return sum

network=[]
f = open('network.txt','r')
for row in f.readlines():
    elements = row.strip().split(',')
    network.append(elements)
G=nx.Graph()
for x in xrange(len(network)):
    for y in xrange(len(network[x])):
        val = network[x][y]
        if val != '-':
            # print x,y,val
            G.add_edge(x,y,weight=int(val))

GS=nx.minimum_spanning_tree(G)

print "Result: %d" % (getWeight(G) - getWeight(GS))
