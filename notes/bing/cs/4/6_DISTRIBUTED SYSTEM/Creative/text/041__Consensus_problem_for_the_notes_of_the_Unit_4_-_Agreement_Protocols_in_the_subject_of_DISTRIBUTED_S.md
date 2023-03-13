### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is a fundamental problem in distributed computing, where a set of processes (or agents) have to agree on a common value based on their initial inputs and communication with each other.
- The consensus problem is also known as the agreement problem, the Byzantine generals problem, or the interactive consistency problem.
- The consensus problem is important for many applications in distributed systems, such as fault-tolerance, distributed transactions, leader election, distributed commit, state machine replication, and blockchain.
- The consensus problem can be formally defined as follows:

  - Each process has an initial input value, which is known only to itself.
  - Each process can communicate with other processes by sending and receiving messages.
  - Each process has to decide on an output value, which is the same for all processes (agreement).
  - The output value has to be one of the input values (validity).
  - The output value has to be decided by all processes within a finite number of steps (termination).

- The consensus problem can be classified into different variants based on the assumptions and properties of the system, such as:

  - Synchronous or asynchronous: whether the processes and the communication channels have bounded delays or not.
  - Crash or Byzantine failures: whether the processes can only stop working or can also behave arbitrarily (e.g., lie, omit messages, etc.).
  - Deterministic or randomized: whether the processes can use randomization or not in their algorithms.
  - Binary or multivalued: whether the input and output values are restricted to two values (e.g., 0 or 1) or can be any value from a domain.
  - Uniform or non-uniform: whether the agreement property holds for all processes or only for a subset of them.

- The consensus problem is known to be impossible to solve in some settings, such as in asynchronous systems with one or more Byzantine failures, or in synchronous systems with more than one-third of Byzantine failures.
- The consensus problem can be solved in some settings, such as in synchronous systems with less than one-third of Byzantine failures, or in asynchronous systems with crash failures and additional assumptions (e.g., failure detectors, common coins, etc.).
- The consensus problem can be solved using different algorithms, such as:

  - Paxos: a family of algorithms for solving consensus in asynchronous systems with crash failures and a majority of correct processes.
  - Raft: a simplified version of Paxos that is easier to understand and implement, and also provides leader election and log replication.
  - Byzantine fault tolerance (BFT): a family of algorithms for solving consensus in synchronous or partially synchronous systems with Byzantine failures and less than one-third of faulty processes.
  - Practical Byzantine fault tolerance (PBFT): a specific BFT algorithm that is optimized for performance and scalability, and is widely used in blockchain systems.
  - Nakamoto consensus: a probabilistic consensus algorithm that is based on proof-of-work and longest chain rule, and is used in Bitcoin and other cryptocurrencies.