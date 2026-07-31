 Here are the notes for Unit 2 - Problem Solving Methods of Artificial Intelligence KCS in a formal tone without emojis or external links:

### Uninformed Search Methods

- Blind Search: It is a naive approach. The agent makes a random choice at each step to reach the goal state. It does not use the information of the explored nodes.
- Breadth First Search: It explores all the neighboring nodes of the start node before going to the next level nodes. It keeps track of all explored nodes in a queue data structure. The node which is at the front of the queue is always processed next.
- Depth First Search: It explores as far as possible along each branch before backtracking. A stack data structure is used to keep track of explored nodes where the node which is at the top of stack is processed next.

The pros and cons of uninformed search methods are:

Pros:
- Guaranteed to find a solution if one exists
- Simple to implement

Cons:
- Does not efficiently use the problem structure/domain information
- Can explore a large number of nodes and have poor runtime performance

Notes:
- The choice of uninformed method depends on - memory usage vs speed
- Graph search, game playing uses uninformed methods
- Informed methods are preferred if problem specific knowledge can be used to guide the search.