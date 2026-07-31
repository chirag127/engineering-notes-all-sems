 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Classification of distributed mutual exclusion

1. Token-based mutual exclusion: In this approach, a token is passed among the processes. Only the process holding the token can enter its critical section. Once it completes its work, it passes the token to the next process. This ensures mutual exclusion.
2. Centralized mutual exclusion: There is a central server that maintains the status of processes. When a process wants to enter its critical section, it sends a request to the central server. The server grants permission to only one process at a time, ensuring mutual exclusion.
3. Distributed mutual exclusion: This is a set of protocols to achieve mutual exclusion in a distributed system without any central coordinator. They are based on ordering messages, timestamps, or graph-based algorithms. Few popular protocols are Ricart-Agrawala algorithm and Raymond's algorithm.
4. Quorum-based mutual exclusion: The system is divided into subsets of processes called quorums. Only processes that belong to the same quorum can access their critical sections simultaneously. This ensures mutual exclusion among processes of different quorums.

The content summarizes four types of approaches to achieve distributed mutual exclusion - token-based, centralized, distributed, and quorum-based. The points briefly describe each approach to help understand the concepts. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.