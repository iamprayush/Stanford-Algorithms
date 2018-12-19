# Karger's Random Contraction Algorithm

## Problem: Find Min Cut of a graph
**Input:** An undirected graph G(V,E).  
**Output:** Compute a cut with fewest number of crossing edges.  

Our main goal here, is to divide the given undirected graph into two such that the number of crossing edges is minimum.
A crossing edge maybe defined as an edge with ends on either "sub-graphs", if you will.

A randomized approach to solve this problem was proposed by David Karger in 1993, which is a very elegant and a simple algorithm
which when repeated multiple times (cuz it's randomized) yeilds the desired min cut of the given undirected graph.

This simple algorithm involves iteratively "contracting" random edges in the graph untill you're only left with two vertices.
__That's it!__ The two remaining vertices will be the super-nodes depicting the cut and edges between these two super-nodes will be the 
crossing edges across our "sub-graphs".
Contracting edges involves merging the two nodes that the edge is connected to thereby,
- Eliminating that edge.
- Eliminating self loops that maybe generated in the process.
- Creating the extra parallel edges due to other vertices.

## Pseudo Code
```
while # of super-nodes > 2:
  randomly choose an edge
  contract it into a single vertex
  remove self loops
return cut represented by final 2 super-nodes
```
## Analysis

Now, this is a relatively straightforward algorithm; all we're doing is choosing random edges and contracting them, so it's 
kinda hard to believe that this might have a decent chance of giving the right answer. To see this, we must find the probabilty
of success of this algo. 
Intuitively, one can think of this with the notion that to find the min-cut (considering just one instance of the many possible
min-cuts), we'd have to avoid contracting the edges which will eventually serve as the crossing edges between the "sub-graphs".
Say there are k crossing edges in the final graphs, then at every iteration, we just need to avoid these k edges.
So, we just need to find:  

![prob_eqn](http://latex.codecogs.com/gif.latex?%5Clarge%20P%28%5Cneg%20S_%7B1%7D%20%5Ccap%20%5Cneg%20S_%7B2%7D%20%5Ccap%20%5Cneg%20S_%7B3%7D%20%5Ccap%20...%29)  
where S<sub>i</sub> is the event of choosing one of the k edges on iteration i.  
After some conditional probabilty and some super-satisfying cancellation of terms, this turns out to be equal to atleast **1/n<sup>2</sup>**.
This seems like an incredibly low chance that we __WON'T__ pick one of the k crossing edges, and it is.
But it is better than brute force which would require 2<sup>n</sup> iterations! Plus, with repeated trials, we can improve this probabilty.

With **n<sup>2</sup>** trails, prob of failure reduces to **1/e**, and with **n<sup>2</sup>logn** trials, to **1/n**.  
So finally, the running time of this algortithm turns out to be (n:# of vertices, m:# of edges):  

![rtime1](http://latex.codecogs.com/gif.latex?%5Clarge%20O%28m%20%5Ccdot%20n%5E2%20%5Clog%20n%29)  

And with some tweaks it could be reduced to:  

![rtime2](http://latex.codecogs.com/gif.latex?%5Clarge%20O%28n%5E2%29)
