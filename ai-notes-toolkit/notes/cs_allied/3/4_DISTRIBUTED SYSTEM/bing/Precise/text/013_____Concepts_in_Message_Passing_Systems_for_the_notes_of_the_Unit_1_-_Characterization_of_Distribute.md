### Concepts in Message Passing Systems

1. **Message Passing Interface (MPI)**: MPI is a standardized and portable message-passing system designed to function on a wide variety of parallel computers. It is used for communication between processes in a distributed memory system.

2. **Point-to-Point Communication**: Point-to-point communication refers to the exchange of messages between two processes. This can be done synchronously, where the sender waits for the receiver to acknowledge the message, or asynchronously, where the sender does not wait for the receiver.

3. **Collective Communication**: Collective communication refers to the exchange of messages between a group of processes. This can include operations such as broadcast, where one process sends the same message to all other processes, or reduce, where all processes send data to one process, which then performs a reduction operation on the data.

4. **Deadlock**: Deadlock is a situation where two or more processes are blocked, waiting for each other to release resources. This can occur in message passing systems when processes are waiting for messages from each other.

5. **Buffering**: Buffering refers to the temporary storage of messages in a message passing system. This can be used to improve performance by allowing the sender to continue without waiting for the receiver, or to prevent deadlock by allowing messages to be received out of order.

6. **Routing**: Routing refers to the process of determining the path that a message will take between the sender and the receiver. This can be done statically, where the path is determined before the message is sent, or dynamically, where the path is determined as the message is being sent.

7. **Flow Control**: Flow control refers to the process of regulating the rate at which messages are sent in a message passing system. This can be used to prevent the receiver from being overwhelmed by incoming messages, or to prevent network congestion.

8. **Reliability**: Reliability refers to the ability of a message passing system to deliver messages correctly and in order. This can be achieved through the use of error detection and correction techniques, or through the use of retransmission protocols.

9. **Ordering**: Ordering refers to the order in which messages are delivered in a message passing system. This can be important in some applications, where the order of messages can affect the correctness of the computation.

10. **Group Communication**: Group communication refers to the exchange of messages between a group of processes. This can include operations such as multicast, where one process sends the same message to a group of processes, or gather, where all processes in a group send data to one process, which then collects the data.