### Commit Protocols

- Commit protocols are algorithms that ensure the atomicity of distributed transactions, i.e., all the sites involved in a transaction either commit or abort it unanimously, even in the presence of failures  .
- Commit protocols are necessary to maintain the consistency and reliability of distributed systems, as they prevent partial commits or inconsistent states  .
- There are different types of commit protocols, such as one-phase commit (1PC), two-phase commit (2PC), and three-phase commit (3PC)    .
- One-phase commit (1PC) is the simplest protocol, where a coordinator sends a commit request to all the participants, and they either commit or abort the transaction based on their local state .
- One-phase commit (1PC) has the advantage of being fast and simple, but it has the disadvantage of being unreliable, as it does not handle failures or concurrency issues .
- Two-phase commit (2PC) is the most widely used protocol, where a coordinator initiates a voting phase, where it asks all the participants to prepare to commit or abort the transaction, and then a commit phase, where it decides to commit or abort based on the votes    .
- Two-phase commit (2PC) has the advantage of being reliable and consistent, as it ensures that all the participants agree on the outcome of the transaction, and it handles failures by using timeouts and log records    .
- Two-phase commit (2PC) has the disadvantage of being blocking, as it requires all the participants to wait for the coordinator's decision, and it may cause deadlock or livelock if the coordinator or some participants fail or lose communication    .
- Three-phase commit (3PC) is an extension of 2PC, where a coordinator adds a pre-commit phase, where it asks all the participants to enter a prepared state, before sending the final commit or abort decision .
- Three-phase commit (3PC) has the advantage of being non-blocking, as it allows the participants to decide the outcome of the transaction independently if the coordinator fails or loses communication, and it avoids deadlock or livelock by using timeouts and majority voting .
- Three-phase commit (3PC) has the disadvantage of being more complex and costly, as it requires an extra phase and more messages, and it may still fail in some scenarios, such as network partitions or simultaneous failures .