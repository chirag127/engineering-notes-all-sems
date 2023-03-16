# Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system and provides a common notion of time.
- A global clock is useful for determining the order of events and the state of the system across different processes.
- However, a global clock is hard to realize in distributed systems due to two inherent limitations: lack of shared memory and unpredictable message delays.
- Lack of shared memory means that processes in a distributed system do not have access to a common storage that can store and update the global clock value.
- Unpredictable message delays mean that the communication channel between processes is unreliable and the transmission time of messages is variable and unknown.
- Therefore, the absence of a global clock implies that:
  - Different processes may have different local clocks that are not synchronized and may drift apart over time.
  - It is not always possible to determine the exact order of events that occur on different processes, especially if they are concurrent or causally unrelated.
  - It is not possible for an individual process to obtain an up-to-date and consistent state of the entire system, as the state may change during the transmission of messages.
  - It is difficult to obtain a meaningful global state of the system, in which the states of different processes are consistent with each other and reflect a common point in time.