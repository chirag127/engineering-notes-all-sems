Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of absence of global clock for the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Absence of global clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system.
- A global clock would allow processes to synchronize their actions, measure the elapsed time between events, and determine the order of events across the system.
- However, a global clock is hard to realize in distributed systems due to the following reasons:
  - The physical clocks of different processes may have different rates of drift, accuracy, and precision, making them unsuitable for global synchronization.
  - The communication channels between processes may have unpredictable and variable transmission delays, making it impossible to exchange accurate clock values or timestamps.
  - The distributed system may span multiple time zones, making it difficult to agree on a common time reference.
- Therefore, distributed systems are inherently asynchronous, meaning that there is no common notion of time or global state among the processes.
- This has two important implications for distributed systems:
  - It is not always possible to determine the order of events on different processes, since there is no global time to compare their timestamps. This affects the consistency and causality of the system.
  - It is not possible for an individual process to obtain an up-to-date state of the entire system, since there is no global clock to capture a consistent snapshot of the system. This affects the observability and debugging of the system.