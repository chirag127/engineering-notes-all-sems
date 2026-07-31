# Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system.
- A global clock can provide a common notion of time and a consistent ordering of events across different processes.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays.
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that the communication channel between processes is unreliable and can introduce variable and unknown delays in message transmission.
- As a result, processes in a distributed system may have different and inaccurate views of the global clock value, and may disagree on the order of events that happened on different processes.
- The absence of a global clock poses challenges for designing and implementing distributed algorithms that require synchronization, coordination, and consistency among processes.