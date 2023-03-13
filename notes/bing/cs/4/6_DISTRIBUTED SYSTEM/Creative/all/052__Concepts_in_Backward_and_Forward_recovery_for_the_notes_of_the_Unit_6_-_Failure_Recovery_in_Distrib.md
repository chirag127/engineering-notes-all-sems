### Concepts in Backward and Forward recovery for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Backward recovery and forward recovery are two techniques to restore the system to a consistent state after a failure .
- Backward recovery involves reverting the system to a previous error-free state by using checkpoints or logs . It does not depend on the nature of the faults, but it may require undoing the effects of previously committed transactions.
- Forward recovery involves correcting the errors in the current state and continuing the execution . It requires knowing the nature and the impact of the faults, but it avoids rolling back the system to an earlier state.
- A mnemonic to remember the difference between backward and forward recovery is: **Backward recovery goes back, forward recovery goes on**.
- An example of backward recovery is the undo operation in a text editor, which restores the previous state of the document.
- An example of forward recovery is the retry operation in a network communication, which attempts to resend the lost or corrupted packets.