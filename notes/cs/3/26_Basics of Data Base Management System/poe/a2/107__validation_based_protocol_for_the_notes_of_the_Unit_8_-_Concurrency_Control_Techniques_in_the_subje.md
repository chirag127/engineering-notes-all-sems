 Here is the formal content in markdown format without any emojis or external links for the given topic:

### Validation based protocol for the notes of the Unit 8 - Concurrency Control Techniques in the subject of Basics of Data Base Management System

1. Validation based protocols are used to ensure the correctness of the transaction execution. These protocols abort the transaction in case of any violation of consistency constraints or deadlock detection.
2. Two phase locking (2PL) is a validation based protocol which locks the data items in two phases.
- Growing phase: Data items are locked as and when required.
- Shrinking phase: All locks are released at the end of the transaction.
3. Strict 2PL: Data items can be locked only in a strict sequence i.e. if T1 locks X and then Y, then T2 can lock X only after locking Y. This ensures serializability but may lead to more number of aborts.
4. Rigorous 2PL: Locks can be acquired in any order but they must be released in reverse order. This protocol reduces the number of aborts as compared to strict 2PL.
5. The major limitation of 2PL is that it may lead to deadlock. So, it must be accompanied by a deadlock detection and resolution technique.

The above points cover the key highlights of validation based protocols for concurrency control in databases focusing on the two phase locking protocol. The points are written in a formal tone with no emotions or friendly remarks as per the given instructions.