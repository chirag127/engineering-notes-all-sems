 Here is the formal content in markdown format without emojis and external links on the topic "edge chasing algorithms for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM":

### Edge Chasing Algorithms

- Edge chasing algorithms are used to detect deadlocks in distributed systems.
- They work by traversing the wait-for graph from each node and checking if a cycle is detected.
- If a cycle is found, it indicates a deadlock. The following are some common edge chasing algorithms:

1. Depth-first search: Starts at a node and goes as far as possible along each branch before backtracking. Detects deadlocks but may take a long time to traverse the entire graph.
2. Breadth-first search: Explores edges at each level before going to the next level. Guaranteed to find a deadlock if one exists but may take a long time for large graphs.
3. Bridging: Starts at an arbitrary node and stops searching down a particular branch as soon as a node that has been previously visited is reached. Fast but may fail to detect deadlocks in some cases.

- The choice of algorithm depends on the efficiency and completeness requirements of deadlock detection in the system.
- Through this process, the distributed deadlock can be detected and appropriate recovery actions can be taken.

The above content summarizes the key points about edge chasing algorithms for detecting distributed deadlocks. The points are written in a formal tone with Markdown formatting and without any emojis or external links as requested. Please let me know if you would like me to elaborate on any part of the content.