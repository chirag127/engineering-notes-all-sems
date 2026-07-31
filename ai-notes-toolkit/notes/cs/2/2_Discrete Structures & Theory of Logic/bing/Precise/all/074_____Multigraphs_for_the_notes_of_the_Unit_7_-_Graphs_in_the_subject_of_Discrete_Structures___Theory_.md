# Multigraphs

- A multigraph is a type of graph that allows multiple edges between two vertices.
- In a multigraph, two vertices can be connected by more than one edge.
- A multigraph can be represented using an adjacency matrix, where the entry in the ith row and jth column represents the number of edges between vertex i and vertex j.
- A multigraph can also be represented using an adjacency list, where each vertex has a list of its adjacent vertices, with multiple entries for vertices that are connected by multiple edges.
- Multigraphs can be used to model real-world situations where there can be multiple relationships between two entities, such as multiple flights between two cities or multiple phone calls between two people.
- A weighted multigraph is a multigraph where each edge has an associated weight, representing the strength or cost of the relationship between the two vertices it connects.
- A directed multigraph is a multigraph where the edges have a direction, representing a one-way relationship between the two vertices it connects.
- A pseudograph is a type of multigraph that allows self-loops, where a vertex can be connected to itself by an edge.
- A simple graph is a type of graph that does not allow multiple edges or self-loops. It can be considered a special case of a multigraph where the maximum number of edges between any two vertices is one and self-loops are not allowed.