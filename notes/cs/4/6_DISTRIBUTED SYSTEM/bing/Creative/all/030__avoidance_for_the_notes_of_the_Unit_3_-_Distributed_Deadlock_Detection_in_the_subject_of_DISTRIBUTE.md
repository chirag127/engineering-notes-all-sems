### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a strategy that tries to ensure that the system will never enter an unsafe state, which is a state that could lead to deadlock.
- Deadlock avoidance requires some knowledge of the future resource requests and releases of each process, which may not be available or predictable in a distributed system.
- Deadlock avoidance algorithms can be classified into two categories: resource ordering and resource allocation.
- Resource ordering is a technique that imposes a global ordering on all the resources in the system and requires each process to request resources in increasing order of the global order. This prevents circular wait and thus deadlock.
- Resource ordering can be implemented by assigning a unique number to each resource and using a distributed algorithm to ensure that each process requests resources in ascending order of their numbers.
- Resource ordering has some drawbacks, such as:
  - It may impose unnecessary constraints on the processes and reduce concurrency.
  - It may not be feasible if the resources are not comparable or the global order is not known.
  - It may not be efficient if the resources are dynamically created or destroyed.
- Resource allocation is a technique that dynamically allocates resources to processes based on some criteria, such as the number of resources available, the number of resources requested, the priority of the processes, etc.
- Resource allocation can be implemented by using a centralized or a distributed algorithm to decide which process should get the requested resource.
- Resource allocation has some advantages, such as:
  - It can be more flexible and adaptable to the changing resource demands and system states.
  - It can be more efficient and fair in utilizing the resources.
- Resource allocation has some challenges, such as:
  - It may require a global view of the system state, which may be difficult or costly to obtain in a distributed system.
  - It may introduce communication and synchronization overheads among the processes and the resource managers.
  - It may be prone to errors or inconsistencies due to failures or delays in the system.
- A common resource allocation algorithm is the Banker's algorithm, which is based on the concept of a safe state.
- A safe state is a state where there exists a sequence of processes that can finish their execution without causing deadlock.
- The Banker's algorithm works as follows:
  - Each process declares its maximum resource needs in advance to the resource manager.
  - The resource manager maintains the current allocation and availability of each resource.
  - When a process requests a resource, the resource manager checks if granting the request will leave the system in a safe state.
  - If yes, the request is granted and the allocation and availability are updated.
  - If no, the request is denied and the process is blocked until some other process releases some resource.
- The Banker's algorithm can be extended to a distributed system by using a distributed resource manager that communicates with the local resource managers at each site.
- The distributed resource manager can use a global state detection algorithm to collect the global allocation and availability information from the local resource managers and determine the safe state of the system.
- The distributed resource manager can also use a distributed agreement protocol to coordinate the resource allocation decisions among the local resource managers and ensure consistency.
- The Banker's algorithm has some limitations, such as:
  - It requires the processes to declare their maximum resource needs in advance, which may not be possible or accurate in a dynamic system.
  - It may be conservative and deny some requests that could be granted without causing deadlock.
  - It may be complex and costly to implement in a distributed system due to the communication and synchronization overheads.

: Deadlock Detection in Distributed Systems - University of Illinois Chicago
: Prevention, Avoidance, and Detection of Deadlock | 5 | Distributed Sys
: Deadlock Avoidance in Distributed System - GeeksforGeeks