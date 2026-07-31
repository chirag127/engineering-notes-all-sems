### Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system and provides a common notion of time.
- A global clock is useful for determining the order of events, synchronizing processes, and obtaining a consistent state of the system.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays.
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that the communication channel between processes is unreliable and may introduce variable and unknown delays in message transmission.
- As a result, processes in a distributed system may have different and inaccurate views of the global clock value, and the notion of common time does not exist.
- Therefore, distributed systems have to rely on other mechanisms, such as logical clocks, vector clocks, or Lamport timestamps, to order events and capture causality.