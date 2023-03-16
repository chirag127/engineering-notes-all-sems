# Classification of distributed mutual exclusion

Distributed mutual exclusion is a problem of ensuring that only one process in a distributed system can access a shared resource or data at a time. It is a fundamental requirement for achieving consistency, coordination and synchronization among the processes.

There are three basic approaches for implementing distributed mutual exclusion:

- Token-based approach
- Non-token based approach
- Quorum-based approach

## Token-based approach

In this approach, a unique token is shared among the sites or processes in the system. A site is allowed to enter its critical section (CS) if it possesses the token. Mutual exclusion is ensured because the token is unique and only one site can have it at a time. The token is passed from one site to another according to some predefined order or algorithm. Some examples of token-based algorithms are:

- Suzuki-Kasami algorithm
- Raymond's algorithm
- Singhal's heuristic algorithm

The advantages of token-based approach are:

- It is simple and easy to implement
- It does not require any knowledge of the global state of the system
- It does not generate any unnecessary messages for requesting or granting access to the CS

The disadvantages of token-based approach are:

- It may cause starvation if the token is lost or delayed
- It may cause performance degradation if the token is far away from the requesting site
- It may cause deadlock if the token is held by a faulty or malicious site

## Non-token based approach

In this approach, a site does not need to possess a token to enter its CS. Instead, it sends a request message to all other sites in the system and waits for their replies. A site is allowed to enter its CS if it receives a reply or an acknowledgment from all other sites. Some examples of non-token based algorithms are:

- Lamport's algorithm
- Ricart-Agrawala algorithm
- Maekawa's algorithm

The advantages of non-token based approach are:

- It does not depend on the existence or availability of a token
- It does not cause starvation or deadlock due to token loss or delay
- It can achieve lower response time and higher throughput than token-based approach

The disadvantages of non-token based approach are:

- It requires more messages and communication overhead than token-based approach
- It requires some knowledge of the global state of the system, such as the number and identity of the sites
- It may cause unnecessary blocking or waiting if some sites are slow or faulty

## Quorum-based approach

In this approach, a site does not need to communicate with all other sites in the system to enter its CS. Instead, it communicates with a subset of sites, called a quorum, that has enough voting power to grant access to the CS. A site is allowed to enter its CS if it receives a majority of votes from the quorum. Some examples of quorum-based algorithms are:

- Majority voting algorithm
- Tree-based algorithm
- Grid-based algorithm

The advantages of quorum-based approach are:

- It reduces the number of messages and communication overhead than non-token based approach
- It allows some degree of concurrency and fault tolerance among the sites
- It can adapt to dynamic changes in the system, such as site addition or deletion

The disadvantages of quorum-based approach are:

- It requires a careful design and selection of the quorum to ensure mutual exclusion and deadlock freedom
- It may cause performance degradation if the quorum is too large or too small
- It may cause inconsistency or violation of mutual exclusion if the quorum overlaps with other quorums