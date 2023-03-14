 Here is the content in markdown format:

### Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system consists of multiple autonomous computers that are connected through a network and cooperate to accomplish a task.
- The computers are geographically separated and often operate asynchronously from each other.
- Some key characteristics of distributed systems are:

1. Consistency: The system must behave as if there is a single copy of the data, even though it is replicated on multiple machines. Achieving and maintaining consistency is challenging.
2. Scalability: The system should continue to work efficiently even as more computers/processes are added. This is hard to achieve due to issues like increased communication overhead, load balancing, etc.
3. Fault Tolerance: The system should be resilient to failures of individual computers and continue operating without loss of functionality. Implementing fault tolerance requires techniques like replication, checkpointing, etc.
4. Transparency: The system should hide the complexity of distribution from the user and make the system appear as a single integrated computing facility. Achieving transparency adds to the challenge.

- Some advantages of distributed systems are scalability, cost efficiency, performance, fault tolerance.
- Some disadvantages are complexity, non-determinism, difficulty of programming and debugging, security issues.
- Examples of distributed systems are web servers, cloud computing systems, peer-to-peer networks.
- Applications include improving response time, increasing throughput, providing continuous availability.

- Mnemonics: CADS stands for Consistency, Scalability, Availability, Durability and Security which are key characteristics of distributed systems.
- Learning trick: Think of a large e-commerce website that stays functional 24/7. This is an example of a distributed system that is scalable, fault tolerant and aims to provide good performance. Understanding how such a system works under the hood can help understand the core concepts and challenges of distributed systems.