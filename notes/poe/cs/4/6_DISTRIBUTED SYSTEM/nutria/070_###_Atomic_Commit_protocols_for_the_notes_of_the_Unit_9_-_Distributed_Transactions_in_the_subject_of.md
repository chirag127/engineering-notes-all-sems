
### Atomic Commit Protocols for the Notes of the Unit 9 - Distributed Transactions in the Subject of DISTRIBUTED SYSTEM

Atomic commit protocols are used in distributed systems to ensure that all participating nodes reach a consensus on the outcome of a transaction. Atomic commit protocols ensure that either all of the changes made to the system during a transaction are applied, or none of them are applied. This ensures that the system remains in a consistent state after the transaction.

Atomic commit protocols can be divided into two categories: two-phase commit protocols and three-phase commit protocols.

#### Two-Phase Commit Protocols

Two-phase commit protocols are used when there are only two participants in the transaction, usually a client and a server. The two-phase commit protocol works in two phases. In the first phase, the client sends a request to the server to commit the transaction. The server then sends an acknowledgement to the client indicating that it is ready to commit the transaction. In the second phase, the client sends a request to the server to commit the transaction. The server then sends an acknowledgement to the client indicating that the transaction has been committed.

#### Three-Phase Commit Protocols

Three-phase commit protocols are used when there are more than two participants in the transaction. The three-phase commit protocol works in three phases. In the first phase, the client sends a request to all the participants to prepare to commit the transaction. The participants then send an acknowledgement to the client indicating that they are ready to commit the transaction. In the second phase, the client sends a request to all the participants to commit the transaction. The participants then send an acknowledgement to the client indicating that the transaction has been committed. In the third phase, the client sends a request to all the participants to confirm that the transaction has been committed. The participants then send an acknowledgement to the client indicating that the transaction has been confirmed.

Atomic commit protocols are used to ensure that all participating nodes reach a consensus on the outcome of a transaction. They are an important part of distributed systems and can be used to ensure that the system remains in a consistent state after a transaction.