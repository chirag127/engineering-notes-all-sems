 Here is the content in markdown format:

### System models for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- System models are abstract representations of a distributed system that captures essential aspects of its operation while ignoring the details.
- They are used to reason about the correctness and properties of distributed algorithms.
- Some commonly used system models are:
    - Synchronous vs asynchronous: In synchronous model, processes proceed in lockstep and there are bounds on message delay and processing time. In asynchronous model, there are no bounds on message delay and processing time. Asynchronous model is more practical but algorithms are harder to design.
    - Crash failures vs Byzantine failures: In crash failure model, processes just crash and stop executing. In Byzantine failure model, processes may behave arbitrarily. Byzantine model is more general but algorithms are more complex.
    - Shared memory vs message passing: In shared memory model, processes access shared memory. In message passing model, processes communicate by exchanging messages. Message passing model is more suitable for distributed systems.
- Examples of system models:
    - Synchronous shared memory model
    - Asynchronous message passing model with crash failures
    - Partially synchronous model (combines aspects of synchronous and asynchronous models)
    - Asynchronous model with Byzantine failures
- System models are important as they allow to reason about impossibility results (what can't be solved) and to design correct and efficient distributed algorithms. By choosing an appropriate system model, we can develop algorithms that make practical tradeoffs between efficiency, complexity, and fault-tolerance.