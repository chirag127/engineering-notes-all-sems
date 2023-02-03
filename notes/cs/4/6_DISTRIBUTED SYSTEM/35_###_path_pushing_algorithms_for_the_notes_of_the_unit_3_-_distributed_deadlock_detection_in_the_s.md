### path pushing algorithms for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM
Path pushing algorithms are used in distributed deadlock detection to detect cycles in resource allocation graphs. They work by sending messages along resource allocation paths in the graph and checking for cycles. 

1. Centralized path pushing: A central coordinator is responsible for detecting deadlocks by pushing messages along resource allocation paths and checking for cycles. 

2. Distributed path pushing: Each node in the system is responsible for detecting deadlocks by pushing messages along resource allocation paths and checking for cycles. 

3. Hybrid path pushing: A combination of centralized and distributed path pushing, where a central coordinator is responsible for coordinating the distributed nodes in detecting deadlocks. 

Advantages of path pushing algorithms include their ability to detect deadlocks in large and complex resource allocation graphs, and their scalability to handle large numbers of nodes. However, they can also be computationally expensive and may introduce additional overhead in the system.
