### Classification of distributed mutual exclusion for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

Distributed mutual exclusion (DME) is a fundamental problem in distributed computing systems. It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner. In other words, only one process is allowed to execute the critical section (CS) at any given time in a distributed system .

In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing DME. The decision as to which process is allowed access to the CS next is arrived at by message passing, in which each process learns about the state of all other processes in some consistent way. The design of DME algorithms is complex because these algorithms have to deal with unpredictable message delays and incomplete knowledge of the system state.

There are three basic approaches for implementing DME :

- Token-based approach: A unique token is shared among all the sites. A site is allowed to enter its CS if it possesses the token and it continues to hold the token until the execution of the CS is over. Mutual exclusion is ensured because the token is unique. Example: Suzuki-Kasami’s Broadcast Algorithm.
- Non-token-based approach: A site communicates with other sites in order to determine which site should execute CS next. This requires exchange of two or more successive rounds of messages among sites. This approach uses sequence numbers to order requests for the CS. Each request for CS contains a sequence number. This sequence number is used to distinguish old and current requests. Example: Ricart-Agrawala’s Algorithm.
- Quorum-based approach: A site is allowed to enter its CS if it obtains permission from a subset of sites in the system, called a quorum. A quorum is a set of sites such that any two quorums have at least one site in common. Mutual exclusion is ensured because any two sites executing CS must have obtained permission from a common site. Example: Maekawa’s Algorithm.

A possible mnemonic to remember the three approaches is: **T**oken, **N**on-token, **Q**uorum, or **TNQ**.

Some of the requirements of DME algorithms are:

- No deadlock: Two or more sites should not endlessly wait for any message that will never arrive.
- No starvation: Every site who wants to execute CS should get an opportunity to execute it in finite time. Any site should not wait indefinitely to execute CS while other sites are repeatedly executing CS.
- Fairness: Each site should get a fair chance to execute CS. Any request to execute CS must be executed in the order they are made, i.e., CS execution requests should be executed in the order of their arrival in the system.
- Fault tolerance: In case of failure, the algorithm should be able to recognize it by itself in order to continue functioning without any disruption.