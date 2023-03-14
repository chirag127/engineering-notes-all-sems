The following is a detailed ASCII diagram for the concepts in backward and forward recovery for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM.

Backward recovery is based on the principle of rolling back the system to a previous consistent state after a failure or error has occurred. This is done by using checkpoints and logs to undo the effects of the failed transactions. Forward recovery is based on the principle of moving the system to a new consistent state after a failure or error has occurred. This is done by using logs to redo the effects of the committed transactions.

The diagram shows a distributed system with four processes (P1, P2, P3, P4) and a stable storage. The processes communicate with each other by sending and receiving messages. The stable storage is used to store the checkpoints and logs of the processes. The checkpoints are denoted by C and the logs are denoted by L. The messages are denoted by M with a sequence number.

The diagram also shows a scenario of a system failure that affects P2 and P4. The failure occurs after P2 has sent M3 to P3 and P4 has sent M4 to P1. The failure is detected by P1 and P3, who initiate the recovery process. The recovery process involves two steps: backward recovery and forward recovery.

Backward recovery:

P1 and P3 roll back to their previous checkpoints (C1 and C2 respectively) and undo the effects of the messages they have received after the checkpoints (M4 and M3 respectively) using their logs (L1 and L2 respectively). P2 and P4 also roll back to their previous checkpoints (C3 and C4 respectively) and undo the effects of the messages they have sent after the checkpoints (M3 and M4 respectively) using their logs (L3 and L4 respectively). The system is now in a consistent state before the failure.

Forward recovery:

P1 and P3 redo the effects of the messages they have sent after their checkpoints (M1 and M2 respectively) using their logs (L1 and L2 respectively). P2 and P4 also redo the effects of the messages they have received after their checkpoints (M1 and M2 respectively) using their logs (L3 and L4 respectively). The system is now in a consistent state after the failure.

The diagram is as follows:

```
    P1              P2              P3              P4
    |               |               |               |
    |               |               |               |
    |               |               |               |
    |               |               |               |
    |               |               |               |
    |               |               |               |
    |               |               |               |
    |               |               |               |
    |               |               |               |
    |               |               |               |
    |               |               |               |
    |<--------------|               |               |
    |     M4        |               |               |
    |               |               |               |
    |               |               |               |
    |               |               |               |
    |               |               |<--------------|
    |               |               |     M3        |
    |               |               |               |
    |               |               |               |
    |               |               |               |
    |               |               |               |
    |               |               |               |
    |               |               |               |
    |               |------->|------->|               |
    |               |     M2 |     M2 |               |
    |               |               |               |
    |               |               |               |
    |               |               |               |
    |               |               |               |
    |------->|------->|               |------->|------->|
    |     M1 |     M1 |               |     M1 |     M1 |
    |               |               |               |
    |               |               |               |
    |               |               |               |
    |               |               |               |
    |               |------->|------->|               |
    |               |     M3 |     M3 |               |
    |               |               |               |
    |               |               |               |
    |               |               |               |
    |<--------------|               |               |
    |     M4        |               |               |
    |               |               |               |
    |               |               |               |
    |               |               |               |
    |               |               |               |
C1  |               |C3             |C2             |C4
L