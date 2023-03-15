### Concepts in Message Passing Systems for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

A message passing system is a type of inter-process communication system that enables processes to communicate with each other by sending and receiving messages. The following are the important concepts in message passing systems:

1. Message: A message is a unit of data that is sent from one process to another. It contains information that is to be communicated between processes.

2. Sender and Receiver: In a message passing system, there are two entities involved, the sender and the receiver. The sender is the process that sends the message, and the receiver is the process that receives the message.

3. Communication Channel: A communication channel is a medium through which messages are sent from the sender to the receiver. It can be a physical medium such as a network cable or a logical medium such as a shared memory.

4. Synchronous and Asynchronous Communication: In synchronous communication, the sender and the receiver synchronize the sending and receiving of messages. In asynchronous communication, the sender sends the message and continues its execution without waiting for a response from the receiver.

5. Message Queuing: Message queuing is the process of storing messages in a queue until they are delivered to the receiver. This is useful when the receiver is not available at the time the message is sent.

6. Message Passing Interface (MPI): MPI is a standardized message passing system that enables processes to communicate with each other in distributed systems. It is widely used in scientific and engineering applications.

7. Remote Procedure Call (RPC): RPC is a technique that allows a process to call a procedure on another process that is running on a remote machine. It is a form of message passing that is commonly used in client-server applications.

8. Message-Oriented Middleware (MOM): MOM is a software layer that provides message passing services between applications. It enables distributed applications to communicate with each other by exchanging messages.

Overall, understanding the concepts of message passing systems is important for designing and implementing distributed systems. These concepts form the basis for many communication protocols and middleware systems that are used in distributed computing. Mnemonic: My Six Red Messages Really Mean More