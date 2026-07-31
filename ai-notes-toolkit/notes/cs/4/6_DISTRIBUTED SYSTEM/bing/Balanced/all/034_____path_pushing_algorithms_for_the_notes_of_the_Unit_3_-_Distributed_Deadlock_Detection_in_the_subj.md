# Path Pushing Algorithms for Distributed Deadlock Detection

- Path pushing algorithms detect distributed deadlocks by keeping an explicit global wait-for graph (WFG)  .
- The main idea is to create a global WFG for each site of the distributed system  .
- A site is a node in the distributed system that can initiate, request, or grant resources .
- A WFG is a directed graph that represents the dependencies among the processes or transactions in the system .
- A node in the WFG is a process or transaction, and an edge from node A to node B means that A is waiting for a resource held by B .
- A cycle in the WFG indicates a deadlock situation .
- In this class of algorithms, at each site, whenever deadlock computation is performed, it sends its local WFG to all the neighboring sites  .
- A neighboring site is a site that shares a common edge with the sender site in the WFG .
- The receiver site then merges the received WFG with its own local WFG and checks for cycles  .
- If a cycle is detected, the receiver site initiates the deadlock resolution process .
- The advantages of path pushing algorithms are that they can detect deadlocks quickly and accurately, and they do not require probe messages or global state information .
- The disadvantages of path pushing algorithms are that they require a lot of communication and storage overhead, and they may generate false cycles due to concurrency and inconsistency .