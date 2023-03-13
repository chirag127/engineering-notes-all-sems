### Path-pushing algorithms for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Path-pushing algorithms are a class of distributed deadlock detection algorithms that use an explicit global wait-for graph (WFG) to detect cycles  .
- A WFG is a directed graph that represents the dependencies among processes or transactions in a distributed system. A node in the WFG is a process or transaction, and an edge from node A to node B means that A is waiting for a resource held by B  .
- The basic idea of path-pushing algorithms is to build a global WFG for each site of the distributed system, and periodically check for cycles in the local WFGs . A cycle in the WFG indicates a deadlock  .
- To build the global WFG, each site maintains a local WFG that contains the nodes and edges related to the processes or transactions at that site. Whenever a site performs a deadlock computation, it sends its local WFG to all the neighboring sites, where a neighboring site is a site that shares an edge with the sender in the global WFG.
- The receiving sites update their local WFGs by adding or deleting the nodes and edges received from the sender, and then check for cycles in their updated WFGs. If a cycle is detected, the site initiates a deadlock resolution procedure, such as aborting one of the processes or transactions in the cycle  .
- Path-pushing algorithms have the advantage of being simple and easy to implement, as they only require local information and message passing among neighboring sites  .
- However, path-pushing algorithms also have some disadvantages, such as  :
  - They may generate a large number of messages and consume a lot of network bandwidth, especially when the WFG is dense or the deadlock computation is frequent  .
  - They may incur a high storage overhead, as each site has to store the entire global WFG, which may contain redundant or irrelevant information  .
  - They may suffer from false positives, as the global WFG may not reflect the current state of the system due to message delays or losses  .
  - They may not be scalable, as the size and complexity of the global WFG may increase with the number of sites and processes or transactions in the system  .

- An example of a path-pushing algorithm is Obermarck's algorithm, which is designed for the single-resource model, where each resource can be held by at most one process or transaction at a time.
- Obermarck's algorithm works as follows:
  - Each site maintains a local WFG that contains the nodes and edges related to the processes or transactions at that site, as well as a timestamp that indicates the last time the site performed a deadlock computation.
  - Each site also maintains a vector clock that records the logical time of each site in the system. A vector clock is an array of integers, where the i-th element represents the logical time of the i-th site.
  - Whenever a site performs a deadlock computation, it increments its logical time by one, and sends its local WFG and its vector clock to all the neighboring sites.
  - The receiving sites update their local WFGs by adding or deleting the nodes and edges received from the sender, and update their vector clocks by taking the maximum of each element in their own vector clock and the sender's vector clock.
  - The receiving sites then check for cycles in their updated WFGs, using a depth-first search algorithm that only considers the edges whose timestamps are less than or equal to the current logical time of the site. This ensures that only the edges that reflect the current state of the system are used for deadlock detection.
  - If a cycle is detected, the site initiates a deadlock resolution procedure, such as aborting the youngest process or transaction in the cycle,