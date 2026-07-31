# Classification of distributed mutual exclusion

Distributed mutual exclusion is a problem of ensuring that only one process can access a shared resource or data at a time in a distributed system. It is a fundamental requirement for achieving consistency, coordination and synchronization among the processes in a distributed system.

There are three basic approaches for implementing distributed mutual exclusion:

- Token-based approach
- Non-token-based approach
- Quorum-based approach

## Token-based approach

In this approach, a unique token is shared among the sites or processes in the system. A site or process is allowed to enter its critical section (CS) if it possesses the token. Mutual exclusion is ensured because the token is unique and only one site or process can have it at a time. The token is passed from one site or process to another according to some predefined order or algorithm. Some examples of token-based algorithms are:

- Suzuki-Kasami algorithm
- Raymond's algorithm
- Singhal's heuristic algorithm

## Non-token-based approach

In this approach, there is no token in the system. Instead, a site or process requests permission from other sites or processes to enter its CS. The other sites or processes reply with either a grant or a deny message. A site or process can enter its CS only if it receives grant messages from all or a majority of the other sites or processes. Mutual exclusion is ensured by the agreement or voting among the sites or processes. Some examples of non-token-based algorithms are:

- Ricart-Agrawala algorithm
- Lamport's algorithm
- Maekawa's algorithm

## Quorum-based approach

In this approach, a site or process requests permission from a subset of sites or processes, called a quorum, to enter its CS. The quorum is chosen such that any two quorums have at least one site or process in common. A site or process can enter its CS only if it receives grant messages from all the sites or processes in its quorum. Mutual exclusion is ensured by the intersection property of the quorums. Some examples of quorum-based algorithms are:

- Sankararaman's algorithm
- Naimi-Trehel's algorithm
- Agrawal-El Abbadi's algorithm