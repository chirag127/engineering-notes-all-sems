# Unit 3 - Distributed Deadlock Detection

### Distributed Deadlock Detection

- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems.
- Deadlock detection in distributed systems seems to be the best approach to handle deadlocks in distributed systems.
- Deadlock handling using the approach of deadlock detection entails addressing two basic issues: First, detection of existing deadlocks and second resolution of detected deadlocks.
- In the deadlock avoidance approach to distributed systems, a resource is granted to a process if the resulting global system is safe.
- Deadlock detection requires an examination of the status of the process–resources interaction for the presence of a deadlock condition.
- To resolve the deadlock, we have to abort a deadlocked process.
- Distributed deadlocks can be detected either by constructing a global wait-for graph, from local wait-for graphs at a deadlock detector or by a distributed algorithm like edge chasing.
- Phantom deadlocks are deadlocks that are detected in a distributed system due to system internal delays but no longer actually exist at the time of detection.
