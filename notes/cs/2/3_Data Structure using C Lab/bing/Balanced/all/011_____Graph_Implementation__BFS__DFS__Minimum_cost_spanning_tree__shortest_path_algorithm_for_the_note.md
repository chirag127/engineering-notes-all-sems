# Graph Implementation, BFS, DFS, Minimum cost spanning tree, shortest path algorithm for the notes of the Data Structure using C Lab in the subject of Data Structure using C

## Graph Implementation in C

- A graph is a collection of vertices and edges, where each edge connects two vertices.
- A graph can be represented in different ways, such as an adjacency matrix, an adjacency list, or an edge list.
- An adjacency matrix is a two-dimensional array of size V x V, where V is the number of vertices in the graph. The element at row i and column j of the matrix is 1 if there is an edge from vertex i to vertex j, and 0 otherwise. An adjacency matrix is easy to implement and query, but it takes O(V^2) space and is inefficient for sparse graphs.
- An adjacency list is an array of linked lists, where each element of the array corresponds to a vertex in the graph. The linked list at index i contains the vertices that are adjacent to vertex i. An adjacency list is more space-efficient than an adjacency matrix, especially for sparse graphs, but it takes more time to check if there is an edge between two vertices.
- An edge list is a list of pairs of vertices, where each pair represents an edge in the graph. An edge list is simple to implement and iterate over, but it takes more time to find the neighbors of a vertex or to check if there is an edge between two vertices.

- In C, we can use structures and pointers to implement a graph data structure. For example, we can define a structure for a vertex as follows:

```c
// A structure to represent a vertex
struct Vertex {
    int data; // the data stored in the vertex
    struct Vertex* next; // a pointer to the next vertex in the adjacency list
};
```

- Similarly, we can define a structure for an edge as follows:

```c
// A structure to represent an edge
struct Edge {
    int src; // the source vertex of the edge
    int dest; // the destination vertex of the edge
    int weight; // the weight of the edge (optional)
    struct Edge* next; // a pointer to the next edge in the edge list
};
```

- To represent a graph using an adjacency list, we can use an array of pointers to vertices, where each pointer points to the head of the linked list of adjacent vertices. For example, we can declare a graph with 6 vertices as follows:

```c
// A structure to represent a graph using an adjacency list
struct Graph {
    int V; // the number of vertices in the graph
    struct Vertex** adjList; // an array of pointers to vertices
};

// Create a graph with 6 vertices
struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
graph->V = 6;
graph->adjList = (struct Vertex**)malloc(graph->V * sizeof(struct Vertex*));

// Initialize all the pointers to NULL
for (int i = 0; i < graph->V; i++) {
    graph->adjList[i] = NULL;
}
```

- To add an edge from vertex u to vertex v in the graph, we can create a new vertex node with data v and insert it at the beginning of the linked list pointed by graph->adjList[u]. For example, to add an edge from 0 to 1 in the graph, we can do the following:

```c
// Create a new vertex node with data 1
struct Vertex* newNode = (struct Vertex*)malloc(sizeof(struct Vertex));
newNode->data = 1;
newNode->next = NULL;

// Insert the node at the beginning of the linked list pointed by graph->adjList[0]
newNode->next = graph->adjList[0];
graph->adjList[0] = newNode;
```

- To represent a graph using an edge list, we can use a pointer to the head of the linked list of edges. For example, we can declare a graph with 6 vertices and 0 edges as follows:

```c
// A structure to represent a graph using an edge list
struct Graph {
    int V; // the number of vertices in the graph
    int E; // the number of edges in the graph
    struct Edge* edgeList; // a pointer to the head of the linked list of edges
};

// Create a graph with 6 vertices and 0 edges
struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
graph->V = 6;
graph->E =