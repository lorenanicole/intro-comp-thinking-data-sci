Using Depth First Search, and beginning at the listed source nodes, give the first path found to the listed destination nodes. For the purpose of this exercise, assume DFS prioritizes lower numbered nodes. For example, if Node 2 is connected to Nodes 3 and 4, the first path checked will be 23. Additionally, DFS will never return to a node already in its path.

To denote a path, simply list the numbers of the nodes exactly as done in the lecture.

```

Hint: [https://courses.edx.org/asset-v1:MITx+6.00.2x_4+3T2015+type@asset+block/l9p4.png](Draw it out)!

nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]
```

1. Source: 0 (ABC)

Destination: 4 (CAB)

Answer: 014

2. Source: 4
Destination: 1

Answer: 41

3. Source: 1
Destination: 1

Answer: 1

4. Source: 2
Destination: 4

Answer: 2014

We saw before that for permutations of 3 people in line, any two nodes are at most three edges, or four nodes, away. But DFS has yielded paths longer than three edges! In this graph, given a random source and a random destination, what is the probability of DFS finding a path of the shortest possible length?

First, realize that the structure of this graph is a set of six nodes, all connected in a circle. Each node has two edges that connect it to adjacent nodes.

Given any node, we know that DFS will prioritize the lower-numbered neighbor. Thus, for any destination, we first check for paths along this side. If our destination is our source, we terminate the DFS, and return a path of length zero, which is clearly the shortest. Otherwise, we continue in a circle in one direction. We cannot change direction once we have begun to traverse the circle, as the path may not include any node more than once. It will have found the shortest path for the nodes that are 0, 1, 2, or 3 edges away, but will yield paths of length 4 and 5 for the last two nodes that are, in reality, 2 and 1 edges away, respectively. As it has found the shortest path for 4 nodes, but not for 2, the probability is 4 in 6, or 2/3.



