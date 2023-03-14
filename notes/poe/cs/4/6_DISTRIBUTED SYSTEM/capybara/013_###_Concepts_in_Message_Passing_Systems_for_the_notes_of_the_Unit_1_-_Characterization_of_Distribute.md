### Concepts in Message Passing Systems for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

Message passing is a fundamental concept in distributed systems. In this section, we will discuss the concepts in message passing systems for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM. 

Here are the important concepts you should be familiar with:

1. Message Passing: Message passing is a communication method used in distributed systems where processes communicate by sending messages. In this method, each process has its own address, and it sends messages to other processes by specifying their addresses.

2. Synchronous and Asynchronous Message Passing: In synchronous message passing, the sender process blocks until the receiver process receives the message. In asynchronous message passing, the sender process sends the message and continues its execution without waiting for the receiver process to receive the message.

3. Message Buffers: Message buffers are used to store messages when they are sent and received. They are implemented in the form of queues, stacks, or arrays.

4. Direct and Indirect Communication: In direct communication, the sender process specifies the receiver process's address when sending the message. In indirect communication, a message is sent to a mailbox or port, and the receiver process reads from that mailbox or port.

5. Message Ordering: The order in which messages are sent and received is crucial in distributed systems. Two types of message ordering are possible: FIFO (First-In-First-Out) and causal ordering.

6. Reliable Message Delivery: In distributed systems, there is a possibility that messages may not be delivered due to network failures, node failures, or other reasons. Reliable message delivery ensures that messages are delivered even in such scenarios.

7. Message Routing: In large-scale distributed systems, messages may need to be routed through multiple nodes before reaching the destination. Routing algorithms are used to determine the path that messages should take.

Mnemonics and Learning Tricks:

- Remember the acronym "SAM DIRM" to recall the important concepts in message passing systems: Synchronous and Asynchronous Message Passing, Message Buffers, Direct and Indirect Communication, Message Ordering, Reliable Message Delivery, and Message Routing.
- To remember the difference between direct and indirect communication, think of direct communication as sending a letter to someone's address, while indirect communication is leaving a message in a mailbox for someone to pick up later. 

In conclusion, understanding the concepts in message passing systems is essential in designing and implementing distributed systems. Remembering the key concepts and their differences can help you answer questions related to message passing on exams and in practical applications.