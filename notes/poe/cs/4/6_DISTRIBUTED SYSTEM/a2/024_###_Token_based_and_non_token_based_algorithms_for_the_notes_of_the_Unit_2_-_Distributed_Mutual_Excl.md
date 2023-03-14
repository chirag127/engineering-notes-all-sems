 Here is the content in markdown format:

### Token based and non token based algorithms for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

Token based algorithms:
- Token is passed between processes. Only process holding the token can enter critical section.
- Examples: Ring based algorithm, Token ring algorithm.
- Advantage: Simplicity, starvation free.
- Disadvantage: Message overhead increases with number of processes.

Non token based algorithms:
- Do not use explicit tokens. Decide entry using information about other processes.
- Examples: Ricart-Agrawala algorithm, Maekawa's algorithm.
- Advantage: Less message overhead.
- Disadvantage: Complexity increases with number of processes.

Mnemonics:
- Token goes round and round,
Only holder enters critical ground.
- Without a token in sight,
Information helps decide right.

Learning tricks:
- Visualize a token being passed between processes to understand token based algorithms.
- For non token based, focus on how processes take decisions using messages and information about each other.
- Implement algorithms on paper with small number of processes to get better intuition.

[Detailed diagrams and examples can be added here for more understanding.]

Applications:
- Distributed databases
- Shared resources in distributed systems
- Parallel programming

Advantages and disadvantages can help compare the algorithms and choose suitable one based on requirements.