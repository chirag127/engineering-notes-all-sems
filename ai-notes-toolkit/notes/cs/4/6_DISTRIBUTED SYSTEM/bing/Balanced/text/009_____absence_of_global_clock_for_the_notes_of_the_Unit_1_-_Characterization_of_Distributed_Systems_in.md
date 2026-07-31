### Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system and provides a common notion of time.
- A global clock is useful for ordering events, synchronizing processes, and obtaining consistent states of the system.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays.
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that processes in a distributed system cannot rely on the communication channel to exchange accurate and timely information about the global clock value.
- As a result, processes in a distributed system may have different and inconsistent notions of time, and it may not be possible to determine the order of events or the state of the system in a meaningful way.