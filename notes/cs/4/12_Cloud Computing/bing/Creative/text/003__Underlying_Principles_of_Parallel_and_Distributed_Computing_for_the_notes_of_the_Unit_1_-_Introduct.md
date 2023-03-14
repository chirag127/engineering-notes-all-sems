### Underlying Principles of Parallel and Distributed Computing

- Parallel and distributed computing is a computational model that breaks programs into smaller sequential operations and performs those smaller operations in parallel, either on multiple processors of a single computer or on multiple computing devices connected by a network .
- Parallel and distributed computing can speed up some types of algorithms by taking advantage of the simultaneous availability of multiple computing resources.
- Parallel and distributed computing builds on fundamental systems concepts, such as concurrency, mutual exclusion, consistency in state/memory manipulation, message-passing, and shared-memory models  .
- Concurrency refers to the execution of more than one procedure at the same time, either truly simultaneously (as on a multiprocessor) or in an unpredictably interleaved order.
- Mutual exclusion refers to the property that no two concurrent processes can access a shared resource at the same time.
- Consistency refers to the property that the state or memory of a system is coherent and valid at all times, regardless of concurrent operations.
- Message-passing refers to the communication model in which processes exchange data by sending and receiving messages.
- Shared-memory refers to the communication model in which processes access data by reading and writing to a common memory space.
- Parallel and distributed computing requires careful design and analysis of algorithms, architectures, networks, operating systems, and software engineering techniques to ensure correctness, efficiency, scalability, and reliability of the system .
- Parallel and distributed computing can be classified into different types based on the degree of coupling, the granularity of tasks, the communication topology, and the programming model .
- The degree of coupling refers to how tightly the processors or computing devices are connected and coordinated.
- The granularity of tasks refers to how large or small the subproblems or operations are in relation to the original problem.
- The communication topology refers to how the processors or computing devices are arranged and linked together.
- The programming model refers to how the parallel or distributed computation is expressed and implemented by the programmer.