# Concepts in Message Passing Systems

- Message passing is a technique for invoking behavior on a computer by sending a message to a process.
- Message passing is used in distributed systems, where processes communicate by exchanging messages over a network  .
- Message passing systems provide a collection of message-based interprocess communication (IPC) protocols that hide the complexities of network protocols and heterogeneous platforms  .
- Message passing systems can be classified into two categories: synchronous and asynchronous .
  - Synchronous message passing systems require the sender and the receiver to be ready at the same time for communication. The sender blocks until the receiver acknowledges the message, and the receiver blocks until a message arrives .
  - Asynchronous message passing systems do not require the sender and the receiver to be ready at the same time for communication. The sender does not block after sending a message, and the receiver does not block if no message is available. Instead, messages are stored in buffers or queues until they are delivered .
- Message passing systems can also be classified into two types: direct and indirect .
  - Direct message passing systems require the sender and the receiver to explicitly name each other in the communication. A communication link must be established between the cooperating processes before messages can be sent .
  - Indirect message passing systems do not require the sender and the receiver to explicitly name each other in the communication. Instead, messages are sent and received through a shared entity called a mailbox or a port. A communication link is established implicitly by the processes accessing the same mailbox or port .
- Message passing systems can also be distinguished by the format and structure of the messages they support .
  - Fixed-format messages have a predefined size and layout, and are easy to implement and efficient to transmit. However, they are less flexible and expressive than variable-format messages .
  - Variable-format messages have a variable size and layout, and can contain different types of data and metadata. They are more flexible and expressive than fixed-format messages, but they are harder to implement and less efficient to transmit .
- Message passing systems can also be characterized by the reliability and ordering of the messages they deliver .
  - Reliable message passing systems guarantee that every message sent by a process will eventually be received by the intended recipient, without duplication or corruption .
  - Unreliable message passing systems do not guarantee that every message sent by a process will eventually be received by the intended recipient, or that the messages will be delivered without duplication or corruption .
  - Ordered message passing systems guarantee that messages sent by a process will be received by the intended recipient in the same order as they were sent .
  - Unordered message passing systems do not guarantee that messages sent by a process will be received by the intended recipient in the same order as they were sent .
- Message passing systems can also be evaluated by the features and properties they offer, such as scalability, performance, security, fault tolerance, transparency, and interoperability  .