# Multigraphs

- A multigraph is a graph that allows multiple edges (also called parallel edges) between two vertices. That is, two vertices can be connected by more than one edge.   
- A multigraph can be represented as a pair G = (V, E), where V is a set of vertices and E is a multiset of unordered pairs of vertices. Each pair in E represents an edge between two vertices. 
- The degree of a vertex in a multigraph is the number of edges incident to it, counting each edge as many times as it appears in the multiset E. 
- A loop is an edge that connects a vertex to itself. A multigraph that has no loops is called a loopless multigraph. 
- A simple graph is a loopless multigraph that has no multiple edges, i.e., each edge connects two distinct vertices and no two edges connect the same pair of vertices. 
- A pseudograph is a multigraph that allows loops. A pseudograph can be represented as a pair G = (V, E), where V is a set of vertices and E is a multiset of unordered pairs of vertices or single vertices. Each pair in E represents an edge between two vertices, and each single vertex in E represents a loop.  
- The degree of a vertex in a pseudograph is the number of edges incident to it, counting each edge as many times as it appears in the multiset E, and counting each loop twice. 
- A multigraph can be used to model various situations where multiple connections are possible or desirable, such as:
  - Redundant connections in a network. 
  - Multiple routes between cities or locations. 
  - Multiple relationships between people or entities. 
  - Multiple types of interactions or transactions.