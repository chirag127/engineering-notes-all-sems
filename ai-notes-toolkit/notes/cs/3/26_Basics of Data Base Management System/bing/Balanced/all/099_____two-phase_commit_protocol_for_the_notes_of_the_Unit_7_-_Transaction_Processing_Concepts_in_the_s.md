# Two-phase commit protocol

The two-phase commit protocol (2PC) is a type of atomic commitment protocol (ACP) that ensures the consistency of distributed transactions in a distributed system. A distributed transaction is a transaction that involves multiple processes or sites that may be geographically dispersed. The 2PC protocol coordinates all the processes or sites that participate in a distributed transaction on whether to commit or abort the transaction. The 2PC protocol has two phases: the prepare phase and the commit phase.

## Prepare phase

In the prepare phase, the following steps are performed:

- The coordinator (Ci) is the process or site that initiates the distributed transaction and acts as the leader of the protocol. The coordinator places a log record <Prepare T> on the log record at its site, where T is the transaction identifier.
- The coordinator sends a Prepare T message to all the participants (Pj), which are the processes or sites that execute some operations of the transaction T. The participants are also called cohorts or subordinates.
- Each participant (Pj) receives the Prepare T message and decides whether to vote for commit or abort. If the participant is ready to commit its part of the transaction, it writes a log record <Ready T> on its log and sends a Ready T message to the coordinator. If the participant decides to abort the transaction, it writes a log record <Abort T> on its log, undoes its part of the transaction, and sends an Abort T message to the coordinator.
- The coordinator waits for the votes from all the participants. If the coordinator does not receive a vote from a participant within a timeout period, it assumes that the participant has failed and votes for abort.

## Commit phase

In the commit phase, the following steps are performed:

- The coordinator decides the final outcome of the transaction based on the votes from the participants. If all the participants voted for commit, the coordinator decides to commit the transaction. If any participant voted for abort, or the coordinator itself decided to abort, the coordinator decides to abort the transaction.
- The coordinator writes a log record <Commit T> or <Abort T> on its log, depending on its decision, and sends a Commit T or Abort T message to all the participants.
- Each participant receives the Commit T or Abort T message from the coordinator and acts accordingly. If the participant receives a Commit T message, it writes a log record <Commit T> on its log and commits its part of the transaction. If the participant receives an Abort T message, it writes a log record <Abort T> on its log, undoes its part of the transaction, and releases any locks it may have acquired.
- Each participant sends an Ack T message to the coordinator to acknowledge the completion of the commit or abort operation.
- The coordinator waits for the acknowledgments from all the participants. If the coordinator does not receive an acknowledgment from a participant within a timeout period, it assumes that the participant has failed and resends the Commit T or Abort T message to the participant.
- The coordinator writes a log record <End T> on its log to indicate the end of the transaction.

## Advantages and disadvantages of 2PC

The main advantage of 2PC is that it guarantees the atomicity of distributed transactions, meaning that either all the participants commit or all the participants abort. This ensures the consistency and integrity of the distributed data.

The main disadvantages of 2PC are:

- It is a blocking protocol, meaning that the failure of a single participant or the coordinator blocks the progress of the transaction until the failed process recovers. Moreover, if the coordinator fails, the participants may be left in an uncertain state, waiting for the final decision from the coordinator. This leads to a loss of availability and concurrency in the system.
- It is a costly protocol, meaning that it requires a lot of messages and log writes to coordinate the distributed transaction. The number of messages and log writes is proportional to the number of participants involved in the transaction. This leads to a high latency and overhead in the system.
- It is a rigid protocol, meaning that it does not allow any flexibility or optimization in the execution of the distributed transaction. For example, it does not allow early commits or read-only transactions that do not need to participate in the protocol. This leads to a loss of performance and scalability in the system.