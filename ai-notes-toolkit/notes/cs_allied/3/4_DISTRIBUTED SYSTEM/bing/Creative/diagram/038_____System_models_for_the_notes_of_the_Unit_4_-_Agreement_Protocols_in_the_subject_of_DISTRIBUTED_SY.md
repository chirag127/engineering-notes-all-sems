### System models for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

A system model is a simplified representation of the properties and behavior of a distributed system. It helps to reason about the system and design algorithms that can cope with the challenges of distributed computing, such as failures, concurrency, and latency. System models can be classified into three types:

- Physical models: capture the hardware composition of a system in terms of computers and other devices and their interconnecting network;
- Interaction models: describe how the components of a system communicate and coordinate their actions through message passing;
- Fault models: specify the types and frequency of failures that can occur in a system and how they affect the system's behavior.

Some of the common system models for distributed systems are :

- Client-server model: a system where one or more servers provide services to multiple clients that request them;
- Peer-to-peer model: a system where each component acts as both a client and a server, and can communicate with any other component in the system;
- Publish-subscribe model: a system where components publish messages to topics and subscribe to topics of interest, and a broker or a network of brokers delivers the messages to the subscribers;
- Message queue model: a system where components send and receive messages through queues, which provide reliable and asynchronous communication;
- MapReduce model: a system where a large computation is divided into smaller tasks that are executed in parallel by multiple workers, and the results are combined by a master node;
- Consensus model: a system where a group of components agree on a common value or decision, despite the possibility of failures and delays.

Each system model has its own assumptions and limitations, and may be suitable for different kinds of applications and scenarios. For example, the consensus model is often used for implementing agreement protocols, such as Paxos and Raft, which are essential for achieving consistency and fault tolerance in distributed systems. However, the consensus model also requires some strong assumptions, such as partial synchrony and crash-recovery, which may not hold in some environments. Therefore, it is important to understand the system model and its implications before designing and implementing a distributed system.