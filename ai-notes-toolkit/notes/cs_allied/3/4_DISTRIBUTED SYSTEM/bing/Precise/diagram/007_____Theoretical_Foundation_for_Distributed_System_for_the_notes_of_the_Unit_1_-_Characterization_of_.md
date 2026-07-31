### Theoretical Foundation for Distributed System

Unit 1 - Characterization of Distributed Systems

1. A distributed system is a collection of independent computers that appear to the users of the system as a single coherent system.
2. The main goal of a distributed system is to make it easy for users and applications to access remote resources and to share them in a controlled and efficient manner.
3. Distributed systems can be characterized by the following properties:
    - Concurrency: Multiple components can operate simultaneously.
    - No global clock: There is no single global clock that can be used to order events.
    - Independent failures: Components can fail independently.
4. Theoretical models for distributed systems include the asynchronous model, the partially synchronous model, and the synchronous model.
5. The asynchronous model assumes no bounds on message transmission delays or relative process speeds.
6. The partially synchronous model assumes some bounds on message transmission delays and relative process speeds, but these bounds are not known a priori.
7. The synchronous model assumes known bounds on message transmission delays and relative process speeds.
8. These models are used to reason about the behavior of distributed algorithms and to prove their correctness.