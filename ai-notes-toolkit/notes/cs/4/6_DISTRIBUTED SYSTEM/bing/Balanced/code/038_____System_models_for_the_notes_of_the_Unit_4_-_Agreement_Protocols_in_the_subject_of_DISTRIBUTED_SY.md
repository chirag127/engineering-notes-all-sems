### System models for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

A system model is a description of the properties and assumptions of a distributed system that are relevant for its design and analysis. System models can help us understand the behavior and limitations of a system, as well as compare different systems and algorithms.

There are three main types of system models:

- **Network models**: These models capture the characteristics and behavior of the communication network that connects the components of a distributed system. For example, network models can describe the reliability, latency, bandwidth, and topology of the network.
- **Node models**: These models capture the characteristics and behavior of the individual components of a distributed system, such as processes, servers, or devices. For example, node models can describe the availability, performance, and failure modes of the nodes.
- **Timing models**: These models capture the assumptions and guarantees about the timing and synchronization of events and actions in a distributed system. For example, timing models can describe the clock accuracy, message delivery order, and global time of the system.

Different system models can have different levels of abstraction and complexity, depending on the goals and requirements of the system. Some common system models are:

- **Synchronous system model**: This model assumes that there are known bounds on the network delay, node processing speed, and clock drift of the system. This model simplifies the design and analysis of distributed algorithms, but it is often unrealistic and impractical for real systems.
- **Asynchronous system model**: This model assumes that there are no bounds on the network delay, node processing speed, and clock drift of the system. This model is more realistic and general for real systems, but it makes the design and analysis of distributed algorithms more challenging and complex.
- **Partially synchronous system model**: This model assumes that there are bounds on the network delay, node processing speed, and clock drift of the system, but they are unknown or may change over time. This model is a compromise between the synchronous and asynchronous models, and it tries to capture the realistic behavior of real systems while still allowing some tractable analysis of distributed algorithms.
- **Crash-stop system model**: This model assumes that nodes can fail by crashing, which means that they stop executing and do not recover. This model simplifies the analysis of fault tolerance, but it does not account for other types of failures, such as network partitions, message losses, or Byzantine behavior.
- **Crash-recovery system model**: This model assumes that nodes can fail by crashing, but they can also recover and resume execution after some time. This model is more realistic and general for real systems, but it requires more complex mechanisms for state recovery and consistency.
- **Byzantine system model**: This model assumes that nodes can fail in arbitrary ways, which means that they can behave maliciously, dishonestly, or inconsistently. This model is the most pessimistic and challenging for fault tolerance, but it can capture the worst-case scenarios of real systems.

System models are essential for the design and analysis of agreement protocols in distributed systems. Agreement protocols are algorithms that allow a set of nodes to reach a common decision or value, despite the presence of failures and uncertainties in the system. Some examples of agreement protocols are:

- **Consensus protocol**: This protocol allows a set of nodes to agree on a single value, such as a leader, a transaction, or a configuration. Consensus is one of the most fundamental and difficult problems in distributed systems, and it has many applications and variations.
- **Atomic broadcast protocol**: This protocol allows a set of nodes to deliver a stream of messages in the same order, such that the order is consistent with the causal dependencies of the messages. Atomic broadcast is a useful abstraction for implementing replicated state machines and consistent databases.
- **Group membership protocol**: This protocol allows a set of nodes to maintain a consistent view of the current members of the system, and to detect and handle node failures and joins. Group membership is a basic service for building reliable and scalable distributed systems.

Different system models have different implications and limitations for the feasibility and performance of agreement protocols. For example, the famous FLP impossibility result shows that consensus is impossible to solve in an asynchronous system model with even one crash failure. On the other hand, consensus can be solved in a synchronous system model with up to half of the nodes crashing. However, synchronous system models are often too restrictive and unrealistic for real systems, so many practical consensus protocols use partially synchronous system models or additional assumptions, such as failure detectors, randomization, or trusted components.

System models are not fixed or universal, but rather they depend on the context