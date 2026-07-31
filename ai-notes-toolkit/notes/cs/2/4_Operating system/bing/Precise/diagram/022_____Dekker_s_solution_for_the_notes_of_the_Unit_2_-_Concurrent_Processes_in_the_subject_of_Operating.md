### Dekker’s solution for the notes of the Unit 2 - Concurrent Processes in the subject of Operating system

- Dekker was a Dutch mathematician who introduced a software-based solution for the mutual exclusion problem. This algorithm is commonly called Dekker’s algorithm.
- The Deckker’s algorithm was developed for an algorithm for mutual exclusion between two processes.
- Dekker’s Solution, mentioned here, ensures mutual exclusion between two processes only, it could be extended to more than two processes with the proper use of arrays and variables.
- Algorithm: It requires both an array of Boolean values and an integer variable: var flag: array [0..1] of boolean; turn: 0..1;.
- Dekker's algorithm is the first known correct solution to the mutual exclusion problem in concurrent programming where processes only communicate via shared memory.
- The solution is attributed to Dutch mathematician Th. J. Dekker by Edsger W. Dijkstra in an unpublished paper on sequential process descriptions [1] and his manuscript on ....
- To obtain such a mutual exclusion, bounded waiting, and progress there have been several algorithms implemented, one of which is Dekker’s Algorithm.
- To understand the algorithm let’s understand the solution to the critical section problem first.