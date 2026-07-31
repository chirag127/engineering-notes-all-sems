### Unit 2 - Distributed Mutual Exclusion: Token-based and Non-token-based Algorithms

Distributed mutual exclusion algorithms can be classified into two categories: token-based and non-token-based.

#### Token-based Algorithms
- In token-based algorithms, a unique token is shared among all the nodes in the system.
- Only the node that holds the token can enter the critical section.
- The token is passed from one node to another in a predefined manner, such as in a logical ring or tree structure.
- Examples of token-based algorithms include the Ricart-Agrawala algorithm and the Suzuki-Kasami algorithm.

#### Non-token-based Algorithms
- In non-token-based algorithms, nodes communicate with each other to coordinate access to the critical section.
- These algorithms do not rely on a unique token, but instead use message passing and timestamps to determine which node can enter the critical section.
- Examples of non-token-based algorithms include the Lamport's algorithm and the Maekawa's algorithm.

Both token-based and non-token-based algorithms have their advantages and disadvantages, and the choice of algorithm depends on the specific requirements of the distributed system.