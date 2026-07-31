### Centralized Deadlock Detection

- This is a technique used in distributed systems to handle deadlock detection.
- According to this technique, the system maintains one global wait-for graph in a single chosen site, which is named as deadlock-detection coordinator.
- The coordinator collects information about the local wait-for graphs of each site and constructs the global wait-for graph.
- The coordinator periodically runs a deadlock detection algorithm on the global wait-for graph to find cycles, which indicate deadlocks.
- If a deadlock is detected, the coordinator selects a victim process to abort and sends a message to the corresponding site to terminate the process.
- The advantages of this technique are simplicity and low communication overhead.
- The disadvantages of this technique are the dependency on a single site, which may become a bottleneck or a single point of failure, and the possibility of false or phantom deadlocks due to outdated information .

: Centralized deadlock detection approach in distributed database. https://www.exploredatabase.com/2014/06/centralized-deadlock-detection-approach-in-distributed-database.html
: Deadlock Detection in Distributed Systems - javatpoint. https://www.javatpoint.com/deadlock-detection-in-distributed-systems
: Distributed Transactions - Rutgers University. https://people.cs.rutgers.edu/~pxk/417/notes/deadlock.html
: Deadlock detection in Distributed systems - GeeksforGeeks. https://www.geeksforgeeks.org/deadlock-detection-in-distributed-systems/
: Deadlock detection in distributed systems (Chapter 10) - Distributed Computing. https://www.cambridge.org/core/books/distributed-computing/deadlock-detection-in-distributed-systems/9A6629FF01607C520BC2AA034B647792