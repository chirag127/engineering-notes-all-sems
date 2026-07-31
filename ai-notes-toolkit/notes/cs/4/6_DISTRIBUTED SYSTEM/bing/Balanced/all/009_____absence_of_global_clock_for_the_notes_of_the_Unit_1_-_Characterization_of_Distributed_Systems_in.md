# Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system and provides a common notion of time.
- A global clock is useful for determining the order of events and the state of the system across different processes.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays.
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that the communication channel between processes is not reliable and can introduce variable and unknown delays in message transmission.
- As a result, different processes may have different and inaccurate views of the global clock value, and the notion of common time does not exist in a distributed system.
- This also makes it difficult to obtain a meaningful and consistent state of the system, as the states of different processes may not be synchronized with each other.
- Therefore, the absence of a global clock poses a challenge for designing and implementing distributed systems that require coordination, synchronization, and consistency among processes.