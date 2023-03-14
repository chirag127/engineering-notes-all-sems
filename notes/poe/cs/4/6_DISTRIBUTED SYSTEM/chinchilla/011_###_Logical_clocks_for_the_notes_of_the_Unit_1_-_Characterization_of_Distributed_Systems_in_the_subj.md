### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

In a distributed system, it is essential to maintain a consistent view of the sequence of events occurring across different processes. Logical clocks are a mechanism that enables us to order events in a distributed system, even when there is no global clock available.

#### Definition
A logical clock is a mechanism that assigns a logical timestamp to each event in a distributed system. Logical clocks are used to order events in a distributed system and to establish a partial ordering of events that are not causally related.

#### Types of Logical Clocks
There are two types of logical clocks:

1. Lamport Clocks: Lamport clocks are the most basic form of logical clocks. They are based on the concept of a global counter that is incremented by one for each event that occurs in the distributed system.

2. Vector Clocks: Vector clocks are an extension of Lamport clocks. In vector clocks, each process maintains a vector of logical timestamps, where the i-th entry in the vector represents the number of events that have occurred at process i.

#### Advantages of Logical Clocks
- Logical clocks help in establishing a partial ordering of events in a distributed system.
- They enable us to detect causality violations, i.e., events that violate the causal ordering of events.
- Logical clocks help in building efficient distributed algorithms, such as distributed snapshots and distributed garbage collection.

#### Disadvantages of Logical Clocks
- Logical clocks cannot establish a total ordering of events, i.e., they cannot determine the exact order in which events occurred.
- Logical clocks require synchronization among processes to ensure that the logical timestamps are consistent across all processes.

#### Mnemonics and Learning Tricks
- To remember the difference between Lamport and Vector clocks, think of Lamport clocks as a single global counter that is incremented for each event, whereas Vector clocks are a vector of counters maintained by each process.
- To remember the advantages of logical clocks, think of the acronym "PIDE" - Partial ordering, Causality violation detection, Distributed algorithms, and Efficient.
- To remember the disadvantages of logical clocks, think of the acronym "TNC" - Total ordering not possible, Need for synchronization, and Consistency.