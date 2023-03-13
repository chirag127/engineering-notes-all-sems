### Concepts in Message Passing Systems

- Message passing is a technique for invoking behavior (i.e., running a program) on a computer.
- In message passing, processes exchange data by sending and receiving messages using only two operations: send and receive.
- Message passing systems use system calls for “send message” and “receive message”.
- A communication link must be established between the cooperating processes before messages can be sent.
- The collection of the channels are called a network.
- The pattern of the connection provided by the channel is described by some topology systems.
- Message passing systems can be classified into two types: synchronous and asynchronous.
- In synchronous message passing, the sender and the receiver must be synchronized, i.e., the sender must wait for the receiver to receive the message, and the receiver must wait for the sender to send the message.
- In asynchronous message passing, the sender and the receiver are not synchronized, i.e., the sender can send the message and continue its execution, and the receiver can receive the message at any time.
- Message passing systems can also be classified into two types: direct and indirect.
- In direct message passing, the sender and the receiver must explicitly name each other, i.e., the sender must specify the identity of the receiver, and the receiver must specify the identity of the sender.
- In indirect message passing, the sender and the receiver do not explicitly name each other, i.e., they communicate through a shared data structure called a mailbox or a port.
- Message passing systems can be used in distributed systems, where processes are geographically set of computers.
- Message passing systems can also be used in parallel systems, where processes are executed on multiple processors or cores.
- Message passing systems are expressive, closely model the functionality of the parallel hardware, and permit explicit management of the memory hierarchy.
- Message passing systems have some advantages, such as simplicity, modularity, portability, scalability, and fault tolerance.
- Message passing systems also have some disadvantages, such as overhead, latency, deadlock, synchronization, and security.