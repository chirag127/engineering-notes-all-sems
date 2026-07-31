### Commit Protocols

- Commit protocols are algorithms that ensure the atomicity of distributed transactions, i.e., all the sites involved in a transaction either commit or abort it unanimously, even in the presence of failures  .
- Commit protocols involve a coordinator site that initiates the transaction and communicates with the participant sites that execute the transaction on behalf of the coordinator .
- There are different types of commit protocols, such as one-phase commit, two-phase commit, and three-phase commit, that vary in the number of phases and messages exchanged between the coordinator and the participants   .

#### One-Phase Commit Protocol

- A one-phase commit protocol involves only one phase, in which the coordinator sends a commit request to all the participants and waits for their replies.
- If all the participants reply with an OK message, the coordinator commits the transaction and sends a commit message to all the participants.
- If any participant replies with an abort message, the coordinator aborts the transaction and sends an abort message to all the participants.
- The advantages of this protocol are simplicity and low message overhead.
- The disadvantages of this protocol are lack of fault tolerance and concurrency control. If the coordinator or any participant fails, the transaction may be left in an inconsistent state. Also, the participants have to lock the resources until they receive the commit or abort message from the coordinator, which may cause blocking and deadlock.

#### Two-Phase Commit Protocol

- A two-phase commit protocol involves two phases: a voting phase and a commit phase  .
- In the voting phase, the coordinator sends a prepare message to all the participants, asking them to vote on whether to commit or abort the transaction  .
- Each participant replies with a yes or no vote, after executing the transaction and writing a prepare log record  .
- In the commit phase, the coordinator decides whether to commit or abort the transaction based on the votes received from the participants  .
- If all the votes are yes, the coordinator commits the transaction and sends a commit message to all the participants  .
- If any vote is no, the coordinator aborts the transaction and sends an abort message to all the participants  .
- Each participant commits or aborts the transaction according to the message received from the coordinator, and writes a commit or abort log record  .
- The advantages of this protocol are fault tolerance and concurrency control  . If the coordinator or any participant fails, the transaction can be recovered from the log records. Also, the participants can release the locks after the voting phase, which reduces the blocking and deadlock  .
- The disadvantage of this protocol is blocking  . If the coordinator fails after the voting phase, the participants have to wait indefinitely for the commit or abort message, which may cause the system to stall  .

#### Three-Phase Commit Protocol

- A three-phase commit protocol involves three phases: a prepare phase, a pre-commit phase, and a commit phase .
- The prepare phase is the same as in the two-phase commit protocol .
- In the pre-commit phase, the coordinator sends an enter prepared state message to all the participants, if all the votes are yes .
- The participants reply with an OK message, after entering a prepared state and writing a pre-commit log record .
- In the commit phase, the coordinator sends a commit message to all the participants, if all the OK messages are received .
- The participants commit the transaction and write a commit log record .
- If any vote is no or any OK message is not received, the coordinator sends an abort message to all the participants[^1^