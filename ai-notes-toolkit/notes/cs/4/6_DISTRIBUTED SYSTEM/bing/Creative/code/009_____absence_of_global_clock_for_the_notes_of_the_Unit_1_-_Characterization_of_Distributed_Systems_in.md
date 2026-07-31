### Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system and provides a common notion of time.
- A global clock is useful for determining the order of events and the state of the system across different processes.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays .
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that the communication channel between processes is unreliable and the transmission time of messages is variable and unknown.
- Therefore, processes in a distributed system may have different and inaccurate views of the global clock value, and the notion of common time does not exist.
- As a result, it is not always possible to determine the order in which two events on different processes were executed, or to obtain an up-to-date and consistent state of the entire system.
- The absence of a global clock poses challenges for designing and implementing distributed algorithms and protocols that require synchronization, coordination, and consistency among processes.