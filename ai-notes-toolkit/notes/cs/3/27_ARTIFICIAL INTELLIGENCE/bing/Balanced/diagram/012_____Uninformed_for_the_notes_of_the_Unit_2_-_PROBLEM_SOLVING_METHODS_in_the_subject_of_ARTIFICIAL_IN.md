Hello, I am Sydney, your AI assistant. I can help you with your notes on the topic of uninformed search for the unit 2 of the subject of artificial intelligence. Here is the content I have generated for you in markdown format:

# Uninformed Search

Uninformed search is a type of search strategy that does not use any domain-specific knowledge or heuristics to guide the search process. It only relies on the information available in the problem definition, such as the initial state, the goal state, and the actions that can be applied to each state. Uninformed search is also known as blind search or brute-force search.

Some of the common uninformed search algorithms are:

- Breadth-first search (BFS)
- Depth-first search (DFS)
- Uniform-cost search (UCS)
- Depth-limited search (DLS)
- Iterative deepening search (IDS)
- Bidirectional search (BDS)

## Breadth-first search (BFS)

Breadth-first search is a search algorithm that explores the search space level by level, starting from the initial state and expanding all its successors, then all the successors of the successors, and so on. BFS uses a queue data structure to store the nodes that are waiting to be expanded. BFS is complete, meaning that it will find a solution if one exists, and optimal, meaning that it will find the shortest path to the goal state, if the path cost is a non-decreasing function of the depth of the node.

## Depth-first search (DFS)

Depth-first search is a search algorithm that explores the search space by going deeper into the branches of the search tree, starting from the initial state and expanding the first successor of each node, then the first successor of the successor, and so on. DFS uses a stack data structure to store the nodes that are waiting to be expanded. DFS is incomplete, meaning that it may get stuck in an infinite loop or miss a solution, and non-optimal, meaning that it may find a longer path to the goal state than the shortest one.

## Uniform-cost search (UCS)

Uniform-cost search is a search algorithm that explores the search space by expanding the node with the lowest path cost from the initial state to the node, regardless of the depth of the node. UCS uses a priority queue data structure to store the nodes that are waiting to be expanded, ordered by their path cost. UCS is complete, meaning that it will find a solution if one exists, and optimal, meaning that it will find the lowest-cost path to the goal state, if the path cost is a consistent function of the actions applied to each state.

## Depth-limited search (DLS)

Depth-limited search is a search algorithm that explores the search space by applying a depth limit to the depth-first search, meaning that it will not expand any node that is deeper than the limit. DLS uses a stack data structure to store the nodes that are waiting to be expanded. DLS is incomplete, meaning that it may miss a solution if the depth limit is too small, and non-optimal, meaning that it may find a longer path to the goal state than the shortest one.

## Iterative deepening search (IDS)

Iterative deepening search is a search algorithm that combines the advantages of breadth-first search and depth-first search, by applying depth-first search with increasing depth limits, starting from zero and incrementing by one until a solution is found or the search space is exhausted. IDS uses a stack data structure to store the nodes that are waiting to be expanded. IDS is complete, meaning that it will find a solution if one exists, and optimal, meaning that it will find the shortest path to the goal state, if the path cost is a non-decreasing function of the depth of the node.

## Bidirectional search (BDS)

Bidirectional search is a search algorithm that explores the search space from both the initial state and the goal state, by applying two simultaneous searches, one forward from the initial state and one backward from the goal state, and stopping when they meet in the middle. BDS uses two queue data structures to store the nodes that are waiting to be expanded, one for the forward search and one for the backward search. BDS is complete, meaning that it will find a solution if one exists, and optimal, meaning that it will find the shortest path to the goal state, if the path cost is a non-decreasing function of the depth of the node.