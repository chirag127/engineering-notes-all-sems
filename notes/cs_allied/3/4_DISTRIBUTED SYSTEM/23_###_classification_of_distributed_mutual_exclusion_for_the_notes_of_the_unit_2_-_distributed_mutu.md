### Classification of distributed mutual exclusion for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

There are two main approaches to classify distributed mutual exclusion: centralized and decentralized.

Centralized approaches rely on a central coordinator to grant access to a shared resource. Examples include:
- Token ring algorithms: a token is passed from one node to another in a fixed order, and the node holding the token has access to the shared resource.
- Ricart-Agrawala algorithm: nodes send requests to a central coordinator, which grants access to the shared resource based on a priority algorithm.

Decentralized approaches do not rely on a central coordinator and instead use communication between nodes to coordinate access to the shared resource. Examples include:
- Lamport's bakery algorithm: nodes use a shared array to coordinate access to the shared resource.
- Maekawa's algorithm: nodes communicate with each other to coordinate access to the shared resource.

In summary, centralized approaches rely on a central coordinator, while decentralized approaches rely on communication between nodes.
