#Problem 18

#learning python networkx, the graph construction was fun, 
#the actual calculation the quickest and dirtiest way possible. 
#Brainpower is delayed to Problem 67.

import networkx as nx

def getTriangle():
    values=[]
    t=open('problem18triangle.txt','r')
    d=0
    for line in t.readlines():
        d+=1
        for n in line.split():
            values.append(n)
    return values,d

def buildgraph(values,d):
    G=nx.DiGraph()
    n=0
    for k in xrange(1,d):
        for o in xrange(0,k):
            G.add_edge(n, (n+k))
            G.add_edge(n, (n+k+1))
            n +=1
    for i in xrange(0,len(values)):
        G.node[i]['value']=int(values[i])
    return G


def findmax(G,n,s):
    global MAX
    # print "dfs, n=%d, sum=%d" % (n,sum)
    s += G.node[n]['value']
    if s > MAX:
        MAX = s
    for x in G.neighbors(n):
        findmax(G,x,s)
    
values,d = getTriangle()
G=buildgraph(values,d)

MAX=0
findmax(G,0,0)
print MAX
    
# for x in xrange(0,len(values)):
#     print "------------"
#     print "Node %d" % (x)
#     print g.node[x]
#     print g.neighbors(x)