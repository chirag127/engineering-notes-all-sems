### Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

Distributed systems are complex systems that consist of multiple interconnected components that work together to perform a particular task. These systems are used in a variety of applications, including cloud computing, peer-to-peer networking, and distributed databases. In this unit, we will discuss the fundamental models that are used to characterize distributed systems. These models are:

1. Client-Server Model:
   - This model is the most common model for distributed systems.
   - In this model, the system is divided into two parts: the client and the server.
   - The client sends requests to the server, and the server responds to those requests.
   - The client and server can be located on different machines connected over a network.

2. Peer-to-Peer Model:
   - In this model, all the nodes in the system are equal, and there is no central server.
   - Each node can act as both a client and a server.
   - Nodes communicate with each other directly, without the need for a central server.
   - Peer-to-peer networks are often used for file sharing and content distribution.

3. Hybrid Model:
   - This model is a combination of the client-server and peer-to-peer models.
   - It is used when some nodes in the system have more resources than others.
   - The nodes with more resources act as servers, while the nodes with fewer resources act as clients.

4. Message-Passing Model:
   - In this model, nodes communicate with each other by sending messages.
   - Messages can be sent asynchronously, which means that the sender does not have to wait for a response from the receiver.
   - This model is often used in distributed systems that require high levels of concurrency.

5. Event-Based Model:
   - In this model, nodes communicate with each other by sending events.
   - An event is a notification that something has happened in the system.
   - Nodes can subscribe to events and receive notifications when they occur.
   - This model is often used in distributed systems that require real-time processing and event-driven architectures.

Understanding these fundamental models is essential for designing and building distributed systems. Each model has its strengths and weaknesses, and choosing the right model for a particular application requires careful consideration of the system's requirements and constraints.