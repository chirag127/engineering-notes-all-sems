### Application of Agreement problem

Agreement among the processes in a distributed system is a fundamental requirement for a wide range of applications. Many forms of coordination require the processes to exchange information to negotiate with one another and eventually reach a common understanding or agreement, before taking application-specific actions.

Reaching agreement in a distributed system is a fundamental issue of both theoretical and practical importance. Consensus, Atomic Commitment, Atomic Broadcast, Group Membership which are different versions of this paradigm underly much of existing fault-tolerant distributed systems.

- Byzantine Agreement Problems Model:
  - Total of n processes, at most m of which can be faulty
  - Reliable communication medium
  - Fully connected
  - Receiver always knows the identity of the sender of a message
  - Byzantine faults
  - Synchronous system
  - In each round, a process receives messages, performs computation, and sends messages.