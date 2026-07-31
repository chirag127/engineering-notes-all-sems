 Here are the notes on Distributed Deadlock Detection in a formal tone without any emojis or external links:

### Distributed Deadlock Detection

1. Local detection: Each site maintains waiting-for graph for transactions at that site. If a cycle is detected, a deadlock exists. This method is inadequate as deadlock may involve multiple sites.
2. Centralized global detection: All sites send information about waiting transactions to a central site which performs cycle detection on the combined graph. This requires extra messages and the central site can become a bottleneck.
3. Distributed detection: Each site sends information about waiting transactions to all other sites. Each site performs cycle detection on the entire system's waiting-for graph by merging information received from all sites. This method detects global deadlocks but messages grow quadratically with number of sites.
4. Partitioned detection: The system is logically partitioned into overlapping groups. Each group performs local cycle detection and if a deadlock is detected, other groups are checked for participating transactions. This reduces messaging but a global deadlock may be missed if partitions are chosen poorly.

The notes cover the key points around the different approaches for Distributed Deadlock Detection - Local detection, Centralized global detection, Distributed detection and Partitioned detection. The points are written in a formal tone with headings and no emojis or external links as specified. Please let me know if you would like me to elaborate on any of the points or modify the notes in any way.