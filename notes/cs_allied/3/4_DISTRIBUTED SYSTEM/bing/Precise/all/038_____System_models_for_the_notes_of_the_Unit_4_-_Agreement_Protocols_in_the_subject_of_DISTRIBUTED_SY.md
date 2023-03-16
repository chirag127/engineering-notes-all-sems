### System Models for Unit 4 - Agreement Protocols in Distributed Systems

1. **Synchronous System Model**: In this model, there are known bounds on message transmission delays and the relative speeds of processes. This model is useful for designing algorithms with deterministic behavior.

2. **Asynchronous System Model**: In this model, there are no known bounds on message transmission delays or the relative speeds of processes. This model is more realistic and is used to design algorithms that can tolerate unpredictable behavior.

3. **Partially Synchronous System Model**: This model is a hybrid of the synchronous and asynchronous models. It assumes that the system is synchronous most of the time, but can occasionally behave asynchronously.

4. **Failure Models**: These models describe the types of failures that can occur in a distributed system. Common failure models include crash failures, omission failures, and Byzantine failures.

5. **Communication Models**: These models describe the ways in which processes in a distributed system can communicate with each other. Common communication models include message passing, shared memory, and remote procedure calls.

6. **Consistency Models**: These models describe the ways in which data can be kept consistent across multiple processes in a distributed system. Common consistency models include sequential consistency, causal consistency, and eventual consistency.

These system models are important for understanding the behavior of distributed systems and for designing algorithms that can operate correctly in the presence of failures and unpredictable behavior. They provide a framework for reasoning about the correctness of distributed algorithms and for analyzing their performance.