# Unit 4 - Agreement Protocols

- Agreement protocols are a class of distributed algorithms that help processes in a network to reach a common decision in the presence of failures .
- Agreement protocols are useful for ensuring reliability, consistency, and fault tolerance in distributed systems, such as distributed databases, distributed consensus, leader election, and atomic broadcast  .
- Agreement protocols can be classified into two types: **consensus protocols** and **atomic commitment protocols** .
  - Consensus protocols require that all non-faulty processes agree on a single value proposed by one or more processes .
  - Atomic commitment protocols require that all non-faulty processes agree on whether to commit or abort a transaction that involves multiple processes .
- Agreement protocols face several challenges in distributed systems, such as asynchronous communication, message delays, message losses, process crashes, and process failures  .
- Agreement protocols must satisfy three properties: **validity**, **agreement**, and **termination** .
  - Validity means that the agreed value must be one of the proposed values .
  - Agreement means that all non-faulty processes must agree on the same value .
  - Termination means that all non-faulty processes must eventually decide on a value .
- Agreement protocols can be implemented using various techniques, such as message passing, voting, quorums, timeouts, and failure detectors   .
- Agreement protocols can be evaluated based on their performance, complexity, and fault tolerance .
  - Performance measures the time and communication costs of reaching an agreement .
  - Complexity measures the number of rounds and messages required to reach an agreement .
  - Fault tolerance measures the resilience of the protocol to different types of failures, such as crash failures, omission failures, and Byzantine failures .