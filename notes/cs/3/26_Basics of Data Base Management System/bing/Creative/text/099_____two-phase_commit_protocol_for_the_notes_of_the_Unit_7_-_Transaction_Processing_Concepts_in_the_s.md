### Two-phase commit protocol

- The two-phase commit protocol (2PC) is a type of atomic commitment protocol (ACP) that ensures the atomicity and consistency of distributed transactions.
- A distributed transaction is a transaction that involves multiple sites (such as databases or servers) that need to agree on whether to commit or abort the transaction.
- The two-phase commit protocol consists of two phases: the prepare phase and the commit phase .
- In the prepare phase, a coordinator (a site that initiates the transaction) sends a prepare message to all the participants (the sites that execute the transaction) and asks them to vote on whether they are ready to commit or not .
- Each participant responds with a vote message: either prepared (meaning ready to commit) or aborted (meaning not ready to commit)  .
- The coordinator collects all the votes and decides the outcome of the transaction based on the majority rule: if all the participants vote prepared, the outcome is commit; otherwise, the outcome is abort .
- In the commit phase, the coordinator sends the outcome to all the participants and asks them to either commit or abort the transaction accordingly .
- Each participant follows the coordinator's decision and sends an acknowledgement message to the coordinator  .
- The coordinator waits for all the acknowledgements and then completes the transaction  .
- The two-phase commit protocol ensures that either all the participants commit the transaction or none of them do, thus preserving the atomicity and consistency of the distributed system .
- However, the two-phase commit protocol also has some drawbacks, such as:
  - It is a blocking protocol, meaning that the failure of a single site or a message loss can block the progress of the transaction until the site or the message recovers .
  - It has a high latency, meaning that it takes a long time to complete the transaction, as it depends on the slowest site or the longest message delay .
  - It is not resilient to network partitions, meaning that it cannot handle the situation when the sites are divided into two or more groups that cannot communicate with each other .