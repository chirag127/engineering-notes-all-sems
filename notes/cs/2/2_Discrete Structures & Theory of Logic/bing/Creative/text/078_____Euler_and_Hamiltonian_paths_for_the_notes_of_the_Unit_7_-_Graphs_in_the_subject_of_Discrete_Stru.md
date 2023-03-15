### Euler and Hamiltonian paths

- An **Euler path** is a path that passes through every **edge** exactly once  . If it ends at the initial vertex then it is an **Euler cycle**  .
- A **Hamiltonian path** is a path that passes through every **vertex** exactly once  . If it ends at the initial vertex then it is a **Hamiltonian cycle**  .
- Euler paths and cycles can be found using **Euler's theorem**, which states that a connected graph has an Euler path if and only if it has exactly **zero or two vertices of odd degree** . A connected graph has an Euler cycle if and only if it has **no vertices of odd degree** .
- Hamiltonian paths and cycles are harder to find, as there is no simple necessary and sufficient criteria to determine if they exist in a graph. However, some **sufficient conditions** are:
  - **Dirac's theorem**: A simple graph with n vertices (n ≥ 3) is Hamiltonian if every vertex has degree n/2 or greater .
  - **Ore's theorem**: A simple graph with n vertices (n ≥ 3) is Hamiltonian if for every pair of non-adjacent vertices, their degrees sum to n or more .
  - **Bondy and Chvátal's theorem**: A simple graph with n vertices (n ≥ 3) is Hamiltonian if for every pair of non-adjacent vertices with degrees summing to less than n, adding an edge between them results in a Hamiltonian graph .
- Some **necessary conditions** for a graph to be Hamiltonian are:
  - The graph must be **connected** .
  - The graph must have at least **three vertices** .
  - The graph must not contain any **vertex cut** (a set of vertices whose removal disconnects the graph) .
- Some examples of graphs that have Euler paths, Euler cycles, Hamiltonian paths, and Hamiltonian cycles are shown below:

![Euler and Hamiltonian paths and cycles](https://i.imgur.com/1g8l8Wf.png)

- The graph on the left has an Euler path (a-b-c-d-e-f-g-h-i-j-k-l) but not an Euler cycle, as it has two vertices of odd degree (a and l) . It also has a Hamiltonian path (a-b-c-d-e-f-g-h-i-j-k-l) but not a Hamiltonian cycle, as a and l are not adjacent .
- The graph on the right has an Euler cycle (a-b-c-d-e-f-g-h-i-j-k-l-a) and an Euler path (any subset of the cycle), as it has no vertices of odd degree . It also has a Hamiltonian cycle (a-b-c-d-e-f-g-h-i-j-k-l-a) and a Hamiltonian path (any subset of the cycle), as it satisfies Dirac's theorem .