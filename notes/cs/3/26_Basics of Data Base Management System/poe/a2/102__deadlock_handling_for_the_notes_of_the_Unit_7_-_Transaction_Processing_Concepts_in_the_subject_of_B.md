 Here is the content in markdown format without any emojis or external links and in formal tone:

### Deadlock Handling

- Deadlock: A deadlock is a situation where two or more transactions are waiting indefinitely for an event that can be caused by only one of the waiting transactions.
- Deadlock Detection: The DBMS constantly monitors all running transactions to detect a deadlock. This can be done using following algorithms:
- Wait-for graph: A directed graph is created where vertices represent transactions and edges represent waiting relationships between transactions. A deadlock exists if a cycle is detected in the graph.
- Timeout-based: If a transaction waits for more than a fixed amount of time, a timeout occurs and system checks for deadlock. If deadlock is detected, one of the deadlocked transactions is aborted.
- Deadlock Prevention: Certain conditions must hold simultaneously for deadlock to occur. By preventing at least one of these conditions, deadlock can be prevented:
 - Mutual exclusion: Prevent transactions from acquiring exclusive locks on resources. Allow only shared locks.
 - Hold and wait: Prevent transactions from requesting new resources while holding locks on other resources. Require transactions to request all locks at once.
 - No preemption: Don't allow resources to be preempted. Once a transaction acquires a resource, it holds it until commit/abort.
- Deadlock Avoidance: Before a transaction acquires a new lock, it checks if it will result in a deadlock using the wait-for graph. If deadlock will occur, do not grant the lock. Choose another available lock or abort one of the waiting transactions.

The content covers the key points regarding deadlock handling namely deadlock, deadlock detection algorithms and deadlock prevention and avoidance techniques. The content is written in points and in a formal tone as requested. Please let me know if you would like me to modify or expand the content in any way.