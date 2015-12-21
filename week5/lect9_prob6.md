In the following examples, assume all graphs are undirected. That is, an edge from A to B is the same as an edge from B to A and counts as exactly one edge.

A clique is an unweighted graph where each node connects to all other nodes. We denote the clique with n nodes as KN. Answer the following questions in terms of n.

1. What is the asymptotic worst-case runtime of a Breadth First Search on KN? For simplicity, write O(n) as just n, O(n2) as n^2, etc.

n

Answer: O(n)
BFS begins by checking all the paths of length 1. In its worst case, it must check the paths to every node from the source to find the destination. This is at most, n−1 checks.

2. BFS will always run faster than DFS.

FALSE

Consider a graph of two nodes, A and B, connected by an edge. You wish to search for a path from A to B. As there is exactly one edge in the graph, and exactly one path from A to B, both run in an equal number of steps.

3. If a BFS and DFS prioritize the same nodes (e.g., both always choose to explore the lower numbered node first), BFS will always run at least as fast as DFS when run on two nodes in KN.

TRUE

As seen in our previous problems in this lecture sequence, BFS checks at most n−1 paths in KN, and DFS always checks O((n−2)!) paths. If given the same node prioritization, both will first find the desired node in the same number of steps.

4. If a BFS and Shortest Path DFS prioritize the same nodes (e.g., both always choose to explore the lower numbered node first), BFS will always run at least as fast as Shortest Path DFS when run on two nodes in any connected unweighted graph.

TRUE

While Shortest Path DFS may find the desired node first in this case, it still must explore all other paths before it has determined which path is the fastest. BFS will explore only a fraction of the paths.

5. Regardless of node priority, BFS will always run at least as fast as Shortest Path DFS on two nodes in any connected unweighted graph.

TRUE

Shortest Path DFS must always explore every path from the source to the destination to ensure that it has found the shortest path. Once BFS has found a path, it knows that it is the shortest, and does not have to explore any other paths.