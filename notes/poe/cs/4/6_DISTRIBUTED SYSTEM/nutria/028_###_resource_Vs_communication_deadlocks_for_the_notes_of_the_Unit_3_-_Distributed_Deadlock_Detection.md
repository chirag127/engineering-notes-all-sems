
### Resource Vs Communication Deadlocks for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of DISTRIBUTED SYSTEM

- **Resource Deadlock**: A resource deadlock occurs when two or more processes are waiting for each other to release a resource that each has already acquired.
- **Communication Deadlock**: A communication deadlock occurs when two or more processes are waiting for each other to send a message that each is expecting to receive.
- **Distributed Deadlock Detection**: Distributed deadlock detection is a technique used to identify and resolve deadlocks in distributed systems. It involves each process in the system sending messages to a central coordinator, which then detects and resolves any deadlocks that exist.
- **Mnemonics and Learning Tricks**: To remember the difference between resource and communication deadlocks, one can use the mnemonic "Resource Deadlocks are Like a Lock and Key, Communication Deadlocks are Like a Conversation". This mnemonic helps to remember that resource deadlocks are caused by a lack of resources, while communication deadlocks are caused by a lack of communication.

- **Advantages of Distributed Deadlock Detection**: 
  - It can detect deadlocks in a distributed system more quickly and reliably than manual methods.
  - It is more efficient than manual methods, since it can detect deadlocks without requiring the system to be stopped.
  - It can detect deadlocks in a system with a large number of processes.

- **Disadvantages of Distributed Deadlock Detection**:
  - It requires the system to have a central coordinator, which can be a single point of failure.
  - It requires the processes in the system to communicate with the central coordinator, which can be a source of additional overhead.
  - It can be difficult to implement in a system with a large number of processes.