#Solution to project euler Problem 15 in python
# learning python graph libraries starting with networkx
# Yes, pen and paper would work, but i wanna learn python ;-)
# easy install networkx

#The 20x20 grid is modeled as an graph. 21 edges per line

import networkx as nx

targetNode = 21*21
foundRoutes = 0
def buildGraph():
	G=nx.Graph()

	for x in range (0,21*21):
		if (x % 21):
			G.add_edge(x ,x+1)
		if (x>0 and x <= 420):
			G.add_edge( x, x+21)
			
	G.add_edge(0,1)
	G.add_edge(0,22)
	return G
	

G=buildGraph()



def run (currentNode, backtrack, numSteps):
	global foundRoutes
	backtrack.append(currentNode)
	numSteps+=1
#	print currentNode, numSteps, len(backtrack)
	if (currentNode == targetNode):
		foundRoutes+=1
		print "found a route"
		return
	for x in G.neighbors(currentNode):
		if (not backtrack.__contains__(x)):
			run(x,backtrack,numSteps)
	backtrack.remove(currentNode)
	return

backtrack = []
run(0,backtrack,0)