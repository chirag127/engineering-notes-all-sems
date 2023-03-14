### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A logical clock is a mechanism for capturing chronological and causal relationships in a distributed system. 
- Distributed systems may have no physically synchronous global clock, so a logical clock allows global ordering on events from different processes in such systems. 
- Logical clocks are useful in computation analysis, distributed algorithm design, individual event tracking, and exploring computational progress. 
- In logical clock systems, each process has two data structures: logical local time and logical global time. 
- Logical local time is used by the process to mark its own events, and logical global time is the local information about global time. 
- A special protocol is used to update logical local time after each local event, and logical global time when processes exchange data. 
- Logical clocks refer to implementing a protocol on all machines within your distributed system, so that the machines are able to maintain consistent ordering of events within some virtual timespan. 
- This is more formally specified as a way of placing events in some timespan so the following property will always be true: 

    - If event A happens before event B, then the timestamp of A is less than the timestamp of B. 

- This property is called the **happen-before** relation, and it is denoted by `->`. 
- The happen-before relation is transitive, meaning that if A -> B and B -> C, then A -> C. 
- The happen-before relation is also causally ordered, meaning that if A -> B, then any changes in A will be reflected in B. 
- However, not every pair of events in a distributed system has a happen-before relation. Some events may be concurrent, meaning that they are not causally related and can happen in any order. 
- This is denoted by `||`, meaning that A || B if neither A -> B nor B -> A. 
- Some noteworthy logical clock algorithms are: 

    - **Lamport timestamps**, which are monotonically increasing software counters. 
    - **Vector clocks**, that allow for partial ordering of events in a distributed system. 
    - **Version vectors**, order replicas, according to updates, in an optimistic replicated system. 
    - **Matrix clocks**, an extension of vector clocks that also contains information about other processes' views of the system. 

- A possible mnemonic for remembering the types of logical clocks is **LVM** (like Linux Volume Manager), which stands for **L**amport, **V**ector, and **M**atrix clocks. 
- A possible learning trick for understanding the happen-before relation is to use a physical analogy, such as sending and receiving messages, or writing and reading files. 
- For example, if Alice sends a message to Bob at 2:00 pm, and Bob receives it at 2:02 pm, then it is obvious that the sending event happens before the receiving event, and the timestamps reflect that. 
- However, if Alice and Bob are working on different files on their own computers, then their events are concurrent, and there is no causal relation between them. 
- Therefore, their timestamps may not be comparable, and they may need a vector clock or a matrix clock to capture the partial ordering of events. 

: https://www.geeksforgeeks.org/logical-clock-in-distributed-system/
: https://en.wikipedia.org/wiki/Logical_clock
: https://levelup.gitconnected.com/distributed-systems-physical-logical-and-vector-clocks-7ca989f5f780
: Personal suggestion