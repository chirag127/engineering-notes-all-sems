Commit protocols are algorithms that ensure that a distributed transaction is either committed or aborted in its entirety, even if some of the nodes in the system fail or crash. They are essential for maintaining the consistency and integrity of the data in the system. There are different types of commit protocols, such as one-phase commit, two-phase commit, and three-phase commit. Each of them has its own advantages and disadvantages in terms of performance, reliability, and message complexity.

The following diagram illustrates the basic architecture of a distributed system with a coordinator and several participants, and how they communicate with each other using a two-phase commit protocol. The two-phase commit protocol consists of two phases: the prepare phase and the commit/abort phase. In the prepare phase, the coordinator asks the participants to vote on whether they are ready to commit or not. In the commit/abort phase, the coordinator decides to commit or abort the transaction based on the votes, and informs the participants of the decision.

```
+------------+              +------------+              +------------+
| Coordinator|              |Participant1|              |Participant2|
+------------+              +------------+              +------------+
     |                           |                           |
     |------------------DONE------------------->             |
     |                           |------------------DONE----->|
     |                           |                           |
     |<-----------------READY-------------------              |
     |-----------------PREPARE----------------->             |
     |                           |<-----------------READY-----|
     |                           |                           |
     |-----------------COMMIT------------------>             |
     |<-----------------ACK--------------------              |
     |                           |-----------------COMMIT---->|
     |                           |<-----------------ACK-------|
     |                           |                           |
+------------+              +------------+              +------------+
```