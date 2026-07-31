Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a summary of the topic of absence of global clock for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Absence of global clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system.
- A global clock would allow processes to synchronize their actions, measure the elapsed time between events, and determine the order of events across the system.
- However, a global clock is hard to realize in distributed systems due to the following reasons:
  - The communication channel between processes is unreliable and has unpredictable message delays.
  - The processes do not share common memory and have to exchange information via messages.
  - The processes may have different local clocks that drift apart over time and are not perfectly accurate.
  - The rate of event occurrence is very high and the granularity of time measurement is limited.
- Therefore, the absence of a global clock implies that:
  - The notion of common time does not exist in a distributed system; different processes may have different notions of time.
  - It is not always possible to determine the order in which two events on different processes were executed.
  - It is not possible for an individual process to obtain an up-to-date state of the entire system.
  - It is difficult to obtain a meaningful state of the system, in which states of different processes are consistent with each other.