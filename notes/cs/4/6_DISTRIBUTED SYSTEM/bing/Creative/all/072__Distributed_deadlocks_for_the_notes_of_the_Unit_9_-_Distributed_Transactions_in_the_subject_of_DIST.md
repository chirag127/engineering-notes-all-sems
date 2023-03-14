### Distributed deadlocks for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- A distributed deadlock is a situation where a set of processes in a distributed system are blocked because each process is holding a resource and waiting for another resource occupied by some other process. 
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems.  
- There are two types of distributed deadlocks: resource deadlocks and communication deadlocks. 
- A resource deadlock occurs when two or more processes wait permanently for resources held by each other. A process that requires certain resources for its execution, and cannot proceed until it has acquired all those resources. 
- A communication deadlock occurs among a set of processes when they are blocked waiting for messages from other processes in the set in order to start execution but there are no messages in transit between them. 
- Distributed deadlocks can be detected either by constructing a global wait-for graph (WFG) from local wait-for graphs at a deadlock detector or by a distributed algorithm like edge chasing.   
- A WFG is a directed graph that represents the dependencies among processes and resources in a system. A node in a WFG can be either a process or a resource, and an edge from a process to a resource indicates that the process is holding the resource, while an edge from a resource to a process indicates that the process is waiting for the resource. A cycle in a WFG indicates a deadlock.  
- Edge chasing is a distributed algorithm that propagates probe messages along the edges of the WFG to detect cycles. A probe message contains the identity of the initiator process and a list of visited processes. When a process receives a probe message, it checks if it is the initiator or if it has already been visited by the probe. If so, it reports a deadlock to the initiator. Otherwise, it appends its identity to the list and forwards the probe to the next process in the WFG.  

#### Mnemonics and learning tricks

- To remember the four conditions for deadlock, use the acronym **MUCH**:

  - **M**utual exclusion: only one process can use a resource at a time.
  - **U**tilization: a process holds a resource while waiting for another resource.
  - **C**ircular wait: a cycle of processes waiting for resources held by each other.
  - **H**old and wait: a process does not release a resource until it gets all the resources it needs.

- To remember the difference between resource deadlock and communication deadlock, use the analogy of **AND** and **OR**:

  - Resource deadlock is like an **AND** condition: a process needs all the resources it requests to proceed.
  - Communication deadlock is like an **OR** condition: a process needs at least one message from another process to proceed.

- To remember the difference between global WFG and edge chasing, use the analogy of **centralized** and **distributed**:

  - Global WFG is a **centralized** approach: a single deadlock detector collects and analyzes the local WFGs from all the processes.
  - Edge chasing is a **distributed** approach: each process participates in the detection by sending and receiving probe messages.