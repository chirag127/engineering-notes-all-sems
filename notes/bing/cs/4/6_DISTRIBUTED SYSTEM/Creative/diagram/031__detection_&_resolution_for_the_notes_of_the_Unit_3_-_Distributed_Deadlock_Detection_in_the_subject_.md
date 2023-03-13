The following is a detailed ASCII diagram for detection and resolution of distributed deadlock for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM.

The diagram is based on the path-pushing edge-chasing algorithm, which is one of the four classes of distributed deadlock detection algorithms. The algorithm works as follows:

- Each site maintains a wait-for graph (WFG) of its local transactions and the transactions that request locks on its resources.
- When a site detects a cycle in its local WFG, it initiates a probe message along the cycle to verify the global deadlock.
- The probe message contains the identities of the transactions involved in the cycle and a time stamp.
- The probe message is forwarded by each site along the cycle until it reaches the initiator site or a site that has already seen the probe message.
- If the probe message reaches the initiator site, a global deadlock is confirmed and a resolution action is taken, such as aborting one of the transactions in the cycle.
- If the probe message reaches a site that has already seen the probe message, the cycle is broken and the probe message is discarded.

The diagram shows an example of a distributed system with four sites (S1, S2, S3, S4) and six transactions (T1, T2, T3, T4, T5, T6). The arrows represent the wait-for dependencies between the transactions. The dotted arrows represent the probe messages sent by the sites to detect the deadlock.

```
+----+     +----+     +----+     +----+
| S1 |     | S2 |     | S3 |     | S4 |
+----+     +----+     +----+     +----+
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  v          v          v          v
+----+     +----+     +----+     +----+
| T1 |---->| T2 |---->| T3 |---->| T4 |
+----+     +----+     +----+     +----+
  ^          ^          ^          ^
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
+----+     +----+     +----+     +----+
| T5 |<----| T6 |<----| T5 |<----| T6 |
+----+     +----+     +----+     +----+

S1 detects a cycle in its local WFG: T1 -> T2 -> T6 -> T5 -> T1
S1 sends a probe message to S2: (T1, T2, T6, T5, T1, TS1)
S2 forwards the probe message to S4: (T1, T2, T6, T5, T1, TS1)
S4 forwards the probe message to S3: (T1, T2, T6, T5, T1, TS1)
S3 forwards the probe message to S1: (T1, T2, T6, T5, T1, TS1)
S1 receives the probe message and confirms the global deadlock
S1 aborts T1 and releases its resources
The deadlock is resolved
```