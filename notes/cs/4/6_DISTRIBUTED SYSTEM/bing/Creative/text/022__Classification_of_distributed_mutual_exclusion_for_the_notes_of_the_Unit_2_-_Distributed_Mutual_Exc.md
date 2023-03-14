### Classification of distributed mutual exclusion

Distributed mutual exclusion is a fundamental problem in distributed computing systems. It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner. In a distributed system, shared variables or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion .

The algorithms designed to ensure mutual exclusion in distributed systems are termed distributed mutual exclusion (DME) algorithms. A number of DME algorithms have been proposed. They have been classified as token-based algorithms or permission-based algorithms depending on the technique used to achieve mutual exclusion.

- Token-based algorithms: A unique token is shared among all the sites. A site is allowed to enter its critical section if it possesses the token and it continues to hold the token until the execution of the critical section is over. Mutual exclusion is ensured because the token is unique. Example: Suzuki-Kasami’s Broadcast Algorithm.
- Permission-based algorithms: A site communicates with other sites in order to determine which site should execute the critical section next. This requires exchange of two or more successive rounds of messages among sites. Example: Ricart-Agrawala Algorithm.
- Quorum-based algorithms: A site obtains permission from a subset of sites (called a quorum) in order to enter the critical section. The quorums are chosen such that any two quorums have at least one site in common. This ensures mutual exclusion. Example: Maekawa’s Algorithm.

Some of the requirements of DME algorithms are:

- No deadlock: Two or more sites should not endlessly wait for any message that will never arrive.
- No starvation: Every site who wants to execute the critical section should get an opportunity to execute it in finite time.
- Fairness: Each site should get a fair chance to execute the critical section. Any request to execute the critical section must be executed in the order they are made.
- Fault tolerance: In case of failure, the algorithm should be able to recognize it and continue functioning without any disruption.