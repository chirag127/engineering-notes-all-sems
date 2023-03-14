### Causal ordering of messages for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

In a distributed system, multiple processes communicate with each other by exchanging messages. The order in which these messages are delivered to the processes can have a significant impact on the correctness of the system. Causal ordering of messages is a technique used to ensure that the messages are delivered in a causally consistent order. 

In causal ordering, the message delivery order is based on the causal relationship between the sending and receiving processes. A message is considered causally related to another message if it is dependent on the outcome of the other message. For example, if a process receives a message that contains the result of a computation that was initiated by another message, then the receiving process is causally dependent on the sending process.

To ensure causal ordering, each message is associated with a vector timestamp that captures the causal relationship between the message and all the other messages in the system. The vector timestamp is a vector with an entry for each process in the system. Each entry in the vector represents the local time of the corresponding process when the message was sent. 

When a process receives a message, it compares the vector timestamp of the received message with its own local vector timestamp. If the received message is causally related to the process, then the process updates its local vector timestamp to reflect the causal relationship and delivers the message. If the received message is not causally related, then the process buffers the message until all the causally preceding messages have been received.

Causal ordering has several advantages, including:

- Ensuring that the messages are delivered in a causally consistent order, which can help to maintain the correctness of the system.
- Avoiding the need for global synchronization, which can be expensive and can reduce the scalability of the system.
- Allowing the system to handle concurrent updates to shared data without the need for locking, which can improve the performance of the system.

However, causal ordering also has some disadvantages, including:

- The need to maintain vector timestamps for each message, which can increase the overhead of the system.
- The possibility of message buffering if a process receives messages out of order, which can increase the latency of the system.

A mnemonic to remember the concept of causal ordering is "Cause and effect." In this way, we can remember that the order of message delivery is based on the causal relationship between the messages. 

Example:

Consider a distributed system with three processes: P1, P2, and P3. Assume that P1 sends a message M1 to P2, which in turn sends a message M2 to P3. The vector timestamps associated with these messages are:

- M1: [1,0,0]
- M2: [1,2,0]

When P2 receives M1, it updates its local vector timestamp to [2,0,0] and sends M2. When P3 receives M2, it updates its local vector timestamp to [2,3,0] and delivers the message.

Application:

Causal ordering is used in many distributed systems, such as databases, messaging systems, and collaborative editing systems. It can help to ensure the consistency of shared data and can improve the performance of the system by allowing concurrent updates without the need for locking.