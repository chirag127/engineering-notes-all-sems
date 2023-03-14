### Concepts in Message Passing Systems for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

In distributed systems, message passing is a fundamental concept that allows different nodes to communicate and exchange information with each other. In this context, message passing refers to the process of sending and receiving messages between nodes in a distributed system. Here are some key concepts related to message passing systems in distributed systems:

1. Message: A message is a unit of information that is sent between nodes in a distributed system. Messages can be of different types such as request messages, response messages, error messages, etc. Messages may also contain some data or payload that needs to be transmitted from one node to another.

2. Message Queues: In message passing systems, messages are stored in a message queue until they are delivered to the intended recipient. A message queue is a data structure that holds messages in a first-in-first-out (FIFO) order.

3. Message Oriented Middleware (MOM): Message Oriented Middleware is a software layer that provides an infrastructure for message passing between different nodes in a distributed system. MOM is responsible for managing message queues, routing messages to their intended recipients, and ensuring message delivery.

4. Synchronous vs Asynchronous Message Passing: In synchronous message passing, the sender node waits for a response from the receiver node before continuing its execution. In contrast, in asynchronous message passing, the sender node does not wait for a response and continues its execution immediately after sending the message.

5. Remote Procedure Call (RPC): Remote Procedure Call is a technique that allows a program running on one node to call a procedure or function running on another node in a distributed system. RPC is often used in message passing systems to provide a more convenient and transparent way of invoking remote procedures.

6. Publish/Subscribe Messaging: Publish/Subscribe Messaging is a messaging pattern where publishers send messages to a topic or channel, and subscribers receive messages from that topic or channel. This pattern is often used in distributed systems where multiple nodes need to receive the same message.

7. Message Serialization: In message passing systems, messages need to be serialized before they can be transmitted over the network. Serialization is the process of converting a message into a binary format that can be transmitted over the network. Deserialization is the process of converting the binary data back into a message.

Mnemonics and learning tricks:
- Remember the acronym "MOM" for Message Oriented Middleware.
- Think of synchronous message passing as a phone call where you wait for the other person to answer before speaking, and asynchronous message passing as sending a text message where you don't wait for a response.
- For Publish/Subscribe Messaging, think of a newspaper where publishers publish articles on specific topics, and subscribers can choose which topics they want to read.