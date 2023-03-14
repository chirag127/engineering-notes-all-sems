 Here is the content in markdown format for the given topic:

### Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- Transaction recovery is required in distributed systems to maintain consistency and atomicity in case of failures.
- The 2 phase commit protocol is used for transaction recovery which involves:
	- Phase 1: Commit request - The coordinator asks all participants if they are ready to commit. If all agree, they proceed to phase 2. Otherwise, the transaction is aborted.
	- Phase 2: Commit - The coordinator logs the commit decision and informs all participants to commit. The participants then make the changes permanent.
- In case of coordinator failure, the participants can't commit and the transaction is aborted. The coordinator failure is detected using a timeout mechanism.
- In case of participant failure, the coordinator aborts the transaction. The status of the failed participant is inferred from timeouts.
- Logging of read and write operations is done to facilitate rollback in case of aborts. The logs are flushed to stable storage for recovery.
- The 2 phase commit protocol ensures that either all participants commit or none, maintaining atomicity. It also reduces the blocking time as participants proceed with other work after phase 1 till phase 2.
- However, the protocol involves multiple messages and rounds of communication leading to performance overheads. It also has single points of failure in the coordinator.
- Possible mnemonics:
	- Phase 1: Ready? Phase 2: Go commit!
	- Ask all, log and inform - The 2 phase flow
- The key points to remember are the 2 phases, logging, recovery from failures and tradeoffs with performance. With regular practice, the steps can be easily memorized.