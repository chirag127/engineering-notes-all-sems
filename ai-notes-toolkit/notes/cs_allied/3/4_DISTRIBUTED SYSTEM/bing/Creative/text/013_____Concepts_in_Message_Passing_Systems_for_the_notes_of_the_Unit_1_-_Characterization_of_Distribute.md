### Concepts in Message Passing Systems for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Message passing is a technique for invoking behavior on a computer by sending messages from one process to another.
- Message passing systems are subsystems of distributed operating systems that provide a set of message-based interprocess communication (IPC) protocols.
- Message passing systems can be classified into two types: synchronous and asynchronous.
  - Synchronous message passing systems require the sender and the receiver to be ready at the same time for communication. The sender blocks until the receiver acknowledges the message, and the receiver blocks until a message arrives.
  - Asynchronous message passing systems do not require the sender and the receiver to be ready at the same time for communication. The sender does not block after sending a message, and the receiver does not block if no message is available. Instead, messages are stored in buffers or queues until they are delivered or retrieved.
- Message passing systems can also be classified into two types: direct and indirect.
  - Direct message passing systems require the sender and the receiver to know each other's identities or addresses. The sender specifies the destination of the message, and the receiver specifies the source of the message.
  - Indirect message passing systems do not require the sender and the receiver to know each other's identities or addresses. The sender and the receiver communicate through a shared entity, such as a mailbox, a port, a topic, or a channel. The sender specifies the name of the shared entity, and the receiver retrieves messages from the shared entity.
- Message passing systems can have different features, such as reliability, ordering, multicasting, and security.
  - Reliability refers to the ability of the message passing system to ensure that messages are delivered correctly and completely, without loss, duplication, or corruption.
  - Ordering refers to the ability of the message passing system to preserve the temporal or causal relationships among messages, such as FIFO, causal, or total ordering.
  - Multicasting refers to the ability of the message passing system to deliver a message to multiple receivers at once, such as broadcast, multicast, or anycast.
  - Security refers to the ability of the message passing system to protect the messages from unauthorized access, modification, or disclosure, such as encryption, authentication, or access control.
- Message passing systems can face different challenges, such as network heterogeneity, network failures, network congestion, and network latency.
  - Network heterogeneity refers to the diversity of the network architectures, protocols, and platforms that the message passing system has to support and interoperate with.
  - Network failures refer to the possibility of the network components, such as links, routers, or hosts, to malfunction or become unavailable, causing message loss, delay, or corruption.
  - Network congestion refers to the situation where the network traffic exceeds the network capacity, causing message queuing, retransmission, or dropping.
  - Network latency refers to the time it takes for a message to travel from the sender to the receiver, which can affect the performance and correctness of the message passing system.