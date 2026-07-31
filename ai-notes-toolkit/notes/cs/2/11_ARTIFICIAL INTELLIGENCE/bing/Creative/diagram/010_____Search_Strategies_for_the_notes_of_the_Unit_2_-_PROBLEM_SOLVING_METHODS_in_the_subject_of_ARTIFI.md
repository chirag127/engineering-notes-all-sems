Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on search strategies for the unit 2 - problem solving methods in the subject of artificial intelligence KCS.

### Search Strategies

- Search strategies are universal problem-solving methods that help rational agents or problem-solving agents in AI to solve a specific problem and provide the best result .
- A search problem consists of a search space, start state, and goal state. Search algorithms help the AI agents to attain the goal state through the assessment of scenarios and alternatives.
- Search strategies can be classified into two types: uninformed search and informed search.
- Uninformed search strategies do not use any domain-specific knowledge or heuristics to guide the search. They are also called blind search or brute-force search.
- Informed search strategies use domain-specific knowledge or heuristics to guide the search. They are also called heuristic search or best-first search.

#### Uninformed Search Strategies

- The uninformed search strategies are of six types. They are:
  - Breadth-first search
  - Depth-first search
  - Depth-limited search
  - Iterative deepening depth-first search
  - Bidirectional search
  - Uniform cost search
- Breadth-first search (BFS) is an algorithm that explores the nodes at the same level of the search tree before moving to the next level. It uses a queue data structure to store the nodes. It is complete and optimal for problems with constant step costs.
- Depth-first search (DFS) is an algorithm that explores the nodes as far as possible along each branch of the search tree before backtracking. It uses a stack data structure to store the nodes. It is neither complete nor optimal, but it is memory-efficient.
- Depth-limited search (DLS) is an algorithm that limits the depth of the search tree to a predefined value. It avoids the problem of infinite paths in DFS. It is complete and optimal for problems with constant step costs and a known depth limit.
- Iterative deepening depth-first search (IDDFS) is an algorithm that combines the benefits of BFS and DFS. It performs DFS with increasing depth limits until the goal is found or the search space is exhausted. It is complete and optimal for problems with constant step costs.
- Bidirectional search (BDS) is an algorithm that performs two simultaneous searches: one from the start state and one from the goal state. It stops when the two searches meet in the middle. It is complete and optimal for problems with reversible actions and known goal states.
- Uniform cost search (UCS) is an algorithm that expands the node with the lowest path cost from the start state. It uses a priority queue data structure to store the nodes. It is complete and optimal for problems with variable step costs.

#### Informed Search Strategies

- The informed search strategies are of four types. They are:
  - Greedy search
  - A* search
  - Hill climbing search
  - Beam search
- Greedy search (GS) is an algorithm that expands the node that appears to be closest to the goal state according to a heuristic function. It uses a priority queue data structure to store the nodes. It is neither complete nor optimal, but it is fast and memory-efficient.
- A* search (AS) is an algorithm that expands the node that has the lowest estimated total cost from the start state to the goal state. The estimated total cost is the sum of the path cost and the heuristic cost. It uses a priority queue data structure to store the nodes. It is complete and optimal for problems with admissible and consistent heuristics.
- Hill climbing search (HCS) is an algorithm that moves from the current state to a better state according to a heuristic function. It does not keep track of the visited states. It is neither complete nor optimal, but it is simple and fast. It may get stuck in local optima or plateaus.
- Beam search (BS) is an algorithm that is similar to BFS, but it only keeps a fixed number of best nodes at each level of the search tree. It uses a priority queue data structure to store the nodes. It is neither complete nor optimal, but it is memory-efficient and can find good solutions quickly.