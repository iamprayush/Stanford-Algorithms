# Version 3.6
import random
from copy import deepcopy

# There will be an adjacency list of the given undirected graph
graph = {}

def minCut(graph):
	'''
	Input: Dictionary containing the adjacency list of the graph
	Output: # of crossing edges after the min-cut
	'''
	while len(graph) > 2:
		# picking vertices of a random edge
		v = random.choice(list(graph.keys()))
		u = random.choice([i for i in graph[v]])

		# merging the two vertices into one
		vl = graph[v]
		ul = graph[u]
		vl.extend(ul)

		# deleting the second vertex
		del graph[u]

		# replacing all occurences of the deleted vertex with v
		for vertex in graph:
			graph[vertex] = [v if vert == u else vert for vert in graph[vertex]]

		# removing self-loops of v
		graph[v] = [vert for vert in graph[v] if vert != v]
		
	# returning the number of crossing edges between the final two sub-graphs
	return len(graph[list(graph.keys())[0]])

minVal = 10**10
iterations = 50
for _ in range(iterations):
	minVal = min(minCut(deepcopy(graph)), minVal)
print(minVal)
