### System Models

System models are abstract representations of a distributed system that help in understanding, designing, and analyzing the behavior of the system. In the context of agreement protocols in distributed systems, there are several system models that are commonly used.

1. **Synchronous System Model**: In this model, there are known bounds on the time it takes for a message to be delivered and for a process to perform a step. This model is useful for designing algorithms with deterministic behavior.

2. **Asynchronous System Model**: In this model, there are no known bounds on the time it takes for a message to be delivered or for a process to perform a step. This model is more realistic than the synchronous model, but it makes designing algorithms more challenging.

3. **Partially Synchronous System Model**: This model is a hybrid of the synchronous and asynchronous models. It assumes that the system is synchronous most of the time, but there may be periods of asynchrony.

4. **Failure Model**: This model specifies the types of failures that can occur in the system. Common failure models include crash failures, where a process stops executing, and Byzantine failures, where a process may behave arbitrarily.

These system models are used to make assumptions about the behavior of the distributed system and to design algorithms that can tolerate the specified types of failures. Understanding these models is crucial for designing robust agreement protocols in distributed systems.