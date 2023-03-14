### Global state for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A global state of a distributed system is the **union of the states of the individual processes and the communication channels** .
- A process can only observe its own state and the messages it sends and receives, but not the state of other processes or channels.
- To determine a global state, a process needs to **coordinate** with other processes and **collect** their local states and the messages in transit.
- A global state is useful for solving many problems in distributed systems, such as:
  - **Checkpointing**: saving the state of a distributed application for recovery from failures.
  - **Garbage collection**: reclaiming the memory of unused objects that are not referenced by any other objects.
  - **Deadlock detection**: identifying circular dependencies among processes that prevent them from making progress.
  - **Termination detection**: determining whether a distributed computation has finished.
  - **Stable property detection**: verifying whether a property that once becomes true remains true thereafter, such as "the system is deadlocked" or "all tokens in a token ring have disappeared" .
- A global state is **consistent** if it reflects a possible state of the system that could have occurred during the execution .
- A consistent global state can be obtained by taking a **snapshot** of the system along a **consistent cut**, which is a partition of the events into past and future such that no message is received before it is sent  .
- A consistent cut can be represented by a **zigzag line** that cuts through the **space-time diagram** of the system, where each process is a vertical line and each message is a horizontal line .
- A consistent cut can be **transformed** into an equivalent one where all the cut events occur simultaneously, by applying a **rubber band transformation** that stretches or shrinks the time axis of each process .
- A consistent global state can be computed by using **snapshot algorithms**, such as the **Chandy-Lamport algorithm**, which initiates a snapshot by sending **marker messages** along the channels and records the state of each process and channel when they receive the marker for the first time .

#### Mnemonics and learning tricks

- To remember the definition of a global state, think of the acronym **PAC** (Process And Channel): a global state is the union of the states of the **P**rocesses and the **C**hannels.
- To remember the definition of a consistent global state, think of the word **POSSIBLE**: a consistent global state is a **POSSIBLE** state of the system that could have occurred.
- To remember the definition of a consistent cut, think of the word **CUT**: a consistent cut **C**uts the events into past and future such that no message is received before it is **U**n**T**imely sent.
- To remember the rubber band transformation, think of the word **RUB**: a rubber band transformation **R**esizes the time axis of each process to make the cut events occur at the same time (**U**niformly **B**alanced).
- To remember the Chandy-Lamport algorithm, think of the word **MARK**: the Chandy-Lamport algorithm initiates a snapshot by sending **MARK**er messages along the channels and records the state of each process and channel when they receive the marker for the first time.