### Token based and non token based algorithms for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM
Token based algorithms:
1. Token Ring Algorithm: Each process has a unique token, and a process can only enter critical section if it holds the token.
2. Ricart-Agrawala Algorithm: Processes send requests to each other to enter critical section, and grant permission based on the timestamps of the requests.

Non token based algorithms:
1. Lamport's Bakery Algorithm: Processes take a number, and the process with the smallest number enters critical section.
2. Centralized Algorithm: A central authority grants permission to enter critical section.
