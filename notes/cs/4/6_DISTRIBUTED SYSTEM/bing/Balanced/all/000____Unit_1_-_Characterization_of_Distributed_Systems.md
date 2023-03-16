# Unit 1 - Characterization of Distributed Systems

A distributed system is a system in which components located at networked computers communicate and coordinate their actions only by passing messages . The components of a distributed system may be hardware devices, software processes, or data sources. The end-users of a distributed system perceive it as a single coherent system that provides some functionality .

Some of the main characteristics of distributed systems are:

- **Resource sharing**: The components of a distributed system can share resources such as hardware, software, or data with other components, either transparently or selectively . Resource sharing enables the system to achieve higher performance, scalability, and availability.
- **Openness**: The components of a distributed system can be easily extended and improved by adding new components or replacing existing ones, without affecting the rest of the system . Openness also implies that the system follows some standard protocols and interfaces for communication and interoperability.
- **Concurrency**: The components of a distributed system can execute concurrently, meaning that they can perform multiple tasks at the same time . Concurrency allows the system to exploit parallelism and increase efficiency and responsiveness.
- **Lack of a global clock**: The components of a distributed system do not have a common notion of time, as they may have different local clocks that are not synchronized . This makes it difficult to coordinate the actions of the components and to order the events that occur in the system.
- **Independent failures**: The components of a distributed system can fail independently, without affecting the whole system . This means that the system has to cope with partial failures and ensure fault tolerance and reliability.

Some of the main challenges of distributed systems are:

- **Heterogeneity**: The components of a distributed system may have different hardware architectures, operating systems, programming languages, or network protocols . This makes it hard to ensure compatibility and interoperability among the components and to provide a uniform interface to the end-users.
- **Security**: The components of a distributed system may be exposed to various threats such as unauthorized access, data tampering, denial of service, or malicious attacks . This requires the system to implement mechanisms for authentication, authorization, encryption, and auditing.
- **Scalability**: The components of a distributed system may have to handle a large number of requests, users, or data, which may vary over time . This demands the system to adapt to the changing load and to maintain acceptable performance and quality of service.
- **Transparency**: The components of a distributed system should hide their complexity and heterogeneity from the end-users and provide them with a consistent and coherent view of the system . Transparency can be achieved at different levels, such as access, location, migration, replication, concurrency, or failure.
- **Consistency**: The components of a distributed system should provide the end-users with a consistent view of the data and the state of the system, despite the concurrency, replication, and failures that may occur . Consistency can be defined in different ways, such as sequential, causal, or eventual, depending on the application requirements and the trade-offs involved.