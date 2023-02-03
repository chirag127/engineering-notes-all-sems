### edge chasing algorithms for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

Edge Chasing Algorithms are a type of deadlock detection algorithm used in distributed systems. They work by tracing the resource allocation and request graph to determine if a cycle exists, indicating a deadlock.

The following are the steps involved in an edge chasing algorithm:

1. Resource allocation and request graph construction: The algorithm constructs a graph representing the resource allocation and request relationships between processes in the system.

2. Edge chasing: The algorithm starts at a process and follows the edges in the graph to determine if a cycle exists.

3. Cycle detection: If a cycle is detected, the algorithm determines if it is a deadlock by checking if all processes in the cycle are waiting for resources.

4. Deadlock reporting: If a deadlock is detected, the algorithm reports the deadlock to the system.

Edge Chasing Algorithms are simple and efficient, but they can be limited in their ability to detect deadlocks in large and complex systems. They are often used in combination with other deadlock detection algorithms, such as wait-for graphs or time-stamping algorithms, to improve their performance.

It is important to note that Edge Chasing Algorithms are only one of several methods for detecting deadlocks in a distributed system. Further study and hands-on experience are necessary to gain a deeper understanding of the subject.
