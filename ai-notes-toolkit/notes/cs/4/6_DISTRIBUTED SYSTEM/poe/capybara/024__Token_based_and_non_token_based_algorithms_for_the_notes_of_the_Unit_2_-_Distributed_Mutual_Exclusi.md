### Token based and non token based algorithms for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

In Unit 2 of Distributed Mutual Exclusion, there are two types of algorithms for achieving mutual exclusion in a distributed system: Token based and Non-token based algorithms. Below are some key points to help you understand these algorithms better:

#### Token Based Algorithms

- In Token based algorithms, a token is passed among the nodes in the system to ensure mutual exclusion.
- A node can enter the critical section only when it receives the token.
- The token is passed from one node to another in a predetermined order, and only the node that has the token can enter the critical section.
- The token is passed from one node to another only when the previous node has released it.
- Examples of Token based algorithms are: Ricart-Agrawala Algorithm, Maekawa's Algorithm, and Suzuki-Kasami Algorithm.

#### Non-Token Based Algorithms

- In Non-Token based algorithms, nodes do not need to pass a token to achieve mutual exclusion.
- Instead, nodes communicate with each other to decide which node can enter the critical section.
- Non-Token based algorithms are also known as Quorum-based algorithms.
- Quorum refers to a set of nodes that are required to make a decision.
- A node can enter the critical section only when it belongs to the quorum.
- Examples of Non-Token based algorithms are: Bully Algorithm, and Chandy-Lamport Algorithm.

Understanding the differences between Token based and Non-Token based algorithms is crucial in Distributed Mutual Exclusion. Knowing the strengths and weaknesses of each algorithm can help you choose the best approach for your distributed system.