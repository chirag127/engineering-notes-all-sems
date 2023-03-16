### Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system and provides a common notion of time.
- A global clock is useful for determining the order of events and the state of the system across different processes.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays.
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that processes in a distributed system cannot synchronize their local clocks with each other or with an external time source reliably and accurately.
- As a result, the absence of a global clock implies that:
  - Different processes may have different notions of time and their local clocks may drift apart over time.
  - It is not always possible to determine the order of events on different processes based on their timestamps or message exchanges.
  - It is not possible for an individual process to obtain an up-to-date and consistent state of the entire system by querying other processes.
  - It is difficult to obtain a meaningful global state of the system that reflects the states of different processes at the same point in time.