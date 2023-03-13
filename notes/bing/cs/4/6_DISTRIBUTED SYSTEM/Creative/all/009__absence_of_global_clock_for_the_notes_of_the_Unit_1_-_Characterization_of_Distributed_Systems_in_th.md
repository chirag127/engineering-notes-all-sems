### Absence of global clock for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A global clock is a hypothetical clock that would provide a common and accurate measure of time for all the processes in a distributed system.
- A global clock does not exist in reality because of the following reasons:
  - Each process in a distributed system has its own local clock that may run at a different rate or granularity than other clocks, leading to them being asynchronous .
  - The communication between processes in a distributed system is subject to unpredictable delays and failures, which makes it impossible to synchronize the clocks perfectly  .
  - The speed of light is finite, which means that any message sent from one process to another will take some time to reach its destination, and this time cannot be measured or compensated for without a global clock.
- The absence of a global clock has important implications for the design and implementation of distributed systems, such as:
  - The processes in a distributed system cannot rely on having an accurate view of the global state, due to transmission delays and concurrency .
  - The processes in a distributed system cannot use timestamps or sequence numbers to order events or messages, unless they agree on a common clock or a logical clock.
  - The processes in a distributed system cannot use timeouts or deadlines to coordinate their actions, unless they account for the clock drift and the network latency.
- Some possible solutions or alternatives to deal with the absence of a global clock are:
  - Using external time sources, such as atomic clocks or GPS, to provide a reference time for the processes, but this may be costly, inaccurate, or unavailable.
  - Using clock synchronization algorithms, such as NTP or Lamport's algorithm, to adjust the local clocks of the processes periodically, but this may introduce errors, overhead, or complexity.
  - Using logical clocks, such as vector clocks or causal clocks, to capture the causal or partial order of events or messages, but this may require additional information, storage, or computation.
  - Using physical clocks, such as Lamport's clocks or hybrid clocks, to approximate the real time or the global time, but this may have limitations, assumptions, or trade-offs.

: Limitation of Distributed System - GeeksforGeeks
: COP 5611 L03 - Florida State University
: Why is there no global clock in distributed systems? - Stack Overflow
: Time and State in Distributed Systems - University of Texas at Austin