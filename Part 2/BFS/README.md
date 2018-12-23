# Breadth First Search  

Here, I've implemented the simple BFS algorithm and the shortest path finder algorithm, both of which work for an undirected as well as a directed graph.

## 1. BFS Traversal  
**Input:** A directed graph G(V,E) in adjacency list format and the starting vertex.  
**Output:** Prints out all vertices/nodes in BFS traversal.  
BFS traversal is implemented with the help of a LIFO data structure (Queue) in order to keep track of the current vertices.
The idea is very simple: All we're doing is starting with the "start" node, looking at all the neighbours by adding them to the queue on by one. At each insertion of an "unvisited" node in the queue, we look at all it's unvisited neighbours and then finally pop that node out from the queue.
This helps in traversing the graph in a layer-by-layer mehtod.

#### Pseudo Code
```
1 mark s as explored, all other vertices as unexplored
2 Q := a queue data structure, initialized with s
3 while Q is not empty do
4   remove the vertex from the front of Q, call it v
5   for each edge (v, w) in v’s adjacency list do
6     if w is unexplored then
7       mark w as explored
8       add w to the end of Q
```
## 2. Shortest Path  
The main advantage of BFS is, that it garantees the shortest path, unlike other algos, if used to find one.
So, here, I've also implemented the shortest path algo with BFS.
The only addition code-wise is that of the updatind distance at each discovery of a new node.
All we do is keep track of the distances from the start node, which btw has a distance of 0(obviously!), and then use the previously calculated distances to update the distances of the newly found nodes.

#### Pseudo Code
```
1 mark s as explored, all other vertices as unexplored
2 l(s) := 0, l(v) := +1 for every v 6= s
3 Q := a queue data structure, initialized with s
4 while Q is not empty do
5   remove the vertex from the front of Q, call it v
6   for each edge (v, w) in v’s adjacency list do
7     if w is unexplored then
8       mark w as explored
9       l(w) := l(v)+1
10      add w to the end of Q
```

## Running Time  
The running time of both these algorithms is linear in # of nodes and edges. 
This is because there is no repeated counting of nodes in any of these algorithms and we're going through all nodes only once.  

![runtime](http://latex.codecogs.com/gif.latex?%5Cdpi%7B150%7D%20%5Clarge%20O%28m%20&plus;%20n%29)  

m : # of edges and   
n : # of nodes/vertices
