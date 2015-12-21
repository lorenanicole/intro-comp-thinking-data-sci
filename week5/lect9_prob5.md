In the following examples, assume all graphs are undirected. That is, an edge from A to B is the same as an edge from B to A and counts as exactly one edge.

A clique is an unweighted graph where each node connects to all other nodes. We denote the clique with n nodes as KN. Answer the following questions in terms of n.

1. How many edges are in KN?

Answer: n*(n−1)/2

In a directed graph, each node would connect to all other nodes, yielding n⋅(n−1) edges. In our undirected graph, an edge from A to B and from B to A are the same edge, so there are, in fact, half as many.

2. Consider the new version of DFS. This traverses paths until all non-circular paths from the source to the destination have been found, and returns the shortest one.

Let A be the source node, and B be the destination in KN. How many paths of length 2 exist from A to B?

Answer: n−2

We have a source A and a destination B. Paths of length 2 contain exactly three three nodes. We must select one more node to place in the middle of our path. As we cannot select the A or B, we are left with N - 2 choices to construct a path.

3. How many paths of length 3 exist from A to B?

4. Continuing the logic used above, calculate the number of paths of length m from A to B, where 1≤m≤(n−1), and write this number as a ratio of factorials.

To indicate a factorial, please enter fact(n) to mean n!; fact(n+2) to mean (n+2)!, etc.

5. Using the fact that for any n, 1/0!+1/1!+1/2!+...+1/n!≤e for all n, where e is some constant, determine the asymptotic bound on the number of paths explored by DFS. For simplicity, write O(n) as just n, O(n2) as n^2, etc.