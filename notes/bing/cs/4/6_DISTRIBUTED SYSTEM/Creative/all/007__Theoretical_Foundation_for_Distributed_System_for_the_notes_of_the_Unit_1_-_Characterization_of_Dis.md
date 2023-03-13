### Theoretical Foundation for Distributed System for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a system whose components are located on different networked computers, which communicate and coordinate their actions by passing messages to one another.
- Distributed systems have some inherent limitations and challenges, such as:
  - The absence of a global clock, which makes it difficult to synchronize and order events across different processes .
  - The lack of shared memory, which requires explicit message passing and data replication for communication and coordination .
  - The arbitrary delays and failures of messages, which can cause inconsistency and uncertainty among processes .
- To cope with these limitations and challenges, distributed systems need some theoretical foundations and concepts, such as:
  - Logical clocks, which are mechanisms to assign logical timestamps to events and messages, and to establish a partial or total order among them .
  - Lamport's logical clocks, which are scalar values that are incremented by one at each event and piggybacked on each message, and satisfy the property that if event A happens before event B, then the timestamp of A is less than the timestamp of B .
  - Vector clocks, which are arrays of values that are incremented by one at each event and updated with the maximum of the local and received values at each message, and satisfy the property that if event A happens before event B, then the vector clock of A is element-wise less than or equal to the vector clock of B .
  - Message passing systems, which are models of distributed computation that assume a set of processes that communicate by sending and receiving messages over a network .
  - Distributed algorithms, which are algorithms that run on multiple processes and coordinate their actions by exchanging messages .

- A possible mnemonic to remember the limitations and challenges of distributed systems is **ADS** (Absence of global clock, Delay and failure of messages, Shared memory lack).
- A possible mnemonic to remember the concepts and foundations of distributed systems is **LVM** (Logical clocks, Vector clocks, Message passing systems).