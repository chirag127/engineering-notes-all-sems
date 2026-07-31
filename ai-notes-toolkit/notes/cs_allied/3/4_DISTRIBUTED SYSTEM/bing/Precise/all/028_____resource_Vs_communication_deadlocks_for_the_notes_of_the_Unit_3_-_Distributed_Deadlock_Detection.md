# Resource Vs Communication Deadlocks

## Unit 3 - Distributed Deadlock Detection

### Resource Deadlocks
- Resource deadlocks occur when two or more processes are blocked and waiting for resources held by the other processes.
- In a distributed system, resource deadlocks can occur when processes on different nodes request and hold resources on other nodes.
- Detection and resolution of resource deadlocks in a distributed system can be challenging due to the lack of a global view of the system.

### Communication Deadlocks
- Communication deadlocks occur when two or more processes are blocked and waiting for messages from the other processes.
- In a distributed system, communication deadlocks can occur when processes on different nodes are waiting for messages from each other.
- Detection and resolution of communication deadlocks in a distributed system can be challenging due to the lack of a global view of the system.

### Comparison
- Both resource and communication deadlocks can occur in a distributed system and can be challenging to detect and resolve.
- Resource deadlocks involve the blocking of processes due to the unavailability of resources, while communication deadlocks involve the blocking of processes due to the unavailability of messages.
- The methods for detecting and resolving resource and communication deadlocks may differ, but both require coordination and communication between the nodes in the distributed system.