### Commit Protocols

- Commit protocols are algorithms that ensure the atomicity of distributed transactions, i.e., all the sites involved in a transaction either commit or abort it unanimously, even in the presence of failures  .
- Commit protocols are initiated by a coordinator site, which communicates with the participating sites and directs them to execute, commit or abort the transaction .
- There are different types of commit protocols, such as one-phase commit, two-phase commit and three-phase commit, which differ in the number of phases and messages exchanged between the coordinator and the participants   .

#### One-Phase Commit Protocol

- A one-phase commit protocol involves a single phase, in which the coordinator sends a commit request to all the participants and waits for their replies.
- The participants execute the transaction and send back an acknowledgement to the coordinator, indicating whether they are ready to commit or not.
- The coordinator then decides to commit or abort the transaction based on the replies from the participants, and sends the final decision to all of them.
- The advantages of this protocol are simplicity and low message overhead, but the disadvantages are lack of fault tolerance and concurrency control.
- If the coordinator or any participant fails, the transaction may be left in an inconsistent state, as there is no way to recover or rollback the changes.
- If multiple transactions access the same data items, there may be conflicts or deadlocks, as there is no locking or synchronization mechanism.

#### Two-Phase Commit Protocol

- A two-phase commit protocol involves two phases, namely the voting phase and the commit phase  .
- In the voting phase, the coordinator sends a prepare request to all the participants, asking them to vote on whether they are ready to commit or not  .
- The participants execute the transaction and send back their votes to the coordinator, along with a promise to wait for the final decision  .
- The coordinator then collects all the votes and decides to commit or abort the transaction based on the majority rule, i.e., if all the votes are yes, then commit, otherwise abort  .
- In the commit phase, the coordinator sends the final decision to all the participants, and they either commit or abort the transaction accordingly  .
- The advantages of this protocol are fault tolerance and concurrency control, but the disadvantages are high message overhead and blocking problem  .
- If the coordinator or any participant fails, the transaction can be recovered or rolled back using the log records and the votes  .
- If multiple transactions access the same data items, there is a locking mechanism that prevents conflicts or deadlocks  .
- However, if the coordinator fails after sending the prepare request, the participants may be blocked indefinitely, as they do not know the final decision and cannot proceed with other transactions  .

#### Three-Phase Commit Protocol

- A three-phase commit protocol involves three phases, namely the prepare phase, the pre-commit phase and the commit phase .
- In the prepare phase, the steps are the same as in the two-phase commit protocol, i.e., the coordinator sends a prepare request to all the participants, and they send back their votes and wait for the final decision .
- In the pre-commit phase, the coordinator sends a pre-commit message to all the participants, indicating that it has decided to commit the transaction, and waits for their acknowledgements .
- The participants acknowledge the pre-commit message and enter a ready state, where they are prepared to commit the transaction, but have not done so yet .
- In the commit phase, the coordinator sends a commit message to all the participants, and they commit the transaction and send back their acknowledgements .
- The coordinator then collects all the acknowledgements and completes the transaction .
-