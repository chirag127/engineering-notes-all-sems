### global state for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM
Global state in distributed systems refers to the shared information that is held by all nodes in a network. This information can include the current status of each node, the state of any ongoing processes, and the state of shared resources such as files and databases. Maintaining a consistent global state is crucial for ensuring the correct functioning of a distributed system, as it allows nodes to coordinate their actions and make decisions based on a shared understanding of the system's current state.

There are several approaches to maintaining global state in distributed systems, including:

1. Centralized state management: A single node is designated as the "state manager" and is responsible for maintaining the global state.

2. Decentralized state management: Each node maintains its own copy of the global state and updates are propagated between nodes through a consensus protocol.

3. Hybrid approach: A combination of centralized and decentralized state management, where some information is managed centrally and other information is managed locally by each node.

Regardless of the approach used, maintaining a consistent global state in a distributed system is a complex task that requires careful design and implementation to ensure that the system remains reliable and scalable.
