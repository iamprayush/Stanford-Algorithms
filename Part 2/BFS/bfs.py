from queue import Queue

def bfs(graph, start):
    '''
    Input: A graph in adjacency list format and a starting vertex.
    Output: Prints vertices in BFS traversal.
    '''

    # Initializing the explored set with the start vertex
    # Using set for more efficient retrieval
    explored = {start}

    # Initializing the queue with the start vertex
    q = Queue()
    q.put(start)
    print(start)
    
    # Exactly like the pseudo-code!
    while not q.empty():
        v = q.get()
        for w in graph[v]:
            if w not in explored:
                print(w)
                explored.add(w)
                q.put(w)
