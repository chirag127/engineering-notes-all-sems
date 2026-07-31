### Detection & Resolution for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of DISTRIBUTED SYSTEM

In distributed systems, deadlocks can occur due to the presence of multiple resources and processes that require those resources. Deadlocks can cause the entire system to become unresponsive and can have a significant impact on the system's overall performance. Therefore, it is crucial to detect and resolve deadlocks in distributed systems. 

Here are some important points related to the detection and resolution of deadlocks in distributed systems:

#### Detection of Deadlocks

1. Resource Allocation Graph (RAG) is a commonly used method to detect deadlocks in distributed systems.
2. In RAG, nodes represent resources, and edges represent the allocation of resources to processes.
3. The cycle in RAG indicates the presence of a deadlock in the system.
4. Another commonly used method for deadlock detection is the Distributed Deadlock Detection (DDD) algorithm.
5. In DDD, each node maintains information about the resources it holds and the resources it is waiting for.
6. If a node detects a cycle in the system, it sends a message to other nodes to check if they are also part of the cycle.
7. If all the nodes confirm the cycle, then the system is in deadlock.

#### Resolution of Deadlocks

1. After detecting a deadlock, the system needs to resolve it to restore its normal functioning.
2. One common method for deadlock resolution is to abort one or more processes involved in the deadlock.
3. However, aborting a process can lead to loss of data or can impact the system's overall performance.
4. Another method for deadlock resolution is to use the concept of preemption, where resources are temporarily taken away from a process to allow other processes to complete their tasks.
5. The preemption method requires the system to have a mechanism to save the state of the process, which can be restored once the process regains the resources.
6. In distributed systems, the preemption method can be challenging to implement because of the need to coordinate the actions of multiple nodes.

Overall, detecting and resolving deadlocks in distributed systems is an essential aspect of ensuring the system's smooth functioning. Various methods and algorithms can be used for deadlock detection and resolution, and the choice of the method depends on the system's requirements and constraints.