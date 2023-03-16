### Concepts in Message Passing Systems for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Message passing is a technique for invoking behavior on a computer by sending messages from one process to another.
- Message passing systems are subsystems of distributed operating systems that provide a set of message-based interprocess communication (IPC) protocols.
- Message passing systems can be classified into two types: synchronous and asynchronous.
  - Synchronous message passing systems require the sender and the receiver to be ready at the same time for communication. The sender blocks until the receiver acknowledges the message, and the receiver blocks until a message arrives.
  - Asynchronous message passing systems do not require the sender and the receiver to be ready at the same time for communication. The sender does not block after sending a message, and the receiver does not block if no message is available.
- Message passing systems can also be classified into two types: direct and indirect.
  - Direct message passing systems require the sender and the receiver to know each other's identities. The sender specifies the destination process and the receiver specifies the source process in the message.
  - Indirect message passing systems do not require the sender and the receiver to know each other's identities. The sender and the receiver communicate through a shared data structure, such as a queue, a mailbox, or a topic.
- Message passing systems can have different features, such as reliability, ordering, multicasting, and security.
  - Reliability refers to the ability of the message passing system to deliver messages without loss, duplication, or corruption.
  - Ordering refers to the ability of the message passing system to preserve the temporal or causal relationships among messages.
  - Multicasting refers to the ability of the message passing system to send a message to multiple destinations at once.
  - Security refers to the ability of the message passing system to protect messages from unauthorized access, modification, or disclosure.
- Message passing systems can face different challenges, such as network failures, message fragmentation, message buffering, and message routing.
  - Network failures refer to the possibility of the communication link between the sender and the receiver being disrupted or unavailable.
  - Message fragmentation refers to the possibility of the message being too large to fit in a single network packet and having to be split into smaller pieces.
  - Message buffering refers to the possibility of the message being stored temporarily in the sender, the receiver, or an intermediate node until it can be delivered or processed.
  - Message routing refers to the possibility of the message having to traverse multiple nodes or paths to reach its destination.