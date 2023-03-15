 Here is the content in markdown format for the topic - ### Classification of distributed mutual exclusion for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM:

### Classification of distributed mutual exclusion

The distributed mutual exclusion algorithms can be classified into the following categories:

1. Token-based algorithms: In these algorithms, a token is circulated among the sites. Only the site holding the token can enter the critical section. Examples are ring-based algorithms and centralized token algorithms.
- Ring-based algorithms: The sites are organized into a logical ring. The token is passed unidirectionally from one site to the next. A site waits until it receives the token to enter the critical section.
- Centralized token algorithms: There is a centralized server that keeps track of the token and grants it to requesting sites. The token-requesting site contacts the server to request and receive the token.

2. Permission-based algorithms: The sites grant each other permissions to enter the critical section. Examples are distributed locking protocols and distributed leasing protocols.
- Distributed locking protocols: The sites act as mutually exclusive lock managers. A site must acquire locks from all other sites before it can enter the critical section.
- Distributed leasing protocols: Each site allocates time periods called leases to other sites. A site can enter the critical section if it has leases from all other sites.

3. Time-based algorithms: The sites coordinate based on time to enter the critical section. Examples are timed access algorithms and delay-based algorithms.
- Timed access algorithms: Each site is allocated a fixed time slot in which it can enter the critical section. Outside its time slot, a site must wait.
- Delay-based algorithms: Each site must wait for a random delay before entering the critical section. By choosing different delays, concurrent access can be avoided with high probability.

The classification is not strict and there can be algorithms that use multiple techniques. The choice of a particular algorithm depends on factors like message delays, number of sites, and critical section length.