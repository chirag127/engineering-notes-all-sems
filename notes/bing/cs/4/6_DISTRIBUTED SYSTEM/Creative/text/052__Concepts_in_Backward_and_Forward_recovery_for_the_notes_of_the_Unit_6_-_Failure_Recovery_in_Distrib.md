### Concepts in Backward and Forward recovery for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Backward recovery and forward recovery are two techniques to restore the system to a consistent state after a failure.
- Backward recovery involves rolling back the system to a previous error-free state by undoing the effects of the failed transactions. Forward recovery involves correcting the errors and continuing the execution from the current state.
- Both techniques require logging the transactions and their effects on the system state.
- Backward recovery is more general and independent of the nature of faults, but it may require compensating actions to undo the committed transactions that depend on the failed ones. It may also cause cascading rollbacks and loss of useful work.
- Forward recovery is more efficient and preserves the useful work, but it requires accurate assessment and removal of the errors. It may not be possible to correct all types of errors in a distributed system.
- Backward recovery is suitable for short-lived transactions that do not affect other transactions. Forward recovery is suitable for long-lived transactions that have external dependencies and side effects.