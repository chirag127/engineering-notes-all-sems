# Dekker’s solution for the notes of the Unit 2 - Concurrent Processes in the subject of Operating system

Dekker’s algorithm is a software-based solution for the mutual exclusion problem, introduced by a Dutch mathematician named Dekker. It is the first known correct solution to the mutual exclusion problem in concurrent programming where processes only communicate via shared memory.

Dekker’s solution ensures mutual exclusion between two processes only, but it could be extended to more than two processes with the proper use of arrays and variables. The algorithm requires both an array of Boolean values and an integer variable.

The algorithm is designed to obtain mutual exclusion, bounded waiting, and progress. To understand the algorithm, it is important to first understand the solution to the critical section problem.

The critical section problem has several requirements, including mutual exclusion, progress, and fault tolerance. Mutual exclusion means that no two processes will simultaneously be inside the same critical section. Progress means that a process wishing to enter its critical section will eventually do so in finite time. Fault tolerance means that processes failing outside their critical section should not interfere with others accessing the critical section.