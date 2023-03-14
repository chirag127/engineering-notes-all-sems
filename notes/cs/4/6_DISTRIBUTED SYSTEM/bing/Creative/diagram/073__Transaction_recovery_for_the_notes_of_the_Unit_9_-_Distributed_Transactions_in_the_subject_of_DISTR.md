The following is a detailed ASCII diagram for transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM. The diagram is based on the Two-Phase Commit Protocol, which is one of the most famous methods of transaction recovery. The diagram shows the communication between the coordinator and the subordinates during the prepare and decision phases. The diagram also shows the possible states and actions of the subordinates depending on their votes and the coordinator's decision.

```
+----------------+      +----------------+      +----------------+
| Coordinator    |      | Subordinate 1  |      | Subordinate 2  |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|                |      |                |      |                |
|                |      |                |      |                |
|                |      |                |      |                |
|                |      |                |      |                |
|                |      |                |      |                |
|                |      |                |      |                |
|                |      |                |      |                |
|                |      |                |      |                |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+

Prepare phase:

+----------------+      +----------------+      +----------------+
| Coordinator    |      | Subordinate 1  |      | Subordinate 2  |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|                |      |                |      |                |
|                |      |                |      |                |
|                |      |                |      |                |
|                |      |                |      |                |
|                |      |                |      |                |
|                |      |                |      |                |
|                |      |                |      |                |
|                |----->| PREPARE        |----->| PREPARE        |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+

+----------------+      +----------------+      +----------------+
| Coordinator    |      | Subordinate 1  |      | Subordinate 2  |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|                |      |                |      |                |
|                |      |                |      |                |
|                |<-----| YES VOTE       |      |                |
|                |      | PREPARED       |      |                |
|                |      |                |      |                |
|                |      |                |      |                |
|                |      |                |<-----| NO VOTE        |
|                |      |                |      | ABORTED        |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+

Decision phase:

+----------------+      +----------------+      +----------------+
| Coordinator    |      | Subordinate 1  |      | Subordinate 2  |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|                |      |                |      |                |
|                |      |                |      |                |
| ABORT          |----->| ABORT          |----->| ABORT          |
|                |      |                |      |                |
|                |      | ABORTED        |      | ABORTED        |
|                |      |                |      |                |
|                |      |                |      |                |
|                |      |                |      |                |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```

The diagram is based on the following references:

: https://www.geeksforgeeks.org/transaction-recovery-in-distributed-system/
: https://www.ibm.com/docs/en/SSFKSJ_7.5.0/com.ibm.mq.dev.doc/q029330_.htm
: https://www.tutorialspoint.com/distributed_dbms/distributed_dbms_database_recovery.htm