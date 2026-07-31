Hello, I am Sydney, your AI assistant. I can help you with your notes on global state for the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM. Here is some information that I found from the web:

### Global State in Distributed Systems

- A **global state** of a distributed system is a collection of the **local states** of the processes and the channels that communicate among them .
- A local state of a process is the values of its variables, registers, program counter, etc. at a given point in time.
- A local state of a channel is the set of messages that have been sent but not yet received by the destination process.
- A global state can be used to determine properties of the distributed system, such as deadlock, termination, consistency, etc  .
- However, capturing a global state of a distributed system is not trivial, because the processes are concurrent and asynchronous, and there is no global clock or shared memory .
- Therefore, a global state must be **consistent**, meaning that it reflects a possible execution of the distributed system, and does not contain any causal anomalies .
- A causal anomaly is a situation where a process observes an effect before its cause, such as receiving a message before it is sent .
- A global state is consistent if it satisfies the **happened-before** relation, which defines a partial order among the events in the distributed system .
- The happened-before relation, denoted by ->, is defined as follows :
  - If a and b are events in the same process, and a occurs before b, then a -> b.
  - If a is the event of sending a message m by a process, and b is the event of receiving m by another process, then a -> b.
  - If a -> b and b -> c, then a -> c (transitivity).
- A **cut** of a distributed system is a subset of events that partitions the system into past and future .
- A cut is consistent if it contains no causal anomalies, i.e., if a -> b and b is in the cut, then a is also in the cut .
- A **snapshot** of a distributed system is a global state that is computed along a consistent cut .
- A snapshot can be taken by each process recording its local state and the state of its incoming channels, and exchanging messages with other processes to coordinate the cut .
- There are different algorithms for taking snapshots, such as the **Chandy-Lamport algorithm**, the **Lai-Yang algorithm**, the **Mattern's algorithm**, etc  .
- The main challenges of snapshot algorithms are to ensure consistency, completeness, accuracy, and efficiency  .