### System Models for Unit 4 - Agreement Protocols in Distributed Systems

1. **Synchronous System Model**: In this model, there are known bounds on message transmission delays and the relative speeds of processes. This allows for the use of timeouts and synchronized clocks to coordinate actions between processes.

2. **Asynchronous System Model**: In this model, there are no known bounds on message transmission delays or the relative speeds of processes. This makes it more difficult to coordinate actions between processes and requires the use of more complex algorithms to achieve agreement.

3. **Partially Synchronous System Model**: This model is a hybrid of the synchronous and asynchronous models. It assumes that there are known bounds on message transmission delays and the relative speeds of processes, but these bounds may change over time or may not always hold.

4. **Failure Models**: In distributed systems, it is important to consider the different types of failures that can occur, such as crash failures, omission failures, and Byzantine failures. Different agreement protocols may be designed to tolerate different types of failures.

5. **Communication Models**: Distributed systems can use different communication models, such as point-to-point communication, broadcast communication, or multicast communication. The choice of communication model can affect the design of agreement protocols.

These are some of the system models that are relevant to the study of agreement protocols in distributed systems. Understanding these models can help in the design and analysis of algorithms for achieving agreement in distributed systems.