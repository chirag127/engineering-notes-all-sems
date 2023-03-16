# Centralized Deadlock Detection

- Centralized deadlock detection is a technique used in distributed systems to handle deadlock detection.
- According to this technique, the system maintains one global wait-for graph in a single chosen site, which is named as deadlock-detection coordinator.
- The coordinator collects information about the local wait-for graphs of each site and constructs the global wait-for graph.
- The coordinator periodically runs a deadlock detection algorithm on the global wait-for graph to identify any cycles.
- If a cycle is detected, the coordinator selects one or more processes involved in the cycle and sends abort messages to their sites.
- The advantages of this technique are simplicity and efficiency, as only one site is responsible for deadlock detection.
- The disadvantages of this technique are the single point of failure and the communication overhead, as the coordinator needs to collect and update the global wait-for graph frequently.

: https://www.exploredatabase.com/2014/06/centralized-deadlock-detection-approach-in-distributed-database.html
: https://www.javatpoint.com/deadlock-detection-in-distributed-systems
: https://people.cs.rutgers.edu/~pxk/417/notes/deadlock.html
: https://www.geeksforgeeks.org/deadlock-detection-in-distributed-systems/