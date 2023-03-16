# Concepts in Message Passing Systems

- Message passing is a technique for invoking behavior on a computer by sending a message to a process.
- Message passing is used in distributed systems, where processes communicate by exchanging messages over a network .
- Message passing systems provide a set of message-based interprocess communication (IPC) protocols that allow processes to send and receive messages .
- Message passing systems can be classified into two types: synchronous and asynchronous .
  - Synchronous message passing systems require the sender and the receiver to be ready at the same time for communication. The sender blocks until the receiver acknowledges the message, and the receiver blocks until a message arrives .
  - Asynchronous message passing systems do not require the sender and the receiver to be ready at the same time for communication. The sender does not block after sending a message, and the receiver does not block if no message is available. Messages are stored in a buffer or a queue until they are delivered .
- Message passing systems can also be classified into two modes: direct and indirect .
  - Direct message passing systems require the sender to specify the identity of the receiver, and the receiver to specify the identity of the sender. The communication link is established explicitly between the sender and the receiver .
  - Indirect message passing systems do not require the sender or the receiver to specify the identity of the other party. The communication link is established implicitly through a shared entity, such as a mailbox, a port, or a topic. The sender and the receiver can communicate anonymously or selectively .
- Message passing systems can also be classified into two styles: point-to-point and collective.
  - Point-to-point message passing systems involve communication between two processes. The sender sends a message to a specific receiver, and the receiver receives a message from a specific sender.
  - Collective message passing systems involve communication between a group of processes. The sender sends a message to all or some of the processes in the group, and the receiver receives a message from any or all of the processes in the group. Collective message passing systems can support operations such as broadcast, scatter, gather, and reduce.
- Message passing systems can also be classified into two standards: Message Passing Interface (MPI) and Remote Procedure Call (RPC).
  - MPI is a standardized and portable message-passing system developed for distributed and parallel computing. MPI provides parallel hardware vendors with a clearly defined base set of routines that can be efficiently implemented. MPI supports both synchronous and asynchronous, direct and indirect, point-to-point and collective message passing .
  - RPC is a message-passing system that allows a process to invoke a procedure or a function on a remote process. RPC hides the details of message passing and network communication from the programmer. RPC supports both synchronous and asynchronous, direct and indirect message passing.