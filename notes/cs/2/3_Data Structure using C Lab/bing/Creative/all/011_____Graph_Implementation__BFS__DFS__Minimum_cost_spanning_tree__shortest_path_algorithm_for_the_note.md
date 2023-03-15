# Graph Implementation, BFS, DFS, Minimum cost spanning tree, shortest path algorithm for the notes of the Data Structure using C Lab in the subject of Data Structure using C

## Graph Implementation

- A graph is a collection of vertices and edges, where each edge connects two vertices.
- A graph can be represented in different ways, such as an adjacency matrix, an adjacency list, or an edge list.
- An adjacency matrix is a two-dimensional array of size V x V, where V is the number of vertices in the graph. The element at row i and column j is 1 if there is an edge from vertex i to vertex j, and 0 otherwise. An adjacency matrix is easy to implement and query, but it takes O(V^2) space and is inefficient for sparse graphs.
- An adjacency list is an array of linked lists, where each element of the array corresponds to a vertex in the graph. The linked list at index i contains the vertices that are adjacent to vertex i. An adjacency list is more space-efficient than an adjacency matrix, especially for sparse graphs, but it takes more time to check if there is an edge between two vertices.
- An edge list is a list of pairs of vertices, where each pair represents an edge in the graph. An edge list is simple to implement and iterate over, but it takes more time to find the neighbors of a vertex or to check if there is an edge between two vertices.

- In C, we can implement a graph using structures and pointers. For example, we can define a structure for an edge as follows:

```c
// A structure to represent an edge
struct Edge {
    int src; // source vertex
    int dest; // destination vertex
    int weight; // weight of the edge (optional)
    struct Edge* next; // pointer to the next edge in the list
};
```

- Similarly, we can define a structure for a vertex as follows:

```c
// A structure to represent a vertex
struct Vertex {
    int data; // data stored in the vertex (optional)
    struct Edge* head; // pointer to the head of the edge list
};
```

- To represent a graph using an adjacency list, we can use an array of vertices, where each element of the array is a pointer to a vertex structure. For example, we can declare a graph with V vertices as follows:

```c
// A structure to represent a graph
struct Graph {
    int V; // number of vertices
    struct Vertex* array; // array of vertices
};

// A function to create a new graph with V vertices
struct Graph* createGraph(int V) {
    // allocate memory for the graph structure
    struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
    // assign the number of vertices
    graph->V = V;
    // allocate memory for the array of vertices
    graph->array = (struct Vertex*)malloc(V * sizeof(struct Vertex));
    // initialize each vertex and its edge list
    for (int i = 0; i < V; i++) {
        graph->array[i].data = i; // assign some data to the vertex (optional)
        graph->array[i].head = NULL; // initialize the edge list as empty
    }
    // return the graph
    return graph;
}
```

- To add an edge from vertex u to vertex v in the graph, we can create a new edge structure and insert it at the beginning of the edge list of vertex u. For example, we can define a function to add an edge as follows:

```c
// A function to add an edge from u to v in the graph
void addEdge(struct Graph* graph, int u, int v, int weight) {
    // allocate memory for the new edge
    struct Edge* edge = (struct Edge*)malloc(sizeof(struct Edge));
    // assign the source, destination, and weight
    edge->src = u;
    edge->dest = v;
    edge->weight = weight;
    // insert the edge at the beginning of the edge list of u
    edge->next = graph->array[u].head;
    graph->array[u].head = edge;
}
```

- To print the graph, we can iterate over the array of vertices and print the edge list of each vertex. For example, we can define a function to print the graph as follows:

```c
// A function to print the graph
void printGraph(struct Graph* graph) {
    // iterate over the array of vertices
    for (int i = 0;