### Concepts in Message Passing Systems

- Message passing is a technique for invoking behavior (i.e., running a program) on a computer.
- In message-passing systems, processors communicate with one another by sending and receiving messages over a communication channel.
- The pattern of the connection provided by the channel is described by some topology systems.
- The collection of the channels are called a network.
- A message-passing system gives a collection of message-based IPC protocols while sheltering programmers from the complexities of sophisticated network protocols and many heterogeneous platforms.
- A message-passing mechanism can be used in a distributed system for the following two forms of inter-process communication:
  - Local communication, where the communicating processes are located on the same node.
  - Distant communication, in which the communication activities are distributed among multiple nodes.
- The formal model for distributed message passing has two timing models:
  - Synchronous, where there are known bounds on the message transmission time, the processing time, and the clock drift rate.
  - Asynchronous, where there are no such bounds and the processes may operate at arbitrary speeds.
- Message passing can be classified into two types:
  - Blocking, where the sender and the receiver are blocked until the message is delivered.
  - Non-blocking, where the sender and the receiver can proceed without waiting for the message delivery.
- Message passing can also be classified into two modes:
  - Point-to-point, where the message is sent from one specific process to another specific process.
  - Broadcast, where the message is sent from one process to all other processes in the system.