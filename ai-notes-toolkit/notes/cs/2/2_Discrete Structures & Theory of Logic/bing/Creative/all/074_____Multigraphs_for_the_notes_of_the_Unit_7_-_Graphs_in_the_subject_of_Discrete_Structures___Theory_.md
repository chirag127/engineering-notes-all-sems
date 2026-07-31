# Multigraphs

- A **multigraph** is a graph that allows **multiple edges** (also called parallel edges) between the same pair of vertices. A multigraph does not allow **loops**, which are edges that connect a vertex to itself .
- A multigraph can be represented by a **pair** of sets: G = (V, E), where V is the set of vertices and E is a **multiset** of unordered pairs of vertices, called edges .
- A multigraph can also be represented by an **adjacency matrix**, which is a square matrix A of size n x n, where n is the number of vertices. The entry A[i][j] is the number of edges between vertices i and j. The matrix is **symmetric** since the graph is undirected.
- A multigraph can be **visualized** by drawing the vertices as points and the edges as curves connecting the vertices. If there are multiple edges between two vertices, they are drawn as separate curves. The order and shape of the curves do not matter .
- A multigraph is a **generalization** of a simple graph, which is a graph that does not allow multiple edges or loops. A simple graph is a special case of a multigraph where the multiset E is a set, i.e., no repeated elements .
- A multigraph can be **converted** to a simple graph by removing the extra edges between any pair of vertices. This process may result in a loss of information about the original multigraph.
- A multigraph can be **used** to model situations where there are different types of relationships or connections between the same entities, such as roads, flights, or communication channels .