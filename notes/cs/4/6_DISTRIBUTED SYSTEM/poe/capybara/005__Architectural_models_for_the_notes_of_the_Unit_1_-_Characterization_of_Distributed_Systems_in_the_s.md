### Architectural Models for the Notes of Unit 1 - Characterization of Distributed Systems in the Subject of DISTRIBUTED SYSTEM

Distributed Systems are systems that work across multiple nodes, communicating with each other to provide a unified service. These systems have become essential for many organizations to operate efficiently. One of the key factors that make distributed systems so popular is their ability to scale horizontally. However, designing and building a distributed system is not an easy task. In this unit, we will explore the different architectural models used in distributed systems.

#### 1. Client-Server Model
This is the most common architectural model used in distributed systems. In this model, the system is divided into two main components: the client and the server. The client sends a request to the server, and the server responds to the request. The communication between the client and the server can happen over different protocols, such as HTTP, TCP, or UDP. This model is suitable for systems that have a large number of clients and require a centralized server to manage the resources.

#### 2. Peer-to-Peer Model
In this model, all nodes have the same capabilities and can communicate with each other directly, without the need for a centralized server. Each node in the system can act as a client or a server, depending on the task at hand. This model is suitable for systems that require high availability and fault tolerance.

#### 3. Three-Tier Model
This model is also known as the n-tier model. In this model, the system is divided into three main components: the presentation layer, the application layer, and the database layer. The presentation layer interacts with the user interface, the application layer contains the business logic, and the database layer stores the data. This model is suitable for systems that require complex business logic and have a large amount of data to store.

#### 4. Service-Oriented Architecture (SOA)
In this model, the system is divided into individual services that are loosely coupled and can communicate with each other over standard protocols, such as HTTP or SOAP. Each service can be developed, deployed, and managed independently. This model is suitable for systems that require flexibility and scalability.

#### 5. Microservices Architecture
This model is similar to SOA, but instead of having a few large services, the system is divided into many small, independently deployable services. Each service is responsible for a specific task and can communicate with other services over standard protocols. This model is suitable for systems that require high scalability and fault tolerance.

In conclusion, selecting the right architectural model for a distributed system is critical for its success. Each model has its strengths and weaknesses, and the selection should be based on the requirements of the system. Understanding the different architectural models is essential for designing and building a distributed system that can scale, perform, and be reliable.