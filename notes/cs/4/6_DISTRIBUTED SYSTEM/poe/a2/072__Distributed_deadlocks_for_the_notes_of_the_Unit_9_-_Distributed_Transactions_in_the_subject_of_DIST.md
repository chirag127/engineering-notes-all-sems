 Here is the content in markdown format without any emojis or external links, in a formal tone with points:

### Distributed deadlocks for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

1. Deadlocks can occur in distributed systems when multiple processes need to access resources (locks) located at different sites.
2. For example, process P1 has a lock on resource R1 at site S1 and is waiting to acquire a lock on resource R2 at site S2. Meanwhile, process P2 has a lock on resource R2 at site S2 and is waiting to acquire a lock on resource R1 at site S1.
3. This results in a deadlock as both processes wait forever.
4. Deadlocks are more complex to detect and resolve in distributed systems compared to centralized systems as the state information of all resources and processes may not be available globally.
5. Prevention approaches like resource ordering may not be applicable in distributed environments where global resource ordering is not feasible.
6. Detection and recovery from deadlocks requires additional protocol overhead to detect deadlocks and coordinate rollback and restart of processes to resolve the deadlock.

The above content outlines the key points about distributed deadlocks in a formal tone with points and without any emojis or external links for the given context. Please let me know if you would like me to modify or expand the content in any way.