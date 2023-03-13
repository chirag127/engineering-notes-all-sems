### Underlying Principles of Parallel and Distributed Computing

- Parallel and distributed computing are two models of computation that aim to improve the performance and efficiency of complex applications by using multiple computing devices or processors .
- Parallel computing on a single computer uses multiple processors to process tasks in parallel, whereas distributed parallel computing uses multiple computing devices connected by a network to process those tasks.
- Parallel and distributed computing build on fundamental systems concepts, such as concurrency, mutual exclusion, consistency in state/memory manipulation, message-passing, and shared-memory models  .
- Concurrency is the ability of a system to execute multiple tasks simultaneously, either by interleaving them on a single processor or by assigning them to different processors.
- Mutual exclusion is the requirement that only one task can access a shared resource at a time, to prevent conflicts or inconsistencies.
- Consistency is the property that the state or memory of a system is coherent and reliable across all tasks and processors, regardless of the order or timing of operations.
- Message-passing is a communication model in which tasks exchange data or instructions by sending and receiving messages through a network.
- Shared-memory is a communication model in which tasks access a common memory space that can be read or written by any processor.
- Parallel and distributed computing can be classified into different types based on the degree of coupling, the granularity of tasks, the communication topology, and the synchronization mechanism.
- The degree of coupling refers to how tightly the processors or devices are connected and coordinated. It can range from loosely coupled (independent and autonomous) to tightly coupled (interdependent and synchronized).
- The granularity of tasks refers to how large or small the units of computation are. It can range from coarse-grained (large and complex tasks) to fine-grained (small and simple tasks).
- The communication topology refers to how the processors or devices are arranged and connected. It can be linear, circular, mesh, tree, hypercube, etc.
- The synchronization mechanism refers to how the tasks or processors coordinate their actions and timings. It can be based on clocks, barriers, locks, semaphores, etc.