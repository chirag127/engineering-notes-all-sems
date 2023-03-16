### Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system and provides a common notion of time.
- A global clock is useful for determining the order of events, synchronizing processes, and obtaining a consistent state of the system.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays.
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that the communication channel between processes is unreliable and the transmission time of messages is variable and unknown.
- Therefore, processes in a distributed system may have different and inaccurate views of the global clock value, and the global clock may not reflect the actual order of events or the actual state of the system.
- Due to the absence of a global clock, distributed systems have to rely on other mechanisms to achieve coordination, consistency, and correctness. Some of these mechanisms are logical clocks, vector clocks, causal ordering, global snapshots, and distributed algorithms.