## Unit 3 - Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set, and none of the processes can proceed.
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems.
- Deadlock detection in distributed systems entails addressing two basic issues: detection of existing deadlocks and resolution of detected deadlocks.
- Deadlock detection requires examination of the status of process-resource interactions for presence of cyclic wait.
- There are three approaches to detect deadlocks in distributed systems: global wait-for graph, edge chasing, and probe-based.
- Global wait-for graph: A deadlock detector collects local wait-for graphs from all sites and constructs a global wait-for graph. A cycle in the global wait-for graph indicates a deadlock.
- Edge chasing: A deadlock detector initiates a probe message along the edges of the local wait-for graph. If the probe message returns to the initiator, a deadlock is detected.
- Probe-based: A deadlock detector periodically sends a probe message to each process. The probe message contains the identifier of the sender and a timestamp. If a process receives a probe message with its own identifier or a smaller timestamp, it detects a deadlock.
- To resolve the deadlock, one or more deadlocked processes have to be aborted. The selection of the victim process can be based on criteria such as priority, execution time, number of resources, etc.