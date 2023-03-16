### Absence of Global Clock for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of DISTRIBUTED SYSTEM

- In a distributed system, there is no global clock that all processes can access.
- This means that it is not possible for all processes to agree on a common time.
- The absence of a global clock can make it difficult to synchronize processes and coordinate their actions.
- To overcome this issue, distributed systems often use logical clocks or vector clocks to establish a partial ordering of events.
- These clocks allow processes to agree on the relative ordering of events, even if they do not agree on the exact time at which the events occurred.
- Another approach to dealing with the absence of a global clock is to use time synchronization protocols, such as the Network Time Protocol (NTP), to synchronize the clocks of all processes in the system.
- These protocols allow processes to agree on a common time, even if their clocks are not perfectly synchronized.
- The absence of a global clock is one of the fundamental challenges in the design and implementation of distributed systems. It requires careful consideration and the use of appropriate synchronization techniques to ensure that processes can coordinate their actions effectively.