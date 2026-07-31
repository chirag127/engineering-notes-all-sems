### Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system and provides a common notion of time.
- A global clock is useful for determining the order of events, synchronizing processes, and obtaining consistent states of the system.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays.
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that the communication channel between processes is unreliable and the transmission time of messages is variable and unknown.
- Therefore, processes in a distributed system may have different and inaccurate views of the global clock value, and the notion of common time does not exist.
- As a result, it is not always possible to determine the order of events, synchronize processes, and obtain consistent states of the system in a distributed system without a global clock.
- To overcome the absence of a global clock, distributed systems use various techniques such as logical clocks, vector clocks, causal ordering, snapshot algorithms, etc. to achieve some form of partial or approximate global time and state.