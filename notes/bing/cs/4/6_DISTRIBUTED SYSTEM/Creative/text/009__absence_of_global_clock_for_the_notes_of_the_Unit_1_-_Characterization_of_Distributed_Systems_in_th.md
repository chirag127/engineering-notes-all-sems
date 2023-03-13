### Absence of Global Clock

- A global clock is a hypothetical clock that would provide a common and accurate measure of time for all the processes in a distributed system.
- A global clock is desirable for many applications that require coordination, synchronization, or ordering of events among distributed processes.
- However, a global clock is impossible to implement in a distributed system, due to the following reasons:
  - Each process has its own local clock, which may run at a different rate or granularity than other clocks, leading to clock drift and asynchrony.
  - The communication between processes is subject to unpredictable delays, which prevent the processes from agreeing on a common time or adjusting their clocks accordingly.
  - The distributed system may be subject to failures, such as network partitions, clock failures, or malicious attacks, which may compromise the accuracy or availability of any clock synchronization protocol.
- Therefore, distributed processes cannot rely on having an accurate view of the global state or the exact order of events, due to the absence of a global clock.
- Instead, distributed processes have to use alternative methods to achieve some form of logical or causal time or order, such as logical clocks, vector clocks, or Lamport timestamps.