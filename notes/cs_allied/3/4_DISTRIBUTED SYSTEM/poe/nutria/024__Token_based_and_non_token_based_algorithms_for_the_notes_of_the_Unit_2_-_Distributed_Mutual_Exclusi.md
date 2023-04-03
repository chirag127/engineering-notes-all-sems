
### Token Based Algorithms
- Ricart and Agrawala algorithm: This algorithm is based on a token which is passed between processes. The token is initially held by a single process and is passed to each process in turn. This algorithm works on the principle that a process can enter its critical section only if it has the token. 
- Maekawa algorithm: This algorithm is based on the concept of quorum. A quorum is a set of processes which must agree before a process can enter its critical section. The algorithm requires that a process must have permission from a quorum of processes before it can enter its critical section.

### Non Token Based Algorithms
- Centralized algorithm: This algorithm is based on a centralized server which is responsible for granting access to the critical section. The server receives requests from processes and grants access to the critical section to only one process at a time.
- Distributed algorithm: This algorithm is based on the concept of distributed mutual exclusion. In this algorithm, each process has a local clock which is used to determine the order in which the processes can enter the critical section. The process with the lowest clock value is granted access to the critical section.