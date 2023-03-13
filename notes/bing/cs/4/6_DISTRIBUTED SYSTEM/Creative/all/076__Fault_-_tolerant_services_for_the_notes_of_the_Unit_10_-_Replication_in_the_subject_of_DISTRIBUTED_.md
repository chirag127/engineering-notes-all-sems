### Fault - tolerant services for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM

- Fault tolerance is the ability of a system to continue functioning correctly even in the presence of failures.
- Replication is a technique for achieving fault tolerance by creating and maintaining multiple copies of the same data or service on different nodes in a distributed system.
- Replication can improve availability, performance, and reliability of a distributed system, but also introduces challenges such as consistency, concurrency, and coordination among replicas.
- There are two main types of replication: passive replication and active replication.
- In passive replication, there is one primary replica that receives and executes all requests from clients, and one or more backup replicas that receive updates from the primary and are ready to take over in case of a failure.
- In active replication, there are multiple replicas that receive and execute the same requests from clients in parallel, and use a consensus protocol to agree on the order and outcome of the requests.
- Passive replication has the advantages of lower overhead, simpler implementation, and higher throughput, but the disadvantages of single point of failure, longer recovery time, and lower availability.
- Active replication has the advantages of higher availability, faster recovery, and no single point of failure, but the disadvantages of higher overhead, more complex implementation, and lower throughput.
- A mnemonic to remember the difference between passive and active replication is: **P**assive replication has one **P**rimary replica, while **A**ctive replication has **A**ll replicas **A**ctive.
- A fault-tolerant service can use either passive or active replication, depending on the requirements and trade-offs of the system. Some examples of fault-tolerant services that use replication are:

  - Distributed file systems, such as HDFS, GFS, and Ceph, that use replication to store data across multiple nodes and ensure data availability and durability in case of node failures.
  - Distributed databases, such as Cassandra, MongoDB, and DynamoDB, that use replication to provide high availability, scalability, and consistency of data across multiple nodes and regions.
  - Distributed consensus protocols, such as Paxos, Raft, and Zab, that use replication to implement a fault-tolerant distributed state machine that can coordinate and agree on the state of the system among multiple nodes.
  - Distributed web services, such as Google, Facebook, and Amazon, that use replication to handle large volumes of requests from users and provide fast and reliable responses.