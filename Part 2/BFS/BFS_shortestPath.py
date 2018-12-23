from queue import Queue
from math import inf

def dist(graph, start, end):
    '''
    Input: A graph in adjacency list format, starting and ending vertex
    Output: An integer denoting the shortest distance from the given start and end vertices
    '''

    # Initializing the explored set with the start vertex
    # Using set for more efficient retrieval
    explored = set([start])

    # initiazing all distances except start with infinity
    distances = {}
    for key in list(graph.keys()):
        if key == start: distances[key] = 0
        else:   distances[key] = inf

    # Rest is same as BFS with a little addition for updating the distance for each discovered node
    q = Queue()
    q.put(start)
    while not q.empty():
        v = q.get()
        for w in graph[v]:
            if w not in explored:
                explored.add(w)
                distances[w] = distances[v] + 1    # Updating distance of a new node based on dist of parent node
                q.put(w)
    return distances[end]
