### Classification of distributed mutual exclusion

- Distributed mutual exclusion is a problem of ensuring that only one process can access a shared resource or data at a time in a distributed system.
- Distributed mutual exclusion algorithms are solutions that use message passing to coordinate the access of processes to the shared resource or data.
- Distributed mutual exclusion algorithms can be classified into three basic approaches: token-based, non-token-based, and quorum-based.

#### Token-based approach

- In this approach, a unique token is shared among the sites or processes in the system.
- A site or process can enter its critical section (CS) only if it possesses the token.
- Mutual exclusion is ensured because the token is unique and only one site or process can have it at a time.
- The token is passed from one site or process to another according to some protocol or rule.
- Examples of token-based algorithms are: Suzuki-Kasami algorithm, Raymond's algorithm, and Maekawa's algorithm.

#### Non-token-based approach

- In this approach, a site or process does not need a token to enter its CS.
- Instead, a site or process requests permission from other sites or processes in the system before entering its CS.
- Mutual exclusion is ensured by the agreement of the other sites or processes on granting or denying the permission.
- The request and permission messages are exchanged according to some protocol or rule.
- Examples of non-token-based algorithms are: Ricart-Agrawala algorithm, Lamport's algorithm, and Singhal's algorithm.

#### Quorum-based approach

- In this approach, a site or process does not need a token or permission from all the other sites or processes in the system to enter its CS.
- Instead, a site or process requests permission from a subset of sites or processes in the system, called a quorum, before entering its CS.
- Mutual exclusion is ensured by the intersection of the quorums, that is, any two quorums have at least one common site or process.
- The request and permission messages are exchanged according to some protocol or rule.
- Examples of quorum-based algorithms are: Majority voting algorithm, Tree-based algorithm, and Grid-based algorithm.