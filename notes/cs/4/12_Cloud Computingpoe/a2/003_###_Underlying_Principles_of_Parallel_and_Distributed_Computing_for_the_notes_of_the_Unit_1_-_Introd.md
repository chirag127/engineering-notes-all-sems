 Here is the content in markdown format for the topic ### Underlying Principles of Parallel and Distributed Computing for the notes of the Unit 1 - Introduction To Cloud Computing in the subject of Cloud Computing:

### Underlying Principles of Parallel and Distributed Computing

The following are the underlying principles of parallel and distributed computing:

1. Divide and Conquer: The problem is divided into smaller subproblems that are solved independently. The solutions to the subproblems are then combined to obtain the solution to the original problem. For example, search algorithms divide the list into halves and conquer each half recursively.

2. Parallelism: Multiple computational tasks are performed simultaneously. This allows the tasks to be completed faster than if they were performed sequentially one after the other. Parallelism can be achieved using multiple CPUs, cores, and machines.

3. Loose Coupling: The parallel components are relatively independent and communicate via message passing. There is no shared memory. Loose coupling makes parallel and distributed systems more scalable but synchronization is required to handle dependencies between components.

4. Locality: Computations are performed on data that is nearby to reduce communication overhead. Data and the processes operating on the data are placed close together.

5. Scalability: The system can handle increased load by adding more resources in a cost-effective manner. Scalability allows parallel and distributed systems to handle large volumes of work.

6. Fault Tolerance: The system can tolerate failures and continue operating correctly. Fault tolerance is achieved through redundancy and checkpointing. If a component fails, its tasks are rescheduled on other resources.

Advantages: Increased performance, resource utilization, and scalability.
Disadvantages: Complexity, non-determinism, and difficulty debugging and tuning.

Examples: Cluster computing, grid computing, cloud computing, and distributed databases.
Applications: Scientific computing, big data analysis, web services, and enterprise systems.