 Here is the content in markdown format for the given topic:

### Deadlock Prevention for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Avoid unnecessary resource holding: Avoid having a process hold resources longer than necessary. Release resources as early as possible to avoid deadlocks.
- Use resource hierarchy: Impose a total ordering of all resources and require that resources be requested and released in that order (e.g., ordering based on size). This prevents deadlock by preventing circular waiting.
- Limit the maximum number of resources: Limit the number of resources of each type that any process may hold. This bounds the resource that a process may hold below a threshold, thus preventing that process from being involved in a deadlock.
- Avoid indefinite postponement: Avoid excessive preemption of low-priority processes. This ensures that all processes make progress and do not wait indefinitely to acquire resources.

Mnemonics/Learning tricks:
- Avoid hogging resources: Think of resources as food and processes as people. If one person takes all the food, others will starve leading to deadlock. Release resources early.
- Order is important: Think of resources as people standing in a queue. Without order, circular waiting and chaos occurs leading to deadlock. Impose ordering to avoid circular waiting.
- Limit greed: Think of processes as people and resources as valuables. Put a limit on how many valuables a person can hold to avoid one person taking everything and causing deadlock. Limit resources per process.

[Diagrams and examples can be included here if required]

Advantages: Prevents deadlocks from occurring.
Disadvantages: May reduce system efficiency and throughput as additional overhead is required to manage and follow the prevention mechanisms. The mechanisms may not be practical to implement in some scenarios.
Applications: Used in resource allocation for operating systems, distributed systems, CPU scheduling, etc. to avoid deadlocks.