 Here is the content in markdown format without emojis and external links:

### Token based and non token based algorithms for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

1. Token based algorithms:
- Circulation of a token between the nodes.
- Only the node having the token can enter into the critical section.
- Once the CS execution is completed, the token needs to be passed to the next node.
- Example: Ring based token circulation algorithm.

2. Non token based algorithms:
- No circulation of explicit tokens.
- The right to enter into CS is based on some priority or logical rules.
- Example: Ricart-Agrawala algorithm based on the concept of timestamps. Each node maintains a timestamp which is incremented when a node sends a request message. The node with the smallest timestamp gets the permission to enter into CS.

In general, the mutual exclusion in distributed systems requires the coordination between multiple nodes to regulate the access to shared resources. The token based and non token based algorithms provide solutions to handle the concurrency issues while accessing the shared resources.

The above content summarizes the key points about the token based and non token based distributed mutual exclusion algorithms in a formal tone with points and without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the answer.