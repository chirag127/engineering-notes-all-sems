### Concepts in Message Passing Systems

- Message passing is a technique for invoking behavior (i.e., running a program) on a computer.
- In message-passing systems, processors communicate with one another by sending and receiving messages over a communication channel.
- The pattern of the connection provided by the channel is described by some topology systems.
- The collection of the channels are called a network.
- A distributed system consists of multiple components, possibly across geographical boundaries, that communicate and coordinate their actions through message passing.
- A message-passing system gives a collection of message-based IPC protocols while sheltering programmers from the complexities of sophisticated network protocols and many heterogeneous platforms.
- A message-passing mechanism can be used in a distributed system for the following two forms of inter-process communication:
  - Local communication, where the communicating processes are located on the same node.
  - Distant communication, in which the communication activities are distributed among multiple nodes.
- The formal model for distributed message passing has two timing models:
  - Synchronous, where the sender and receiver processes are synchronized by the message passing, and the message delivery time is bounded and known.
  - Asynchronous, where the sender and receiver processes are independent of each other, and the message delivery time is unbounded and unknown.