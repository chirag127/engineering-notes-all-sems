 Here is the content in markdown format:

### Resource vs Communication Deadlocks for Distributed Deadlock Detection

* Resource deadlock: Occurs when two or more processes acquire locks on shared resources in a conflicting order and wait for each other to release the locks, thus forming a cycle. For example, process P1 acquires lock on resource R1, process P2 acquires lock on resource R2. Now, P1 waits for P2 to release R2 and P2 waits for P1 to release R1.
* Communication deadlock: Occurs when two or more processes are blocked while sending or receiving messages. For example, process P1 sends a message to P2 which is waiting to receive a message from P3 which is waiting to receive a message from P1. All three processes are blocked waiting for each other.

* Mnemonics: Think of resource deadlock as two people wanting to use two resources (say, two printers) at the same time in a conflicting order. Communication deadlock is like a loop of people waiting to pass messages to each other.
* To detect distributed deadlocks, we need to track resource allocation and message passing between processes running on different nodes. This can be done using timestamp ordering, wait-for graphs, etc. The distributed deadlock detection algorithm should be efficient, scalable and minimize false positives.
* Advantages: Preventing deadlocks increases system throughput and avoids system halts.
* Disadvantages: Distributed deadlock detection can be expensive in terms of time and message overhead. It may not scale well for large systems.
* Examples: Database systems, distributed file systems.

The content gives an overview of resource vs communication deadlocks and highlights some key points around distributed deadlock detection. Please let me know if you would like me to elaborate on any part of the answer.