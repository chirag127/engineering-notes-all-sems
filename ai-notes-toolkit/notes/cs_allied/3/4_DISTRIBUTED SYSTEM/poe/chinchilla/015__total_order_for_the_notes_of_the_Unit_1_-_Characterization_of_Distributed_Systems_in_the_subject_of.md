### Total Order for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of DISTRIBUTED SYSTEM

Distributed systems are complex systems that consist of multiple autonomous components, such as computers, servers, and applications, that communicate and coordinate with each other to achieve a common goal.

In this unit, we will learn about the characterization of distributed systems, which is an important aspect of understanding how they work and how to design them.

Here are some key points to keep in mind while studying the unit:

1. Definition of Distributed Systems
    - A distributed system is a collection of independent computers that appear to the users as a single coherent system.
    - The components of a distributed system interact with each other by exchanging messages over a network.

2. Characteristics of Distributed Systems
    - Concurrency: Multiple processes may be executing simultaneously.
    - Lack of a global clock: Each node in the system has its own clock and there is no global clock.
    - Independent failures: Components of the system may fail independently.
    - Heterogeneity: Different types of hardware, operating systems, and programming languages may be used in a distributed system.

3. Challenges in Designing Distributed Systems
    - Communication: The design of a communication protocol that enables components to exchange messages effectively and efficiently is challenging.
    - Consistency: Ensuring consistency in a distributed system is difficult because of the lack of a global clock and independent failures.
    - Fault tolerance: The system must be able to tolerate component failures and continue to operate correctly.
    - Scalability: A distributed system should be able to handle an increasing number of users and data.

4. Types of Distributed Systems
    - Client-server architecture: A client requests services from a server.
    - Peer-to-peer architecture: All nodes in the system are equal and can act as both clients and servers.
    - Hybrid architecture: A combination of client-server and peer-to-peer architectures.

5. Communication Models
    - Message passing: Communication is achieved by sending and receiving messages between components.
    - Shared memory: Communication is achieved by accessing a shared memory location.
    - Remote procedure call (RPC): Communication is achieved by invoking a procedure on a remote component.

6. Consensus Algorithms
    - Consensus algorithms are used to achieve agreement among distributed components.
    - Examples of consensus algorithms include the Paxos algorithm and the Raft algorithm.

By understanding the above points, you can get a comprehensive understanding of the characterization of distributed systems, which is essential to design and develop distributed systems.