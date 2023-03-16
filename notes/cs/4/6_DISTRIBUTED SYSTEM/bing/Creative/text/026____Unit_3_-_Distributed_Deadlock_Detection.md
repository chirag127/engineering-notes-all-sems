## Unit 3 - Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems.
- Deadlock detection in distributed systems entails addressing two basic issues: detection of existing deadlocks and resolution of detected deadlocks.
- Deadlock detection requires examination of the status of process-resource interactions for presence of cyclic wait.
- There are three approaches to detect deadlocks in distributed systems: global wait-for graph, edge chasing, and probe-based.
- Global wait-for graph: A deadlock detector collects local wait-for graphs from all sites and constructs a global wait-for graph. A cycle in the global wait-for graph indicates a deadlock.
- Edge chasing: A deadlock detector initiates a probe message along the edges of the local wait-for graph. A probe message that returns to the initiator indicates a deadlock.
- Probe-based: A deadlock detector periodically sends a probe message to each process. A process that receives a probe message replies with its status and forwards the message to its successor. A deadlock is detected if a process does not reply or if a probe message is lost.
- To resolve a deadlock, one or more deadlocked processes have to be aborted. The selection of processes to abort can be based on criteria such as priority, cost, or rollback distance.