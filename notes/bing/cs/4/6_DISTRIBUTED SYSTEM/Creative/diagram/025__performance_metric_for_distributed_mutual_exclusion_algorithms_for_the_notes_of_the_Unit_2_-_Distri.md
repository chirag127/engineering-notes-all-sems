The following is a detailed ASCII diagram for performance metric for distributed mutual exclusion algorithms for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM.

The diagram shows four processes (P1, P2, P3, P4) that are connected by a network and communicate by sending messages. Each process has a local clock (C1, C2, C3, C4) and a queue (Q1, Q2, Q3, Q4) to store the requests for the critical section (CS). The diagram also shows the four performance metrics that are used to evaluate the mutual exclusion algorithms:

- Message complexity (MC): the number of messages that are required per CS execution by a site.
- Synchronization delay (SD): the time required after a site leaves the CS and before the next site enters the CS.
- Response time (RT): the time interval between a request for the CS and the end of its execution.
- Throughput (TP): the number of CS executions per unit time.

The diagram illustrates a scenario where P1 requests the CS at time t1 and receives a reply from P2, P3, and P4 at time t2, t3, and t4 respectively. P1 enters the CS at time t5 and leaves the CS at time t6. P2 requests the CS at time t7 and receives a reply from P1, P3, and P4 at time t8, t9, and t10 respectively. P2 enters the CS at time t11 and leaves the CS at time t12. P3 and P4 do not request the CS in this scenario.

The diagram uses the following symbols and conventions:

- A solid line represents a message sent or received by a process.
- A dashed line represents the local clock of a process.
- A square bracket represents the queue of a process.
- A star (*) represents the CS execution by a process.
- A vertical bar (|) represents the time axis.
- A horizontal arrow (->) represents the direction of time.
- A label (t1, t2, etc.) represents the time of an event.

The diagram is as follows:

```
    P1          P2          P3          P4
    |           |           |           |
    |           |           |           |
    |---REQ---> |           |           |  t1: P1 requests CS
    |           |---REQ---> |           |  t7: P2 requests CS
    |           |           |---REQ---> |  t9: P3 replies to P2
    |           |           |           |---REQ--->  t10: P4 replies to P2
    |<--REPLY---|           |           |  t2: P2 replies to P1
    |           |<--REPLY---|           |  t8: P3 replies to P2
    |           |           |<--REPLY---|  t3: P3 replies to P1
    |           |           |           |<--REPLY---  t4: P4 replies to P1
    |           |<--REPLY---|           |  t6: P1 leaves CS
    |           |           |<--REPLY---|  t12: P2 leaves CS
    |           |           |           |
    |           |           |           |
    |           |           |           |
    |           |           |           |
    |           |           |           |
    |           |           |           |
    |           |           |           |
    |           |           |           |
    |           |           |           |
    |           |           |           |
    |           |           |           |
    |           |           |           |
    |           |           |           |
    |           |           |           |
    |           |           |           |
C1 |-----------|-----------|-----------|-----------|-> time
    |           |           |           |
    |           |           |           |
Q1 |[ ]        |[ ]        |[ ]        |[ ]        |
    |           |           |           |
    |           |           |           |
    |           |           |           |
    |           |           |           |
    |           |           |           |
    |           |           |           |
    |* CS *     |           |           |  t5: P1 enters CS
    |           |* CS *     |           |