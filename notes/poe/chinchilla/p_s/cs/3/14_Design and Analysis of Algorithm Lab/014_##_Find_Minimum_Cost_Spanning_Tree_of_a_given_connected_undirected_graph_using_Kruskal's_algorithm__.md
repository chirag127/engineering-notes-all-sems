## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a connected weighted graph. It finds the minimum spanning tree by adding edges in increasing order of their weights until all the vertices are connected. 

The algorithm uses a Union-Find data structure to keep track of the connected components in the graph. The Union-Find data structure maintains a collection of disjoint sets and supports two operations: union and find. The union operation merges two sets, while the find operation returns the representative element of the set containing a given element.

The steps involved in Kruskal's algorithm are as follows:
1. Sort all the edges in non-decreasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If not, add it to the spanning tree. Otherwise, discard it.
3. Repeat step 2 until there are n-1 edges in the spanning tree, where n is the number of vertices in the graph.

Advantages:
- Kruskal's algorithm is easy to understand and implement.
- It always produces a minimum spanning tree.
- It works well for graphs with a large number of edges.

Disadvantages:
- It may not work well for graphs with a large number of vertices.
- It can be slow for dense graphs.

Example:
Consider the following graph:

```
        2
   (0)------(1)
    | \      | 
   6|   \5   |4
    |      \ |
   (2)------(3)
        3
```

The minimum spanning tree using Kruskal's algorithm is:

```
        2
   (0)------(1)
    |        | 
   6|        |4
    |        |
   (2)------(3)
        3
```

Applications:
- Network design
- Circuit design
- Image segmentation

Code:

```
// Kruskal's algorithm
// G is the graph, V is the number of vertices
int kruskal(int G[MAX][MAX], int V)
{
    int parent[MAX];
    int rank[MAX];
    for (int i = 0; i < V; i++) {
        parent[i] = i;
        rank[i] = 0;
    }
    int edges = 0;
    int cost = 0;
    while (edges < V - 1) {
        int min_index = -1;
        int min_weight = INT_MAX;
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (G[i][j] != 0 && find(parent, i) != find(parent, j)) {
                    if (G[i][j] < min_weight) {
                        min_weight = G[i][j];
                        min_index = i;
                    }
                }
            }
        }
        if (min_index != -1) {
            union_sets(parent, rank, min_index, find(parent, min_index));
            cost += min_weight;
            edges++;
        }
    }
    return cost;
}

// Union-Find data structure
int find(int parent[MAX], int i)
{
    if (parent[i] == i) {
        return i;
    }
    return parent[i] = find(parent, parent[i]);
}

void union_sets(int parent[MAX], int rank[MAX], int x, int y)
{
    int xroot = find(parent, x);
    int yroot = find(parent, y);
    if (rank[xroot] < rank[yroot]) {
        parent[xroot] = yroot;
    } else if (rank[xroot] > rank[yroot]) {
        parent[yroot] = xroot;
    } else {
        parent[yroot] = xroot;
        rank[xroot]++;
    }
}
```