# Precedence Constraints and Data Dependency

- Precedence constraints and data dependency are two types of constraints that may affect the scheduling of jobs in real-time systems.
- Precedence constraints specify the order in which jobs must execute, while data dependency specifies the data flow between jobs that communicate via shared data.
- Precedence constraints and data dependency can be represented by directed graphs, where vertices are jobs and edges are constraints or dependencies.

## Precedence Constraints

- Precedence constraints are imposed by the logical or temporal relationships among jobs, such as control flow, synchronization, or resource sharing.
- A job J_i is a predecessor of another job J_k (and J_k a successor of J_i) if J_k cannot begin execution until the execution of J_i completes.
- A precedence graph G = (J, <) is a directed graph where J is the set of jobs and < is the precedence relation. An edge (J_i, J_k) in G means that J_i is a predecessor of J_k.
- A precedence graph is acyclic if there is no cycle in the graph, meaning that there is no job that is a predecessor of itself or of its predecessors. A cyclic precedence graph implies a deadlock situation, where no job can execute.
- A precedence graph is transitive if for any three jobs J_i, J_j, and J_k, if (J_i, J_j) and (J_j, J_k) are edges in the graph, then (J_i, J_k) is also an edge in the graph. A transitive precedence graph can be simplified by removing redundant edges.
- A precedence graph is consistent if for any two jobs J_i and J_k, if (J_i, J_k) is an edge in the graph, then the deadline of J_i is earlier than or equal to the deadline of J_k. A consistent precedence graph ensures that no job misses its deadline because of its predecessors.

## Data Dependency

- Data dependency arises when jobs communicate via shared data, such as variables, buffers, or messages.
- A job J_i is a producer of another job J_k (and J_k a consumer of J_i) if J_i writes data that J_k reads.
- A data dependency graph G = (J, D) is a directed graph where J is the set of jobs and D is the data dependency relation. An edge (J_i, J_k) in G means that J_i is a producer of J_k.
- A data dependency graph is acyclic if there is no cycle in the graph, meaning that there is no job that is a producer of itself or of its producers. A cyclic data dependency graph implies a livelock situation, where no job can access the data it needs.
- A data dependency graph is transitive if for any three jobs J_i, J_j, and J_k, if (J_i, J_j) and (J_j, J_k) are edges in the graph, then (J_i, J_k) is also an edge in the graph. A transitive data dependency graph can be simplified by removing redundant edges.
- A data dependency graph is consistent if for any two jobs J_i and J_k, if (J_i, J_k) is an edge in the graph, then the release time of J_i is earlier than or equal to the release time of J_k. A consistent data dependency graph ensures that no job reads stale data because of its producers.