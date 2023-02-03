## Unit 3 - Distributed Deadlock Detection
Unit 3 Distributed Deadlock Detection deals with methods for detecting deadlocks in a distributed system. Deadlocks occur when multiple processes are blocked waiting for resources held by other processes. This can lead to a situation where no progress can be made. Distributed deadlock detection algorithms are used to identify such situations and resolve them. The most common methods include:
1. Chandy-Misra-Haas algorithm
2. Maekawa's algorithm
3. Ricart-Agrawala algorithm

Each algorithm uses different techniques to detect deadlocks, such as message passing, vector clocks, and distributed resource allocation tables. The choice of algorithm depends on factors such as network size, resource allocation patterns, and system requirements. The goal of these algorithms is to minimize the overhead of deadlock detection and resolve deadlocks in an efficient manner.
