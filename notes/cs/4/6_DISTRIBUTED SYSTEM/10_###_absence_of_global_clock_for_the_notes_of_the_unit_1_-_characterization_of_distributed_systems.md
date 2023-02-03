### absence of global clock for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

In distributed systems, the absence of a global clock refers to the lack of a single, accurate time source that is shared by all nodes in the system. This can make it difficult to coordinate and synchronize the actions of different nodes in the system.

Without a global clock, each node in a distributed system may have its own local clock, which can drift over time and cause inconsistencies in the system. This can lead to problems such as incorrect ordering of events, incorrect timing of events, and incorrect detection of failures.

To address the issues caused by the absence of a global clock, various synchronization algorithms have been developed. These algorithms aim to provide a way for nodes in the system to agree on a common time, or at least to agree on the ordering of events.

Examples of synchronization algorithms include clock synchronization protocols, such as the Network Time Protocol (NTP), and logical clocks, such as Lamport timestamps. These algorithms can help to ensure that the nodes in a distributed system have a consistent view of time and can coordinate their actions effectively.

In summary, the absence of a global clock in distributed systems can lead to coordination and synchronization problems, but these issues can be addressed through the use of synchronization algorithms.
