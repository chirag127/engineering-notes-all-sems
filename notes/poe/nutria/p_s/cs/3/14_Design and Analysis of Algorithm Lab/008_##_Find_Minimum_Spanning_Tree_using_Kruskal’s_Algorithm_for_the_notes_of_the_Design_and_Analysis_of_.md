
## Find Minimum Spanning Tree using Kruskal’s Algorithm 
Kruskal’s Algorithm is a method used to find the minimum spanning tree (MST) of a given graph. It is a greedy algorithm which finds an MST by finding the smallest weighted edge of the graph and adding it to the MST. The algorithm works by sorting the edges of the graph by their weight and then iteratively adding the smallest weighted edge to the MST. The algorithm stops when it has added all the edges in the graph to the MST.

Advantages: 
- Kruskal’s Algorithm is simple and easy to implement. 
- It is a fast and efficient algorithm for finding the MST of a graph. 
- It is a greedy algorithm, so it can be used to solve many other optimization problems.

Disadvantages: 
- Kruskal’s Algorithm is not suitable for finding the MST of a directed graph. 
- It is not able to handle negative weights.

Applications: 
- Kruskal’s Algorithm can be used to find the MST of a graph, which can be used to solve many optimization problems such as the Traveling Salesman Problem. 
- It can also be used to find the shortest path between two nodes in a graph. 
- It can be used to solve the Steiner Tree problem, which is the problem of finding the minimum cost tree that connects a given set of vertices.

Example: 
Consider the following graph: 

![alt text](https://i.imgur.com/Qz6U8x6.png)

Using Kruskal’s Algorithm, we can find the MST of this graph as follows: 

1. Sort the edges of the graph by their weight. 
2. Select the smallest weighted edge (A-B, weight = 2). 
3. Add this edge to the MST. 
4. Check if adding this edge creates a cycle in the MST. If not, add the edge to the MST. 
5. Repeat steps 2-4 until all the edges in the graph have been added to the MST. 

The MST of this graph is shown below: 

![alt text](https://i.imgur.com/XZQ2gKj.png)