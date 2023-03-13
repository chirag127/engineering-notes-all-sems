### Resource vs Communication Deadlocks for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- A deadlock is a condition where a process cannot proceed because it needs to obtain a resource held by another process, and it itself is holding a resource that the other process needs.
- Four requirements must be met for a deadlock to occur:
  - Mutual exclusion: Each resource can be assigned to only one process at a time.
  - Hold and wait: A process holding at least one resource can request additional resources.
  - No preemption: A resource can be released only by the process that holds it.
  - Circular wait: There exists a set of processes such that each process is waiting for a resource held by the next process in the set.
- In distributed systems, deadlocks can be classified into two types :
  - Resource deadlocks: These occur when processes access resources, such as data objects in database systems and buffers in store and forward communication networks. A process acquires a resource before accessing it and releasing it after using it.
  - Communication deadlocks: These occur when processes exchange messages, such as in remote procedure calls and message passing systems. A process sends a message to another process and waits for a reply before continuing.
- The main difference between resource and communication deadlocks is that in resource deadlocks, the resources are explicitly acquired and released by the processes, whereas in communication deadlocks, the resources are implicitly allocated and deallocated by the communication system .
- Another difference is that in resource deadlocks, the processes are aware of the resources they need and request, whereas in communication deadlocks, the processes are unaware of the messages they need and receive .
- A third difference is that in resource deadlocks, the processes can release the resources they hold voluntarily, whereas in communication deadlocks, the processes cannot release the messages they hold until they receive a reply .
- A fourth difference is that in resource deadlocks, the resources are usually reusable and can be shared by multiple processes, whereas in communication deadlocks, the messages are usually consumable and can be used by only one process .
- A fifth difference is that in resource deadlocks, the processes can detect the deadlock by examining the resource allocation graph, whereas in communication deadlocks, the processes cannot detect the deadlock by examining the message dependency graph .
- A sixth difference is that in resource deadlocks, the deadlock can be resolved by aborting or preempting some processes, whereas in communication deadlocks, the deadlock can be resolved by sending or receiving some messages .

- A possible mnemonic to remember the differences between resource and communication deadlocks is:

  - **R**esource deadlocks are **R**equested and **R**eleased by the processes, while communication deadlocks are **C**reated and **C**leared by the communication system.
  - **R**esource deadlocks are **R**eusable and **R**eal, while communication deadlocks are **C**onsumable and **C**oncealed.
  - **R**esource deadlocks can be **R**esolved by **R**emoving some processes, while communication deadlocks can be **C**ured by **C**ommunicating some messages.