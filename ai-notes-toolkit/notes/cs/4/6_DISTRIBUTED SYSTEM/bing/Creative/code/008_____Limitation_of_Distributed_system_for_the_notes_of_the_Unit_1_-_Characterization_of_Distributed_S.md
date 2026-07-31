Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the limitation of distributed system for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Limitation of Distributed System

A distributed system is a system that consists of multiple independent components that communicate with each other over a network. Distributed systems have many advantages, such as scalability, reliability, availability, and performance. However, they also face some challenges and limitations, such as:

- **Absence of a global state**: In a distributed system, there is no single point of control or coordination for the entire system. Each component has its own local state and view of the system, which may differ from other components. This makes it difficult to achieve consistency, synchronization, and agreement among the components. For example, it is hard to determine the total number of users or transactions in a distributed system, or to ensure that all components have the same version of the data.  

- **Absence of a global clock**: In a distributed system, there is no common notion of time or order of events among the components. Each component has its own local clock, which may drift or be inaccurate. This makes it difficult to measure the duration of events, to coordinate actions, and to detect causality and concurrency. For example, it is hard to determine if an event A happened before or after an event B in a distributed system, or to ensure that all components execute a task at the same time. 

- **Network issues**: In a distributed system, the communication between the components depends on the underlying network, which may be unreliable, unpredictable, or insecure. The network may experience delays, failures, congestion, or attacks, which may affect the availability, performance, and correctness of the system. For example, a message sent by a component may be lost, duplicated, corrupted, or delayed by the network, or a component may be isolated from the rest of the system due to a network partition.  

- **Security issues**: In a distributed system, the components may not trust each other or the network, as they may be exposed to malicious or unauthorized actions. The system may face threats such as eavesdropping, tampering, spoofing, denial-of-service, or intrusion, which may compromise the confidentiality, integrity, or availability of the system. For example, an attacker may intercept, modify, or forge a message sent by a component, or may launch a distributed denial-of-service attack to overwhelm the system.  

These limitations of distributed system have an impact on both the design and the implementation of the system, and require the use of various techniques and algorithms to overcome them, such as consensus, replication, fault tolerance, distributed transactions, distributed locking, cryptography, authentication, and authorization.   
