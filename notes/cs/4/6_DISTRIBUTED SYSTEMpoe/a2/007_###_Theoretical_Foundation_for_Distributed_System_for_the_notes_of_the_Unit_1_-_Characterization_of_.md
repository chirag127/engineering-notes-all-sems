 Here is the content in markdown format for the topic ### Theoretical Foundation for Distributed System for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM:

### Theoretical Foundation for Distributed System

- A distributed system consists of multiple autonomous computers that communicate through a network.
- The computers in a distributed system may vary in size and function. They can be regular PCs, servers, supercomputers, etc.
- There is no shared memory between the computers. Each computer has its own local memory.
- Computations are distributed across the system, rather than confined to a single machine. This distribution introduces many new and complex issues into system design and operation.
- Some key aspects of distributed systems are:
    - Concurrency: Many computations may be executing simultaneously in the system, resulting in non-deterministic behaviour.
    - Lack of global clock: It is impossible to have a single clock that is globally synchronized. This makes it hard to measure time intervals and ordering of events.
    - Independent failures: Since components are independent, each can fail independently, thus increasing the chances of system failure.
    - Resource sharing: Resources may be shared by many components, introducing the possibility of conflicting access.
    - Openness: Components may join and leave the system, thus changing the system configuration dynamically.
    - Scalability: The system can be expanded by adding more components, to handle larger workloads or larger amounts of data.
- Some reasons for building distributed systems are:
    - Increased performance and resource sharing
    - Improved reliability and availability
    - Geographic distribution of components
    - System extensibility and incremental growth

[Additional details, diagrams, examples, etc. can be added here if required.]