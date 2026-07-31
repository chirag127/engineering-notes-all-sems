### Unit 2 - Distributed Mutual Exclusion: Token-based and Non-token-based Algorithms

Distributed mutual exclusion algorithms can be classified into two categories: token-based and non-token-based.

#### Token-based Algorithms:
- In token-based algorithms, a unique token is shared among all the nodes in the system.
- The node that holds the token has the right to enter the critical section.
- When a node wants to enter the critical section, it must first request the token from the node that currently holds it.
- After the node has finished executing the critical section, it passes the token to the next node that has requested it.
- Examples of token-based algorithms include the Ricart-Agrawala algorithm and the Suzuki-Kasami algorithm.

#### Non-token-based Algorithms:
- In non-token-based algorithms, nodes do not share a unique token.
- Instead, nodes use other methods to coordinate access to the critical section, such as message passing or timestamps.
- When a node wants to enter the critical section, it sends a request message to all other nodes in the system.
- Each node responds with a permission message, indicating whether or not the requesting node can enter the critical section.
- The requesting node can enter the critical section only after it has received permission from all other nodes.
- Examples of non-token-based algorithms include the Lamport's algorithm and the Maekawa's algorithm.