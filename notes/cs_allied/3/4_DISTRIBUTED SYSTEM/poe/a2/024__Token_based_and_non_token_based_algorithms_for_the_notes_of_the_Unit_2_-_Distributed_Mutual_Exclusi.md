 Here is the formal content written in Markdown format without any emojis or external links for the topic -

Token based and non token based algorithms for Distributed Mutual Exclusion

### Token based algorithms

- Token ring algorithm: A token is circulated among the nodes. Only the node possessing the token can access the critical section. Once done, it passes the token to the next node.
- Centralized token algorithm: A centralized server maintains a token. Nodes request the server for token. The server grants the token to one node at a time.

Advantages:
- Absence of race conditions
- Resource utilization is good as only one node at a time accesses the critical section.

Disadvantages:
- Message overhead due to token circulation/passing
- If the server fails, the system becomes unavailable

### Non-token based algorithms

- Ricart-Agrawala algorithm: Each node maintains a request table recording requests from other nodes and the order of requests. The node with the smallest timestamp is granted access.
- Maekawa's algorithm: A logical timestamp ordering is used along with priority to determine which node gains access.

Advantages:
- No explicit token messaging overhead

Disadvantages:
- Prone to race conditions. Additional synchronization required.
- Complexity of maintaining and determining ordering.