### System Model and Group Communication

#### Unit 10 - Replication in Distributed Systems

1. A **system model** is a representation of the components and interactions within a distributed system. It is used to understand and reason about the behavior of the system.

2. **Group communication** is a mechanism for exchanging messages between multiple processes in a distributed system. It is used to coordinate the actions of the processes and to ensure that they operate correctly.

3. **Replication** is the process of creating and maintaining multiple copies of data or services in a distributed system. It is used to improve the availability, reliability, and performance of the system.

4. In a **replicated system**, each replica maintains a copy of the data or service. The replicas communicate with each other to ensure that they remain consistent and up-to-date.

5. **Consistency** is a key concern in replicated systems. It refers to the requirement that all replicas should have the same view of the data or service at all times.

6. There are several approaches to achieving consistency in replicated systems, including **primary-backup replication**, **active replication**, and **quorum-based replication**.

7. **Primary-backup replication** involves designating one replica as the primary and the others as backups. The primary is responsible for processing all updates to the data or service, and the backups receive updates from the primary.

8. **Active replication** involves all replicas processing updates simultaneously. Each update is sent to all replicas, and they all execute the update in the same order.

9. **Quorum-based replication** involves requiring a minimum number of replicas to agree on an update before it is considered committed. This approach can provide a balance between availability and consistency.

10. Group communication plays a crucial role in ensuring the consistency of replicated systems. It is used to coordinate the actions of the replicas and to ensure that they all have the same view of the data or service.