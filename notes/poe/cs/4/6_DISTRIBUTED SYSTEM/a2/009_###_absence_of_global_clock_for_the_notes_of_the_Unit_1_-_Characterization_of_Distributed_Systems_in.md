 Here is the content in markdown format for the given topic:

### Absence of global clock for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- In distributed systems, there is no global clock. Each system has its own local clock which may or may not be synchronized with the clocks of other systems.
- This makes it difficult to assign timestamps and determine the ordering of events. There can be uncertainties in determining which event happened first.
- For example, if two processes P1 and P2 execute an event E1 and E2 respectively at their local times T1 and T2, it is not possible to say whether E1 happened before E2 or vice versa in an absolute sense. We can only say that either E1 happened before E2 or E2 happened before E1 based on the local times. But this ordering can be relative to the processes only and not in an absolute manner across the distributed system.
- To partially solve this, synchronization algorithms are used to synchronize the clocks of different systems. But these algorithms can't achieve perfect synchronization. Some amount of clock skew always remains.
- So, in distributed systems we have to make our algorithms and designs resilient to the absence of a perfectly synchronized global clock. We have to use concepts like logical clocks, causality, etc. to determine ordering and timestamps in a fairly accurate manner.

Some key points to remember:

- No global clock - each system has independent local clock
- Difficult to determine absolute ordering of events
- Have to use other mechanisms like logical clocks for ordering
- Clock synchronization algorithms can't achieve perfect synchronization
- Have to design systems resilient to lack of global clock