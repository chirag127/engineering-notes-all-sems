 Here is the content in markdown format:

### Token based and non token based algorithms for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

Token based algorithms:
- Token is passed between nodes to grant access to critical section.
- Only node with token can enter critical section.
- Eg: Ring based algorithm

Non token based algorithms:
- No physical token is passed.
- Nodes coordinate with each other to grant access to critical section.
- Eg: Ricart-Agrawala algorithm, Maekawa's algorithm.

**Ring based algorithm (Token based):**
- Nodes are organized in a logical ring.
- Token is passed between nodes in a fixed direction.
- Node with token can enter critical section.
- If token holding node does not need CS, it passes token to next node.
- Advantage: Simple and efficient if most nodes don't need CS.
- Disadvantage: Uneven token rotation can lead to starvation.

**Ricart-Agrawala algorithm (Non token based):**
- Each node broadcasts request message to enter critical section to all other nodes.
- On receiving requests, each node assigns timestamps and sends acknowledgement with timestamp information.
- Node with smallest timestamp among all nodes enters critical section.
- Advantage: Solves problem of uneven token distribution in ring based approach.
- Disadvantage: More number of messages exchanged leading to higher overhead.

**Maekawa's algorithm (Non token based):**
- Combines features of Ricart-Agrawala algorithm and ring based approach.
- Nodes are organized in a logical ring. Requests are made in a fixed direction.
- On receiving request, node assigns timestamp and sends acknowledgement with timestamp to only previous node in ring.
- Node with smallest timestamp enters critical section.
- Advantage: Overhead is less than Ricart-Agrawala algorithm as acknowledgments are sent only to previous node.
- Disadvantage: Possibility of uneven request distribution leading to starvation.