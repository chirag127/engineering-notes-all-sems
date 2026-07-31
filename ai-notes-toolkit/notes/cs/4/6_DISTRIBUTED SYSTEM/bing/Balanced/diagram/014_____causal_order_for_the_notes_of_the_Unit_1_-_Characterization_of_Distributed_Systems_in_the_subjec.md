Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on causal order for the Unit 1 - Characterization of Distributed Systems.

### Causal order

- Causal order is a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps or their global order.
- Causal order is important for ensuring consistency and correctness of distributed applications that rely on message passing and shared state.
- Causal order is defined by the **happened-before** relation, denoted by `->`, which captures the notion of potential causality between events.
- The happened-before relation has the following properties :
  - If `a` and `b` are events in the same process, and `a` occurred before `b`, then `a -> b`.
  - If `a` is the event of sending a message by one process and `b` is the event of receiving that message by another process, then `a -> b`.
  - If `a -> b` and `b -> c`, then `a -> c` (transitivity).
  - Two events `a` and `b` are **concurrent**, denoted by `a || b`, if neither `a -> b` nor `b -> a`.
- Causal order implies that if a process observes some event `a`, then it must also observe all events that happened before `a`.
- Causal order can be implemented by using **vector clocks**, which are arrays of logical clocks that track the causal dependencies among processes .
- Vector clocks have the following properties :
  - Each process maintains a vector clock `VC[p]` of size `n`, where `n` is the number of processes in the system, and `VC[p][p]` is the logical clock of process `p`.
  - Initially, all entries of `VC[p]` are zero.
  - Whenever a process `p` executes an internal event, it increments `VC[p][p]` by one.
  - Whenever a process `p` sends a message `m`, it piggybacks `VC[p]` on `m` and increments `VC[p][p]` by one.
  - Whenever a process `q` receives a message `m` with a vector clock `VC[m]`, it updates its own vector clock `VC[q]` by taking the element-wise maximum of `VC[q]` and `VC[m]`, and then increments `VC[q][q]` by one.
- Vector clocks can be used to determine the causal order of events by comparing their vector clocks :
  - If `VC[a] < VC[b]`, meaning that `VC[a][i] <= VC[b][i]` for all `i` and `VC[a][j] < VC[b][j]` for some `j`, then `a -> b`.
  - If `VC[a] > VC[b]`, meaning that `VC[a][i] >= VC[b][i]` for all `i` and `VC[a][j] > VC[b][j]` for some `j`, then `b -> a`.
  - If `VC[a]` and `VC[b]` are incomparable, meaning that neither `VC[a] < VC[b]` nor `VC[a] > VC[b]`, then `a || b`.
- Causal order can be used to implement different consistency models for distributed systems, such as **causal consistency** and **total-causal order**  .
  - Causal consistency is a consistency model that guarantees that all processes see causally related updates in the same order, but concurrent updates may be seen in different orders.
  - Total-causal order is a consistency model that guarantees that all processes see all updates in the same order, which is consistent with the causal order.