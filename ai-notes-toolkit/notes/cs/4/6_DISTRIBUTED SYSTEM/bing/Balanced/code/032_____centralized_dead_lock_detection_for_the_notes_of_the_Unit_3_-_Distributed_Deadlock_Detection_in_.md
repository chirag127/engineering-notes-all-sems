# Centralized Deadlock Detection

- This is a technique used in distributed systems to handle deadlock detection.
- According to this approach, the system maintains one global wait-for graph in a single chosen site, which is named as deadlock-detection coordinator.
- The coordinator collects information about the local wait-for graphs of each site and constructs the global wait-for graph.
- The coordinator periodically runs a deadlock detection algorithm on the global wait-for graph to find cycles, which indicate deadlocks.
- If a deadlock is detected, the coordinator selects a victim process and sends an abort message to the site where the process is located.
- The advantages of this approach are simplicity and low communication overhead.
- The disadvantages of this approach are single point of failure, scalability issues, and lack of autonomy.

: https://www.exploredatabase.com/2014/06/centralized-deadlock-detection-approach-in-distributed-database.html
: https://www.javatpoint.com/deadlock-detection-in-distributed-systems
: https://people.cs.rutgers.edu/~pxk/417/notes/deadlock.html
: https://www.geeksforgeeks.org/deadlock-detection-in-distributed-systems/