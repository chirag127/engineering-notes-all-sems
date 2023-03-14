### Absence of Global Clock

- A global clock is a system-wide clock that is equally accessible to all processes in a distributed system and can be used to timestamp and order events.
- A distributed system is a collection of independent processes that communicate by exchanging messages over a network, but do not share any common memory or clock.
- Due to the absence of a global clock, the notion of common time does not exist in a distributed system; different processes may have different notions of time and clocks may drift apart.
- As a result, it is not always possible to determine the order in which two events on different processes were executed, or to obtain a consistent view of the system state.
- The absence of a global clock makes it difficult to design and debug algorithms for distributed systems, and to implement applications that require temporal ordering, synchronization, or coordination of events.
- To overcome this limitation, different schemes have been proposed to implement an abstract notion of time and to order events in a distributed system, such as physical clocks, logical clocks, vector clocks, and causal ordering.