### Centralized Deadlock Detection

- This is a technique used in distributed systems to handle deadlock detection.
- According to this approach, the system maintains one global wait-for graph in a single chosen site, which is named as deadlock-detection coordinator.
- The coordinator collects information about the local wait-for graphs of all the sites and constructs the global wait-for graph.
- The coordinator periodically runs a deadlock detection algorithm on the global wait-for graph to find cycles.
- If a cycle is found, the coordinator selects one or more processes to abort and sends a message to the corresponding sites.
- The advantages of this approach are simplicity and low communication overhead.
- The disadvantages of this approach are the single point of failure and the bottleneck of the coordinator.

: Centralized deadlock detection approach in distributed database, https://www.exploredatabase.com/2014/06/centralized-deadlock-detection-approach-in-distributed-database.html
: Deadlock Detection in Distributed Systems - javatpoint, https://www.javatpoint.com/deadlock-detection-in-distributed-systems
: Distributed Transactions - Rutgers University, https://people.cs.rutgers.edu/~pxk/417/notes/deadlock.html
: Deadlock detection in Distributed systems - GeeksforGeeks, https://www.geeksforgeeks.org/deadlock-detection-in-distributed-systems/
: Deadlock Detection in Distributed Systems - GeeksforGeeks, https://www.geeksforgeeks.org/deadlock-detection-in-distributed-systems-2/