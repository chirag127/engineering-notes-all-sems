The consensus problem in distributed systems is to achieve overall system reliability in the presence of a number of faulty processes. This often requires coordinating processes to reach consensus, or agree on some data value that is needed during computation .

The following diagram illustrates the basic architecture of a consensus problem in distributed systems using ASCII art:

```
+-----------------+      +-----------------+      +-----------------+
| Process 1       |      | Process 2       |      | Process 3       |
|                 |      |                 |      |                 |
| +-------------+ |      | +-------------+ |      | +-------------+ |
| | Proposal    | |      | | Proposal    | |      | | Proposal    | |
| | (value 1)   | |      | | (value 2)   | |      | | (value 3)   | |
| +-------------+ |      | +-------------+ |      | +-------------+ |
|       |         |      |       |         |      |       |         |
|       |         |      |       |         |      |       |         |
|       V         |      |       V         |      |       V         |
| +-------------+ |      | +-------------+ |      | +-------------+ |
| | Consensus   | |      | | Consensus   | |      | | Consensus   | |
| | Algorithm   | |      | | Algorithm   | |      | | Algorithm   | |
| +-------------+ |      | +-------------+ |      | +-------------+ |
|       |         |      |       |         |      |       |         |
|       |         |      |       |         |      |       |         |
|       V         |      |       V         |      |       V         |
| +-------------+ |      | +-------------+ |      | +-------------+ |
| | Decision    | |      | | Decision    | |      | | Decision    | |
| | (value 2)   | |      | | (value 2)   | |      | | (value 2)   | |
| +-------------+ |      | +-------------+ |      | +-------------+ |
+-----------------+      +-----------------+      +-----------------+
```

The diagram shows three processes, each with a different proposal value. They use a consensus algorithm to communicate with each other and agree on a common decision value, which is the same for all processes. In this example, the decision value is 2, which is the majority of the proposals. The consensus algorithm ensures that the decision value is consistent, even if some processes fail or behave maliciously. Different consensus algorithms have different properties and assumptions, such as synchrony, fault tolerance, and security.