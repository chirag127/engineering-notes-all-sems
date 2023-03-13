## Unit 9 - Distributed Transactions

A distributed transaction is a transaction that involves multiple nodes in a distributed system, such as databases, servers, or applications. A distributed transaction must ensure the ACID properties (atomicity, consistency, isolation, and durability) across all the nodes involved.

Some points to remember about distributed transactions are:

- A distributed transaction can be initiated by a client, a coordinator, or a participant node.
- A coordinator node is responsible for managing the execution and commit of a distributed transaction. It communicates with the participant nodes that execute the transaction operations.
- A participant node is a node that executes a part of a distributed transaction and reports its outcome to the coordinator node.
- A distributed transaction can use different protocols to achieve consensus among the nodes, such as two-phase commit (2PC), three-phase commit (3PC), or Paxos.
- A distributed transaction can face various challenges, such as network failures, node failures, concurrency conflicts, or data inconsistencies.
- A distributed transaction can use different techniques to handle these challenges, such as timeouts, logging, locking, replication, or compensation.

Some mnemonics and learning tricks for distributed transactions are:

- To remember the ACID properties, think of a transaction as a **A**cid **C**leaner that **I**solates and **D**estroys dirt.
- To remember the two-phase commit protocol, think of a **2**-way **C**onversation between the coordinator and the participants: **P**repare and **C**ommit.
- To remember the three-phase commit protocol, think of a **3**-way **C**onversation between the coordinator and the participants: **P**repare, **P**recommit, and **C**ommit.
- To remember the Paxos protocol, think of a **P**arliament that elects a leader and votes on proposals.