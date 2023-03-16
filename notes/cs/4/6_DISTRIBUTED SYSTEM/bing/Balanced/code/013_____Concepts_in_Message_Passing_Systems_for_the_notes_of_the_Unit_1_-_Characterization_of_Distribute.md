### Concepts in Message Passing Systems

- Message passing is a technique for invoking behavior on a computer by sending and receiving messages over a communication channel.
- Message passing systems provide a collection of message-based inter-process communication (IPC) protocols that hide the complexities of network protocols and heterogeneous platforms.
- Message passing can be used for two forms of IPC in distributed systems: local communication and distant communication.
- Local communication occurs when the communicating processes are located on the same node, and distant communication occurs when the processes are distributed among multiple nodes.
- Message passing can be synchronous or asynchronous, depending on the timing model of the system.
- Synchronous message passing assumes that there is a known bound on the message transmission time and the process execution time, and that the processes are synchronized by a global clock.
- Asynchronous message passing does not make any assumptions about the message transmission time and the process execution time, and that the processes are not synchronized by a global clock.
- Message passing can be unicast, multicast, or broadcast, depending on the number of recipients of the message.
- Unicast message passing sends a message to a single destination, multicast message passing sends a message to a subset of destinations, and broadcast message passing sends a message to all destinations.
- Message passing can be reliable or unreliable, depending on the guarantees of the message delivery.
- Reliable message passing ensures that every message sent by a process is eventually received by the intended recipient, and that the messages are received in the same order as they were sent.
- Unreliable message passing does not provide any guarantees of the message delivery, and that the messages may be lost, duplicated, or reordered.
- Message passing can be blocking or non-blocking, depending on the behavior of the sender and the receiver.
- Blocking message passing requires the sender to wait until the message is received by the destination, and the receiver to wait until a message is available from the source.
- Non-blocking message passing allows the sender to continue without waiting for the message delivery, and the receiver to check for the availability of a message without waiting.
- Message passing can be implemented using various methods, such as sockets, message queues, remote procedure calls, remote method invocation, publish-subscribe systems, etc  .