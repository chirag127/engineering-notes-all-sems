### Concepts in Message Passing Systems for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Message passing is the interaction of exchanging messages between at least two processors.
- The process which is sending the message to another process is known as the sender and the process which is receiving the message is known as the receiver.
- In a message-passing system, we can send the message by using send function and we can receive the message by using receive function.
- Message passing is possible whenever the processors are in communication. The communication of a message can be established in distributed in two ways:
  - Interprocess communication (IPC)
  - Remote procedure call (RPC)
- Interprocess communication is a process of exchanging information between two independent processes in a distributed environment. Interprocess communication can be achieved using two strategies or approaches:
  - Original sharing (or) shared data approach
  - Copy sharing (or) message passing approach
- Remote procedure call is a powerful technique for building distributed client-server based applications. In RPC there is no need to change all the processors in the same memory location or address space. RPC is used widely to communicate the processors whenever they are in the different memory location in the same system or in a different system in the distributed system. The process which needs to access the service is known as the client process or “caller”. The process which provides the services is known as the server process, or “callee”.
- The formal model for distributed message passing has two timing models:
  - Synchronous: The sender and the receiver processes are synchronized by the message passing primitives. The sender blocks until the message is delivered and the receiver blocks until the message is available.
  - Asynchronous: The sender and the receiver processes are not synchronized by the message passing primitives. The sender does not block after sending the message and the receiver does not block if the message is not available.
- The message passing system should have the following features:
  - Simplicity: The message-passing system should be simple, easy, and user-friendly. It should be easy to build the applications and to communicate with existing applications & new applications by using primitives provided by the message passing system. It should also be possible for a developer to divide various modules of the distributed application and to send and receive the message between them in a way as simple as possible without the need to worry about the network and are network aspects.
  - Uniform semantics: In a distributed system the message can be passed in two ways:
    - Local communication, where the communicating processes are located on the same node.
    - Remote communication, in which the communication activities are distributed among multiple nodes.
    Whenever we are using the remote procedure call system we should use 2 semantics one is at:
    - Client machine
    - Server machine
    Both the semantics should be similar to get good communication among the process.
  - Efficiency: Efficiency is a crucial task in the distributed message-passing system. The message-passing system should be efficient in terms of:
    - Time: The message-passing system should minimize the time required to send and receive the messages between the processes.
    - Space: The message-passing system should minimize the space required to store the messages in the buffers or queues.
  - Reliability: Reliability is the ability of the message-passing system to deliver the messages correctly and consistently. The message-passing system should ensure that:
    - No message is lost or duplicated
    - No message is corrupted or modified
    - No message is delivered out of order
    - No message is delivered to the wrong process
  - Corrections: Corrections are the mechanisms to handle the errors or faults that may occur in the message-passing system. The message-passing system should provide the following corrections:
    - Error detection: The message-passing system should be able to detect the errors or faults that may occur in the message transmission or reception.
    - Error recovery: The message-passing system should be able to recover from the errors or faults that may occur in the message transmission or reception. This may involve retransmitting the message, requesting for acknowledgment, or using backup channels.
    - Error