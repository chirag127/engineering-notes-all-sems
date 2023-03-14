### Atomic Commit protocols for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

Atomic Commit protocols are used in distributed systems to ensure that a set of transactions are executed atomically, that is, either all the transactions are committed or none of them are, even if some of the nodes in the system fail or crash during the execution of the transactions. This ensures consistency and reliability in the system.

There are two types of Atomic Commit protocols:

1. Two-Phase Commit (2PC)

2. Three-Phase Commit (3PC)

#### Two-Phase Commit (2PC)

Two-Phase Commit (2PC) is the most widely used Atomic Commit protocol that ensures that all transactions are either committed or aborted. Here are the two phases in 2PC:

1. Prepare Phase: In this phase, the coordinator sends a "prepare" message to all the participants, asking them to vote whether they can commit or not. The participants reply with "yes" or "no" depending on their ability to commit the transaction.

2. Commit Phase: If all the participants vote "yes," then the coordinator sends a "commit" message to all the participants, and the participants perform the transaction and reply with an "acknowledge" message. If any participant votes "no," then the coordinator sends an "abort" message to all the participants, and the transaction is rolled back.

#### Three-Phase Commit (3PC)

Three-Phase Commit (3PC) is a more reliable version of the Atomic Commit protocol than 2PC. The three phases in 3PC are:

1. CanCommit Phase: In this phase, the coordinator sends a "canCommit" message to all the participants, asking them to vote whether they can commit or not. The participants reply with "yes," "no," or "wait" depending on their ability to commit the transaction.

2. PreCommit Phase: If all the participants vote "yes," then the coordinator sends a "preCommit" message to all the participants, and the participants perform the transaction and reply with an "acknowledge" message. If any participant votes "no," then the coordinator sends an "abort" message to all the participants, and the transaction is rolled back. If any participant votes "wait," then the coordinator waits for a specific amount of time before sending a "abort" or "preCommit" message.

3. Commit Phase: In this phase, the coordinator sends a "commit" message to all the participants, and the participants perform the transaction and reply with an "acknowledge" message.

Mnemonics and learning tricks:

One simple mnemonic to remember the difference between 2PC and 3PC is to think of them as "Two-Phase" and "Three-Phase." 2PC has two phases, while 3PC has three phases. Additionally, 3PC is more reliable than 2PC, as it has an additional "CanCommit" phase, which allows participants to vote "wait" if they need more time to prepare for the transaction.

In summary, Atomic Commit protocols ensure that transactions are executed atomically in distributed systems, even if some of the nodes in the system fail or crash during the execution of the transactions. Two-Phase Commit (2PC) and Three-Phase Commit (3PC) are the two types of Atomic Commit protocols, with 3PC being more reliable than 2PC. A simple mnemonic to remember the difference between them is to think of 2PC as "Two-Phase" and 3PC as "Three-Phase."